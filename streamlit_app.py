import cmath
from jupyter_client import run_kernel
import numpy as np
import pandas as pd
import streamlit as st
import requests
from datetime import date

# def create_df(country, commodity, year):
#         requesturl = "https://apps.fas.usda.gov/OpenData/api/esr/exports/commodityCode/"+str(commodity)+"/countryCode/"+str(country)+"/marketYear/"+str(year)
#         print(requesturl)
#         d = requests.get(url=requesturl, headers=key)
#         dfd_name = "df_{}".format(str(country)+"_"+str(commodity)+"_"+str(year))
#         print (dfd_name)
#         dfd[dfd_name] = pd.read_json(d.text).set_index('weekEndingDate')
#         return (dfd)

def get_usda_data(endpoint_url):
    # USDA API Key
    key = {"API_KEY": "aefd68b9-cfdc-4c9e-a800-b457ff5adade"}
    request = requests.get(url=endpoint_url, headers=key)
    print(request.headers['Content-Length'])
    # convert response to pandas dataframe
    if int(request.headers['Content-Length']) > 2:
      return (pd.read_json(request.text))
    else: 
      return (False)

# Endpoints
# regions = "https://apps.fas.usda.gov/OpenData/api/esr/regions"
country_url = "https://apps.fas.usda.gov/OpenData/api/esr/countries"
commodity_url = "https://apps.fas.usda.gov/OpenData/api/esr/commodities"
units_url = "https://apps.fas.usda.gov/OpenData/api/esr/unitsOfMeasure"

# USDA api key
key = {"API_KEY": "aefd68b9-cfdc-4c9e-a800-b457ff5adade"}
# probably should add a country vs. region vs. rest of world selection here at some point
country_request = requests.get(url=country_url, headers=key)
commodity_request = requests.get(url=commodity_url, headers=key)
units_request = requests.get(url=units_url, headers=key)

# converts to pandas df for the selection menus
country_list = pd.read_json(country_request.text)
commodity_list = pd.read_json(commodity_request.text)
units_list = pd.read_json(units_request.text)
year_list = [item for item in range(2000, date.today().year+1)]
com_categories = ['commodityCode', 'countryCode', 'weeklyExports', 'accumulatedExports', 'outstandingSales', 'grossNewSales', 'currentMYNetSales', 'currentMYTotalCommitment', 'nextMYOutstandingSales', 'nextMYNetSales', 'unitId', 'weekEndingDate']

# st.write(commodity_list)
# st.write(units_list)
st.title("US Export Sales Reporting (ESR) Data Explorer")
st.markdown("USDA's Export Sales Reporting Program monitors U.S. agricultural export sales on a daily and weekly basis. Export sales reporting provides a constant stream of up-to-date market information for 40 U.S. agricultural commodities sold abroad. In a typical year, the program monitors more than 40 percent of total U.S. agricultural exports. The program also serves as an early alert on the possible impact foreign sales have on U.S. supplies and prices. The weekly U.S. Export Sales report is the most currently available source of U.S. export sales data. The data is used to analyze the overall level of export demand, determine where markets exist, and assess the relative position of U.S. commodities in foreign markets. [Learn more here](https://apps.fas.usda.gov/opendataweb/about)")
# creates the menus
selected_countries = st.multiselect("Select Countries", country_list["countryDescription"])
selected_years = st.multiselect("Select Years", year_list)
selected_commodity = st.multiselect("Select Commodities", commodity_list["commodityName"])
selected_cat = st.multiselect("Select Comparison Categories", com_categories[2:9])

# creates dictionary with commodity name: commodity code key: value pairs
com_entry_dict = {}
if selected_commodity:
  for com in selected_commodity:
    com_entry_dict[com] = commodity_list.loc[(commodity_list['commodityName'].str.contains(com, case=False)), 'commodityCode'].iloc[0]

# creates dictionary with country name: country code key: value pairs
cou_entry_dict = {}
if selected_countries:
  for cou in selected_countries:
    cou_entry_dict[cou] = country_list.loc[(country_list['countryDescription'].str.contains(cou, case=False)), 'countryCode'].iloc[0]

# gets all the data from API and adds to request_dict
# this might be better as a class rather than dictionary but maybe that ship has sailed
request_dict = {}
for cou in cou_entry_dict:
  for com in com_entry_dict:
    for y in selected_years:
      request_url = "https://apps.fas.usda.gov/OpenData/api/esr/exports/commodityCode/{commodity_code}/countryCode/{country_code}/marketYear/{year}"
      r = get_usda_data(request_url.format(commodity_code = com_entry_dict[com], country_code = cou_entry_dict[cou], year = y))
      # ensures that when the call comes back with no data it doesn't throw an error
      if isinstance(r, pd.DataFrame):
        request_dict[str(y)+"|"+str(com)+"|"+str(cou)] = r.set_index('weekEndingDate')
      else:
        # What is written to page if URL doesn't have data returned
        st.markdown('_Note: No data was returned for "' + com.lower() + '" exported to ' + cou.capitalize() + "in " + str(y) + ' it has not been included in the charts below._')



chart_dict ={}
for y in selected_years:
  for com in selected_commodity:
    for cat in selected_cat:
      chart_dict[str(y)+str(com)+str(cat)] = pd.DataFrame()

# Creates data frames for charts
for df in request_dict:
  for cat in selected_cat:
    # for reference:
    # year name is df[0:4]
    # commodity name is df.split('|', 2)[1]
    # country name is df.rsplit('|', 1)[1]
    dfname = df[0:4]+df.split('|', 2)[1]+cat
    cat_col = request_dict[df][cat].to_frame()
    chart_dict[dfname] = pd.concat([chart_dict[dfname], cat_col], axis=1)
    chart_dict[dfname].rename(columns={cat: df.rsplit('|', 1)[1].capitalize()}, inplace=True)

# for debugging
# st.write(chart_dict.keys())

for e in chart_dict:
  st.subheader(e)
  st.write(chart_dict[e])
  st.area_chart(chart_dict[e])