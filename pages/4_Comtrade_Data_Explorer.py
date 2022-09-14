import pandas as pd
import streamlit as st
import requests
from datetime import date


# Get's data from comtrade
def get_comtrade_data(endpoint_url):
     request = requests.get(url=endpoint_url)
     print (request)
     print ("length is " + str(len(request.json()["dataset"])))
     return (pd.json_normalize(request.json()["dataset"]))
    
page_title = st.sidebar.empty()
page_title.header("Comtrade Data Explorer")
st.title("Comtrade Data Explorer")

# Endpoints
country_url = "https://comtrade.un.org/Data/cache/reporterAreas.json"
commodity_url = "https://comtrade.un.org/Data/cache/classificationHS.json"

country_request = requests.get(url=country_url)
country_request.encoding='utf-8-sig'
country_df = pd.json_normalize(country_request.json()["results"])
# st.write(country_df)

# todo perhaps limit commodity list to 2 digit commodity codes
commodity_request = requests.get(url=commodity_url)
commodity_request.encoding='utf-8-sig'
commodity_df = pd.json_normalize(commodity_request.json()["results"])
# st.write(commodity_df)

year_list = [item for item in range(2000, date.today().year+1)]

region = st.selectbox(
     'Region of Interest',
     (country_df["text"]))

commodity = st.selectbox(
     'Region of Interest',
     (commodity_df["text"]))
commodity_string = commodity.rsplit('- ')[1]
print(commodity_string)

impex = st.radio(
     f"Imports to {region} or Exports from {region}?",
     ('Imports', 'Exports'))

selected_years = st.multiselect("Select Years", year_list)
year_string = ""
for y in selected_years:
     year_string += str(y)+"&"
print ("year string is " + year_string)

country_code = country_df.loc[country_df['text'] == region, 'id'].item()
commodity_code = commodity_df.loc[commodity_df['text'] == commodity, 'id'].item()
print (commodity_code)

# todo run on button click
if year_string and country_code and commodity_code:
     if impex == "Imports":
          request_url = f"https://comtrade.un.org/api/get?max=50000&type=C&freq=A&px=HS&ps={year_string}r={country_code}&p=all&rg=1&cc={commodity_code}"
     elif impex == "Exports":
          request_url = f"https://comtrade.un.org/api/get?max=50000&type=C&freq=A&px=HS&ps={year_string}r=all&p={country_code}&rg=1&cc={commodity_code}"

     print (request_url)
     
     if impex == "Imports":
          prep1 = " to "
          prep2 = " from "
          region_title = "ptTitle"
     else: 
          prep1 = " from "
          prep2 = " to "
          region_title = "rtTitle"

     chart_df = get_comtrade_data(request_url)
     if len(chart_df) > 0:
          chart_df = chart_df[["period", region_title, "TradeValue"]]
          chart_df.set_index(region_title, inplace=True)
          chart_df.sort_values(by="TradeValue", ascending=[False], inplace=True)
          st.header(str(commodity_string)+" "+str(impex)+prep1+str(region)+prep2+"the world")
          st.write(chart_df)
     else:
          st.write("No data found for this query")

