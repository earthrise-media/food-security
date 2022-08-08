import cmath
import numpy as np
import pandas as pd
import streamlit as st
from requests.auth import HTTPBasicAuth
import requests
# Need dependency file to support these packages
import geopandas as gpd
from datetime import date



fews_url = "https://fdw.fews.net/api/ipcphasemap/?country_code=CM&collection_date=2022-05-01&format=geojson"
gdf = gpd.read_file(fews_url)

st.map(gdf)