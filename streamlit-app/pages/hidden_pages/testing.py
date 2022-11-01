import numpy as np
import pandas as pd
import geopandas as gpd
import streamlit as st
import pydeck as pdk
import plotly.express as px
from urllib.request import urlopen
import json
mbtoken = "pk.eyJ1IjoiaGlnaGVzdHJvYWQiLCJhIjoiY2w2cjRpc2wzMTB3bDNkcjNraWcwMDQ5NCJ9.o1tPQcVhzDZ4JNtD-19aCg"

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

import plotly.express as px

fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, mapbox_style="mapbox://styles/highestroad/cl6to8tmy000n14qv57hgs7pp", mapbox_accesstoken=mbtoken)
fig.update_geos(projection_type="natural earth")
# fig.write_html('map_figure.html', auto_open=True)
# fig.show()
st.plotly_chart(fig, use_container_width=True)
