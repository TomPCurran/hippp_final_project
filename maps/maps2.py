import pandas as pd
import numpy as np
import string
import json
import ast
import plotly
import pprint
import plotly.plotly as py
import plotly.graph_objs as graph_objs
import folium

plotly.tools.set_credentials_file(username='tcurran4589', api_key='daaMACDepMRaSr3cjH6j')
#import centers data
centers = pd.read_csv("condom_dist_u.csv")
centers = centers[['Venue Type', 'Name', 'Address','State', 'ZIP Code', 'Community Areas']]
centers['City'] = 'Chicago'

#import STI information
male_chl = pd.read_csv("chlamydia_males.csv")
male_chl = male_chl[["Community Area Name",
          "CASES 2001 Male 15-44",
          "CASES 2002 Male 15-44",
          "CASES 2003 Male 15-44",
          "CASES 2004 Male 15-44",
          "CASES 2005 Male 15-44",
          "CASES 2006 Male 15-44",
          "CASES 2007 Male 15-44",
          "CASES 2008 Male 15-44",
          "CASES 2009 Male 15-44",
          "CASES 2010 Male 15-44",
          "CASES 2011 Male 15-44",
          "CASES 2012 MALE 15-44",
          "CASES 2013 Male 15-44",
          "CASES 2014 Male 15-44"
         ]]

male_gon = pd.read_csv("gonorrhea_males.csv")
male_gon = male_gon[["Community Area Name",
                  "Cases 2001 Male 15-44",
                  "Cases 2002 Male 15-44",
                  "Cases 2003 Male 15-44",
                  "Cases 2004 Male 15-44",
                  "Cases 2005 Male 15-44",
                  "Cases 2006 Male 15-44",
                  "Cases 2007 Male 15-44",
                  "Cases 2008 Male 15-44",
                  "Cases 2009 Male 15-44",
                  "Cases 2010 Male 15-44",
                  "Cases 2011 Male 15-44",
                  "Cases 2012 Male 15-44",
                  "Cases 2013 Male 15-44",
                  "Cases 2014 Male 15-44"
         ]]

female_chl = pd.read_csv("chlamydia_females.csv")
female_chl = female_chl[["Community Area Name",
                        "Cases 2000 Female 15-44",
                        "Cases 2001 Female 15-44",
                        "Cases 2002 Female 15-44",
                        "Cases 2003 Female 15-44",
                        "Cases 2004 Female 15-44",
                        "Cases 2005 Female 15-44",
                        "Cases 2006 Female 15-44",
                        "Cases 2007 Female 15-44",
                        "Cases 2008 Female 15-44",
                        "Cases 2009 Female 15-44",
                        "Cases 2010 Female 15-44",
                        "Cases 2011 Female 15-44",
                        "Cases 2012 Female 15-44",
                        "Cases 2013 Female 15-44",
                        "Cases 2014 Female 15-44"]]


female_gon = pd.read_csv("gonorrhea_females.csv")
female_gon = female_gon[["Community Area Name",
                        "Cases 2000 Female 15-44",
                        "Cases 2001 Female 15-44",
                        "Cases 2002 Female 15-44",
                        "Cases 2003 Female 15-44",
                        "Cases 2004 Female 15-44",
                        "Cases 2005 Female 15-44",
                        "Cases 2006 Female 15-44",
                        "Cases 2007 Female 15-44",
                        "Cases 2008 Female 15-44",
                        "Cases 2009 Female 15-44",
                        "Cases 2010 Female 15-44",
                        "Cases 2011 Female 15-44",
                        "Cases 2012 Female 15-44",
                        "Cases 2013 Female 15-44",
                        "Cases 2014 Female 15-44"]]

#merge datasets
chl = male_chl.merge(female_chl, left_on = 'Community Area Name', right_on = 'Community Area Name', how = 'inner')

gon = male_gon.merge(female_gon, left_on = 'Community Area Name', right_on = 'Community Area Name', how = 'inner')

#Converting the data frame to make it longer
#pd.melt(df, id_vars=['column_A', 'column_B', 'column_C'], var_name='Year', value_name='Value')

