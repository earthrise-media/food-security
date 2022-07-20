"""
# My first app
Here's our first attempt at using data to create a table:
"""

import numpy as np
import pandas as pd
import streamlit as st
from requests.auth import HTTPBasicAuth
import requests
# Need dependency file to support these packages
# import geopandas as gpd
# import matplotlib.pyplot as plt

# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df
# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
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
countries = "https://apps.fas.usda.gov/OpenData/api/esr/countries"
commodities = "https://apps.fas.usda.gov/OpenData/api/esr/commodities"
unitsofmeasure = "https://apps.fas.usda.gov/OpenData/api/esr/commodities"
wheat = "https://apps.fas.usda.gov/OpenData/api/esr/exports/commodityCode/101/allCountries/marketYear/2021"
endpointlist = [regions, countries, commodities, unitsofmeasure, wheat]
codelist = []
commodityCode = "107"
marketYear = "2021"
ccydf = pd.DataFrame()
# for u in endpointlist:
#     headers_dict = {"API_KEY": "aefd68b9-cfdc-4c9e-a800-b457ff5adade"}
#     URL = u
#     data = requests.get(url=URL, headers=headers_dict)
#     # create list of dictionaries.
#     st.table(pd.read_json(data.text))

# USDA api key
headers_dict = {"API_KEY": "aefd68b9-cfdc-4c9e-a800-b457ff5adade"}
URL = countries
data = requests.get(url=URL, headers=headers_dict)
# converts to pandas df
countrydf = pd.read_json(data.text)
# all countries read from USDA website
st.table(countrydf)
# this populates menu with country names
chosencountry = st.multiselect("country", countrydf["countryDescription"])
# This converts the chosen country names into country codes.
for c in chosencountry:
  codelist.append(countrydf.loc[(countrydf['countryDescription'].str.contains(c, case=False)), 'countryCode'].iloc[0])

st.write('You selected:', codelist)

for c in codelist:
  # ccyurl = "https://apps.fas.usda.gov/OpenData/exports/commodityCode/{commodityCode}/countryCode/{countryCode}/marketYear/{marketYear}". format(commodityCode, c, marketYear)
  ccyurl = "https://apps.fas.usda.gov/OpenData/api/esr/exports/commodityCode/107/countryCode/"+str(c)+"/marketYear/2021"
  d = requests.get(url=ccyurl, headers=headers_dict)
  ccydf = pd.read_json(d.text).set_index('weekEndingDate')
  # ccydf.set_index('weekEndingDate')
  st.write('commodity', ccydf)
  st.area_chart(ccydf["grossNewSales"])
  st.line_chart(ccydf["grossNewSales"])
  st.bar_chart(ccydf["grossNewSales"])
