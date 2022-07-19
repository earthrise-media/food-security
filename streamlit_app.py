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
import geopandas as gpd
import matplotlib.pyplot as plt

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart

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
for u in endpointlist:
    headers_dict = {"API_KEY": "aefd68b9-cfdc-4c9e-a800-b457ff5adade"}
    URL = u
    data = requests.get(url=URL, headers=headers_dict)
    # create list of dictionaries.
    st.table(pd.read_json(data.text))