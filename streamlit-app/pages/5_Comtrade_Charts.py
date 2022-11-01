import streamlit as st
import pandas as pd
import requests
from datetime import date
import plotly.express as px
import numpy as np


color_dict = {
            "(?)":"#F1EEE7",
            "Animals; live":"#807E5B",
            "Meat and edible meat offal":"#C9938B",
            "Dairy produce; birds' eggs; natural honey; edible products of animal origin, not elsewhere specified or included":"#99B7CF",
            "Animal originated products; not elsewhere specified or included":"#7D7E7D",
            "Vegetables and certain roots and tubers; edible":"#57633C",
            "Fruits and nuts; edible":"#98A552",
            "Cereals":"#B99A7A",
            "Coffee, tea, mate and spices":"#5F4737",
            "Fruit and nuts, edible; peel of citrus fruit or melons":"#C66562",
            "Products of the milling industry; malt, starches, inulin, wheat gluten":"#8D8D8E",
            "Oil seeds and oleaginous fruits; miscellaneous grains, seeds and fruit, industrial or medicinal plants; straw and fodder":"#F3E18F",
            "Lac; gums, resins and other vegetable saps and extracts":"#B5A6C8",
            "Animal or vegetable fats and oils and their cleavage products; prepared animal fats; animal or vegetable waxes":"#EAAC55",
            "Sugars and sugar confectionery":"#EBE5D9",
            "Preparations of cereals, flour, starch or milk; pastrycooks' products":"#662C69",
            "Fish and crustaceans, molluscs and other aquatic invertebrates":"#A3AAA5",
            "Meat, fish or crustaceans, molluscs or other aquatic invertebrates; preparations thereof":"#3B768C",
            "Preparations of vegetables, fruit, nuts or other parts of plants":"#E95F85",
            "Import": "#3C787E",
            "Export": "#241623"
            }

def get_comtrade_data(endpoint_url):
     request = requests.get(url=endpoint_url)
     length = len(request.json()["dataset"])
     if length > 1998:
           print ("Data may be truncated in graphs due to API limit")
     return (pd.json_normalize(request.json()["dataset"]))

def make_treegraph (dataframe, Year, Type):
     fig = px.treemap(dataframe, path=[px.Constant("all"), "cmdDescE", 'ptTitle'], values='TradeValue', color='cmdDescE', color_discrete_map=color_dict)
     fig.update_layout(margin = dict(t=50, l=0, r=0, b=0))
     fig.update_layout(title_text=f'{Type} by Commodity and Partner in {Year}')
     # remove outline color
     fig.update_traces(marker_line_color='rgb(0,0,0)', marker_line_width=.1)
     return(fig)
def make_yoygraph (dataframe, Type):
    fig = px.bar(dataframe, x="periodDesc", y="TradeValue", color="cmdDescE", color_discrete_map=color_dict, title=f'Year Over Year {Type}', labels={"period": "Year", "TradeValue": "Imports (USD)"})
    fig.update_layout(showlegend=False)
    fig.update_traces(marker_line_color='white', marker_line_width=0.0)
    fig.update_layout(margin = dict(t=50, l=0, r=5, b=0))
    return(fig)
def make_sunburst_chart (df1, df2):
    # join df1 and df2
    total_df = pd.concat([df1, df2])
    fig = px.sunburst(total_df, path=['rgDesc', 'cmdDescE'], values='TradeValue', color='cmdDescE', color_discrete_map=color_dict, title="Imports and Exports by Commodity")
    fig.update_traces(marker_line_color='#b8baba', marker_line_width=0.2)
    fig.update_layout(margin = dict(t=50, l=0, r=0, b=0))
    # fig.update_traces(color_discrete_map=color_dict, title='Total Imports and Exports')
    return(fig)

