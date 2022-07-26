import cmath
import numpy as np
import pandas as pd
import streamlit as st
from requests.auth import HTTPBasicAuth
import requests
# Need dependency file to support these packages
import geopandas as gpd
from datetime import date
# # import matplotlib.pyplot as plt

# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df
# Draw a title and some text to the app:
'''
# USDA data API Experiments
Work in progress
'''

# df = pd.DataFrame({'col1': [1,2,3]})
# df  # 👈 Draw the dataframe

# x = 10
# 'x', x  # 👈 Draw the string 'x' and then the value of x

# # Also works with most supported chart types
# arr = np.random.normal(1, 1, size=100)
# fig, ax = plt.subplots()
# ax.hist(arr, bins=20)

# fig  # 👈 Draw a Matplotlib chart

# headers_dict = {"API_KEY": "aefd68b9-cfdc-4c9e-a800-b457ff5adade"}
# URL = "https://apps.fas.usda.gov/OpenData/api/esr/regions"
# wData = requests.get(url=URL, headers=headers_dict)
# st.table(wData.text)

# Endpoints
regions = "https://apps.fas.usda.gov/OpenData/api/esr/regions"
country_url = "https://apps.fas.usda.gov/OpenData/api/esr/countries"
commodity_url = "https://apps.fas.usda.gov/OpenData/api/esr/commodities"
unitsofmeasure = "https://apps.fas.usda.gov/OpenData/api/esr/commodities"
wheat = "https://apps.fas.usda.gov/OpenData/api/esr/exports/commodityCode/101/allCountries/marketYear/2021"
# endpointlist = [regions, countries, commodities, unitsofmeasure, wheat]
dfd = {}
def create_df(country, commodity, year):
        requesturl = "https://apps.fas.usda.gov/OpenData/api/esr/exports/commodityCode/"+str(commodity)+"/countryCode/"+str(country)+"/marketYear/"+str(year)
        print(requesturl)
        d = requests.get(url=requesturl, headers=key)
        dfd_name = "df_{}".format(str(country)+"_"+str(commodity)+"_"+str(year))
        print (dfd_name)
        dfd[dfd_name] = pd.read_json(d.text).set_index('weekEndingDate')
        return (dfd)
        # ccydf = pd.read_json(d.text).set_index('weekEndingDate')
#  "df_{}".format(str(country)+"_"str(commodity)+"_"+str(year))
codelist = []
commodityCode = "107"
marketYear = "2021"
ccydf = pd.DataFrame()
selection_dict = {}
commodity_dict = {}

# USDA api key
key = {"API_KEY": "aefd68b9-cfdc-4c9e-a800-b457ff5adade"}
# probably should add a country vs. region vs. rest of world selection here at some point
country_request = requests.get(url=country_url, headers=key)
commodity_request = requests.get(url=commodity_url, headers=key)

# converts to pandas df for the selection menus
country_list = pd.read_json(country_request.text)
commodity_list = pd.read_json(commodity_request.text)
year_list = [item for item in range(2000, date.today().year+1)]

st.write(commodity_list)

# creates the menus
selected_countries = st.multiselect("Select Countries", country_list["countryDescription"])
selected_years = st.multiselect("Select Years", year_list)
selected_commodity = st.multiselect("Select Commodities", commodity_list["commodityName"])

# creates dictionary with commodity name: code key: value pairs
if selected_commodity:
  clist = []
  for com in selected_commodity:
    com_entry_dict = {}
    com_entry_dict[com] = commodity_list.loc[(commodity_list['commodityName'].str.contains(com, case=False)), 'commodityCode'].iloc[0]
    clist.append(com_entry_dict)

# populating selection_dict
for name in selected_countries:
  code_dict = {"code": country_list.loc[(country_list['countryDescription'].str.contains(name, case=False)), 'countryCode'].iloc[0]}
  if selected_commodity:
    commodity_dict = {"commodity": clist}
  else:
    commodity_dict = {"commodity": None}
  year_dict = {"year": selected_years}
  df_dict = {"df": []}
  selection_dict[name] = code_dict, commodity_dict, year_dict, df_dict
  

