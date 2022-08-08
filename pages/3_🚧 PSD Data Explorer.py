import cmath
from jupyter_client import run_kernel
import numpy as np
import pandas as pd
import streamlit as st
import requests
from datetime import date

def get_usda_data(endpoint_url):
    # USDA API Key
    key = {"API_KEY": "aefd68b9-cfdc-4c9e-a800-b457ff5adade"}
    request = requests.get(url=endpoint_url, headers=key)
    # convert response to pandas dataframe
    if int(request.headers['Content-Length']) > 2:
    #   return (pd.read_json(request.text))
      return (request.text)
    else:
        print ("Nothing Found")
        return (False)

st.set_page_config(
	layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
	page_title="PSD Data Explorer",  # String or None. Strings get appended with "• Streamlit". 
	page_icon="./assets/img/earthrise_logo.png",  # String, anything supported by st.image, or None.
)
page_t = st.sidebar.empty()
page_t.header("PSD Data Explorer")

st.title("🚧 Under Construction 🚧")
st.header("Production, Supply & Distribution (PSD) Data Explorer")
st.markdown("PSD Online is the public repository for USDA’s Official Production, Supply and Distribution forecast data, reports and circulars for key agricultural commodities. FAS's PSD Online data are reviewed and updated monthly by an interagency committee chaired by USDA's World Agricultural Outlook Board (WAOB),and consisting of: the Foreign Agricultural Service (FAS), the Economic Research Service (ERS),the Farm Service Agency (FSA), and the Agricultural Marketing Service (AMS). The international portion of the data is updated with input from agricultural attachés stationed at U.S. embassies around the world, FAS commodity analysts, and country and commodity analysts with ERS. The U.S. domestic component is updated with input from analysts in FAS, ERS, the National Agricultural Statistical Service, and FSA.")

# More info on endpoints here: https://apps.fas.usda.gov/opendataweb/home
# Returns a set of records with Forecast number for a given Commodity Code (Ex, 0440000 for Corn) and a given Market Year (Ex, 2017) for the world. Data from all applicable countries are aggregated together for reporting it at the World Level.
aggregate_forecast_url = "https://apps.fas.usda.gov/OpenData/api/psd/commodity/{commodity}/world/year/{year}"
# Returns a set of records with Forecast number for a given Commodity Code (Ex, 0440000 for Corn) and a given Market Year (Ex, 2017) for all applicable countries.
country_forecast_url = "https://apps.fas.usda.gov/OpenData/api/psd/commodity/{commodity}/country/all/year/{year}"
# returns forecast for commodity in specific country
single_country_forecast_url = "https://apps.fas.usda.gov/OpenData/api/psd/{commodity}/0440000/country/{country}/year/{year}"

release_dates_url = "https://apps.fas.usda.gov/OpenData/api/psd/commodity/{commodity}/dataReleaseDates"
region_url = "https://apps.fas.usda.gov/OpenData/api/psd/regions"
country_url = "https://apps.fas.usda.gov/OpenData/api/psd/countries"
commodities_url = "https://apps.fas.usda.gov/OpenData/api/psd/commodities"
units_url = "https://apps.fas.usda.gov/OpenData/api/psd/unitsOfMeasure"
attributes_url = "https://apps.fas.usda.gov/OpenData/api/psd/commodityAttributes"

#API Calls - only uncomment the ones needed as it slows app down 
# country_list = pd.read_json(get_usda_data(country_url))
# region_list = pd.read_json(get_usda_data(region_url))
commodities_list = pd.read_json(get_usda_data(commodities_url))
# units_list = pd.read_json(get_usda_data(units_url))
# attributes_list = pd.read_json(get_usda_data(attributes_url))
year_list = [item for item in range(1990, date.today().year+1)]
st.write(commodities_list)
# define columns here
# col1, col2 = st.columns(2)
comparison_choice = st.radio("Choose what you would like to compare", ["Commodity by Country", "World Aggregate Commodity by Year", "Commodity in a Country Year to Year"])

if comparison_choice == "World Aggregate Commodity by Year":
    com_select = st.selectbox("Pick one", commodities_list["commodityName"])
    year_select = st.multiselect("Pick as many as you would like", year_list)
    com_code = str(commodities_list.loc[(commodities_list['commodityName'].str.contains(com_select, case=False)), 'commodityCode'].iloc[0])
    print(com_code)
    for y in year_select:
        print(aggregate_forecast_url.format(commodity=com_code, year=y))
        # url = aggregate_forecast_url.format(commodity=com_code, year=y)
        # pd_list = pd.read_json(get_usda_data(url))
        pd_list = pd.read_json(get_usda_data("https://apps.fas.usda.gov/OpenData/api/psd/commodity/0440000/world/year/2010"))
        st.write(pd_list)
    

    st.write(com_code)

# App is currently erroring out becuase the pandas dictionary is shaving off leading 0's first priority to fix this. 