def commodity_charts(country_code):
    year = "2021"
    multiyear_string = "2021%2C2020%2C2019%2C2018%2C2017"
    # this is a string of all the two digit commodity codes that I consider to be food
    food_code_string = "01%2C02%2C03%2C04%2C05%2C07%2C08%2C09%2C10%2C11%2C12%2C13%2C15%2C16%2C17%2C19%2C20"
    import_url = f"http://comtrade.un.org/api/get?max=10000&type=C&freq=A&px=HS&ps={year}&r={country_code}&p=all&rg=1&cc={food_code_string}"
    export_url = f"http://comtrade.un.org/api/get?max=10000&type=C&freq=A&px=HS&ps={year}&r={country_code}&p=all&rg=2&cc={food_code_string}"
    yoy_import_url = f"http://comtrade.un.org/api/get?max=10000&type=C&freq=A&px=HS&ps={multiyear_string}&r={country_code}&p=0&rg=1&cc={food_code_string}"
    yoy_export_url = f"http://comtrade.un.org/api/get?max=10000&type=C&freq=A&px=HS&ps={multiyear_string}&r={country_code}&p=0&rg=2&cc={food_code_string}"
    import_df = get_comtrade_data(import_url)
    export_df = get_comtrade_data(export_url)
    yoy_import_df = get_comtrade_data(yoy_import_url)
    yoy_export_df = get_comtrade_data(yoy_export_url)
    # print size of import df


    print ("Import URL: ", import_url)
    print (f"Import df size is {import_df.shape}")
    print ("Export URL: ", export_url)
    print (f"Export df size is {export_df.shape}")
    print ("YOY Import URL: ", yoy_import_url)
    print (f"YOY Import df size is {yoy_import_df.shape}")
    print ("YOY Export URL: ", yoy_export_url)
    print (f"Import df size is {export_df.shape}")

    if import_df.shape[0] > 1:
        import_df = import_df[import_df['ptTitle'].str.match('World') == False]
        import_treegraph = make_treegraph(import_df, year, "Imports")
    else:
        import_treegraph = False
    if export_df.shape[0] > 1:
        export_df = export_df[export_df['ptTitle'].str.match('World') == False]
        export_treegraph = make_treegraph(export_df, year, "Exports")
    else:
        export_treegraph = False
    if yoy_import_df.shape[0] > 1:
        yoy_import_df = yoy_import_df.sort_values(by=['period'])
        yoy_import_graph = make_yoygraph(yoy_import_df, "Imports")
    else:
        yoy_import_graph = False
    if yoy_export_df.shape[0] > 1:
        yoy_export_df = yoy_import_df.sort_values(by=['period'])
        yoy_export_graph = make_yoygraph(yoy_export_df, "Exports")
    else:
        yoy_export_graph = False
    if import_df.shape[0] > 1 and export_df.shape[0] > 1:
        total_sunburstchart = make_sunburst_chart (import_df, export_df)
    else:
        total_sunburstchart = False
    return [import_treegraph, yoy_import_graph, export_treegraph, yoy_export_graph, total_sunburstchart]
    
page_title = st.sidebar.empty()
page_title.header("Comtrade Data Overviews")
st.title("Comtrade Data Overviews")

# Endpoints
country_url = "https://comtrade.un.org/Data/cache/reporterAreas.json"

country_request = requests.get(url=country_url)
country_request.encoding='utf-8-sig'
country_df = pd.json_normalize(country_request.json()["results"])
# st.write(country_df)

# remove row with text matching all from country_df
# country_df = country_df[country_df['text'].str.match('All') == False]

region = st.selectbox(
     'Region of Interest',
     (country_df["text"]),)

if st.button('Make Charts'):
    country_code = country_df.loc[country_df['text'] == region, 'id'].item()
    if region == "World" or region == "All":
        st.write(f"{region} is not a valid country")
    else:
        charts = commodity_charts(country_code)
        if charts[4] != False:
            st.plotly_chart(charts[4], use_container_width=True)
        else:
            st.write(f"No data for total imports and exports in 2021 in {region}")
        if charts[0] != False:
            st.plotly_chart(charts[0], use_container_width=True)
        else:
            st.write(f"No data for 2021 imports in {region}")
        if charts[1] != False:
            st.plotly_chart(charts[1], use_container_width=True)
        else:
            st.write(f"No data for year over year imports in {region}")
        if charts[2] != False:
            st.plotly_chart(charts[2], use_container_width=True)
        else:
            st.write(f"No data for exports in {region}")
        if charts[3] != False:
            st.plotly_chart(charts[3], use_container_width=True)
        else:
            st.write(f"No data for year over year exports in {region}")