'''
## Accumulated exports of selected countries
Errors vaguely if data does not exist
'''
if selected_countries and selected_commodity and selected_years:
  chart_df = pd.DataFrame()
  for n in selection_dict:
    for cm in commodity_dict["commodity"]:
      for y in year_dict["year"]:
        ctry_name = n
        ctry_code = selection_dict[n][0]["code"]
        com_name = next(iter(cm.keys()))
        com_code = next(iter(cm.values()))
        df_dict["df"].append(create_df(ctry_code, com_code, y))
        st.write(dfd["df_"+str(ctry_code)+"_"+str(com_code)+"_"+str(y)])
        chart_df[n] = dfd["df_"+str(ctry_code)+"_"+str(com_code)+"_"+str(y)]["accumulatedExports"]
        # print (next(iter(selection_dict[n][3].values())))

# st.write("dictionary is ", selection_dict)


# def create_chart():
#   chart_df = pd.DataFrame()
#   for n in selection_dict:
#     print(n)
#     for d in selection_dict[n][3]["df"]:
#       for df in d.values():
#         chart_df[n] = df[['accumulatedExports']].copy()
#         print(chart_df)
#         # st.write(chart_df)
#         # chart_df.rename(columns = {'accumulatedExports':n})

#         # chart_df[n] = df[['accumulatedExports']].copy()
#   print(chart_df)
  st.area_chart(chart_df)
  st.write(chart_df)
    # chart_df[n] = next(iter(selection_dict[n][3].values()))[['accumulatedExports']].copy()
  # print (chart_df)

# create_chart()


  # create_df(1220, 107, 2021)
  # st.write(df_dict["df_1220_107_2021"])
  # st.write(df_dict[0])
  # for co in selected_countries:
  #   for cm in selected_commodity:
  #     for y in selected_years:


        


# This adds a key with country name to dictionary with code value
# in the future it will probably be better to do this as a function that runs on change of menus defined above.

  # codelist.append(country_list.loc[(country_list['countryDescription'].str.contains(name, case=False)), 'countryCode'].iloc[0])
  # countryCode = country_list.loc[(country_list['countryDescription'].str.contains(name, case=False)), 'countryCode'].iloc[0]
  # selections[name] = 's'

#   codelist.append(country_list.loc[(country_list['countryDescription'].str.contains(name, case=False)), 'countryCode'].iloc[0])
#   countryCode = country_list.loc[(country_list['countryDescription'].str.contains(name, case=False)), 'countryCode'].iloc[0]
#   selections[name] = 's'
# st.write('You selected:', codelist)
# # dict structure:
# name: code, [commodities], [years]

# '''### Price of wheat from chosen country over 2021'''
# for c in codelist:
#   # ccyurl = "https://apps.fas.usda.gov/OpenData/exports/commodityCode/{commodityCode}/countryCode/{countryCode}/marketYear/{marketYear}". format(commodityCode, c, marketYear)
#   ccyurl = "https://apps.fas.usda.gov/OpenData/api/esr/exports/commodityCode/107/countryCode/"+str(c)+"/marketYear/2002"
#   d = requests.get(url=ccyurl, headers=headers_dict)
#   ccydf = pd.read_json(d.text).set_index('weekEndingDate')
#   # ccydf.set_index('weekEndingDate')
#   st.write('commodity', ccydf)
#   st.area_chart(ccydf["grossNewSales"])
#   st.line_chart(ccydf["grossNewSales"])
#   st.bar_chart(ccydf["grossNewSales"])

  # creating a dictionary of pandas dataframes to make streamlit graphs
# cnt = 22  # your loop
# dict_of_df = {} # initialize empty dictionary
# for c in codelist:
#   ccyurl = "https://apps.fas.usda.gov/OpenData/api/esr/exports/commodityCode/107/countryCode/"+str(c)+"/marketYear/2021"
#   d = requests.get(url=ccyurl, headers=headers_dict)
#   ccydf = pd.read_json(d.text).set_index('weekEndingDate')
#   newname = df_sheetnames['col'].values[i]
#   dict_of_df["df_{}".format(i)] = pd.read_excel('DATA.xlsx', sheetname=newname, skiprows=6, usecols=[14,15,16])
# # You can access the dataframes by call dict_of_df[key], where key = "df_1", "df_2", ... , "df_22"