chl_long = pd.melt(chl,
                id_vars = ['Community Area Name'],
                var_name = "Cases",
                value_name = "Reported Cases")


chl_long['Year'] = chl_long['Cases'].str.extract(r'([0-9]{4})', expand = True)

chl_long['Gender'] = chl_long['Cases'].str.extract(r'(Female|Male)', expand = True)

gon_long = pd.melt(gon,
                id_vars = ['Community Area Name'],
                var_name = "Cases",
                value_name = "Reported Cases")


gon_long['Year'] = gon_long['Cases'].str.extract(r'([0-9]{4})', expand = True)

gon_long['Gender'] = gon_long['Cases'].str.extract(r'(Female|Male)', expand = True)

gon_long['Community Area Name'] = gon_long['Community Area Name'].str.upper()
chl_long['Community Area Name'] = chl_long['Community Area Name'].str.upper()


#mapbox_access_token = pk.eyJ1IjoidGN1cnJhbjQ1ODkiLCJhIjoiY2ltbWRxc3FmMDM1NXRxa3E0Ymp3OGJscSJ9.xRqKXR3MEfr3ZfBcP1yqCg
#community_areas.geojson
with open('community_areas.geojson') as g:
    chi_comm_shape = json.load(g)

#creates properties for STI rates that are dictionaries

names = []

for ca_names in range(0, len(chi_comm_shape['features'])):
    name = chi_comm_shape['features'][ca_names]['properties']['community']
    names.append(name)
    chi_comm_shape['features'][ca_names]['properties']['STI_Rates'] = {"chlamydia":{"male":{},"female":{}},
                                                            "gonorrhea":{"male":{},"female":{}}}

#loop through the gonorrhea dataframe first
for community in range(0, len(chi_comm_shape['features'])):
    for i in range(0, len(gon_long)):
        ca_name = chi_comm_shape['features'][community]['properties']['community']
        year = gon_long['Year'][i]
        rate = gon_long['Reported Cases'][i]
        if gon_long['Community Area Name'][i] == ca_name:
            if gon_long['Gender'][i] == 'Female':
                chi_comm_shape['features'][community]['properties']['STI_Rates']['gonorrhea']['female'][year]=rate
            else:
                chi_comm_shape['features'][community]['properties']['STI_Rates']['gonorrhea']['male'][year]=rate


for community in range(0, len(chi_comm_shape['features'])):
    for j in range(0, len(chl_long)):
        ca_name = chi_comm_shape['features'][community]['properties']['community']
        year = chl_long['Year'][j]
        rate = chl_long['Reported Cases'][j]
        if chl_long['Community Area Name'][j] == ca_name:
            if chl_long['Gender'][j] == 'Female':
                chi_comm_shape['features'][community]['properties']['STI_Rates']['chlamydia']['female'][year]=rate
            else:
                chi_comm_shape['features'][community]['properties']['STI_Rates']['chlamydia']['male'][year]=rate

mapbox_token = "pk.eyJ1IjoidGN1cnJhbjQ1ODkiLCJhIjoiY2ltbWRxc3FmMDM1NXRxa3E0Ymp3OGJscSJ9.xRqKXR3MEfr3ZfBcP1yqCg"

m = folium.Map(location = [41.881832, -87.623177],
              tiles = 'Mapbox Bright',
              zoom_start = 9)

folium.GeoJson( chi_comm_shape,
               name = 'Chicago Community Area').add_to(m)

folium.LayerControl().add_to(m)

chl_long_2014 = chl_long[chl_long['Year'] == '2014']

chl_2014 = chl_long_2014.groupby(['Community Area Name']).sum()

chl_2014 = chl_2014.reset_index()

m = folium.Map(location = [41.881832, -87.623177],
              tiles = 'Mapbox Bright',
              zoom_start = 9)

folium.Marker([41.881832, -87.623177], popup='<i>Chicago</i>').add_to(m)

m.choropleth(

    geo_data = chi_comm_shape,
    name = 'Community area',
    data = chl_2014,
    columns=['Community Area Name','Reported Cases'],
    fill_color = 'YlGn'

)

folium.LayerControl().add_to(m)

m.save('map_test.html')
