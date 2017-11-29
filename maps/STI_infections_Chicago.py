
# coding: utf-8

# In[13]:

import geopandas as gpd
import pandas as pd
import folium as f
ca = gpd.read_file("community_areas.geojson")
ca.shape_area = ca.shape_area.astype(float)

m = f.Map(location = [41.881832, -87.623177],
              tiles = 'Mapbox Bright',
              zoom_start = 7)


ft = "Number of Reported Cases of STI"

colormap = f.LinearColormap(("Green", "Yellow","Orange", "Red"),
                                 vmin = ca.shape_area.min(),
                                 vmax = ca.shape_area.max() * 0.5,
                                 caption = "Number of Reported Carese")

colormap.add_to(m)

f.GeoJson(ca,
               style_function = lambda feature: {
                  'fillColor': colormap(feature['properties']["shape_area"]),
                  "color" : "k", "weight" : 0.3, "fillOpacity" : 0.4,
               }).add_to(m)

m.save("test.html")


# In[54]:

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

chl_2014 = chl_long[chl_long['Year']=="2014"]

chl_2014 = chl_2014.groupby(['Community Area Name']).sum()

chl_2014 = chl_2014.reset_index()


# In[55]:

x = ca.merge(chl_2014, left_on = 'community',
            right_on = 'Community Area Name',
            how = 'inner')


# In[60]:

m = f.Map(location = [41.881832, -87.623177],
              tiles = 'Mapbox Bright',
              zoom_start = 11)


ft = "Number of Reported Cases of STI"

colormap = f.LinearColormap(("Green", "Yellow","Orange", "Red"),
                                 vmin = min(x['Reported Cases']),
                                 vmax = max(x['Reported Cases'])*.35,
                                 caption = "Number of Reported Cases")


colormap.add_to(m)

f.GeoJson(x,
               style_function = lambda feature: {
                  'fillColor': colormap(feature['properties']["Reported Cases"]),
                  "color" : "k", "weight" : 0.3, "fillOpacity" : 0.4,
               }).add_to(m)

centers = pd.read_csv("centers2.csv")

for l in range(0, len(centers)):

    lat = float(centers["Latitude"][l])
    lng = float(centers["Longitude"][l])
    center_name = centers['Name'][l]

    #print(l)
    f.Marker([lat, lng], popup = center_name).add_to(m)


f.LayerControl().add_to(m)

def inline_map(m, width=650, height=500):
    """Takes a folium instance and embed HTML."""
    m._build_map()
    srcdoc = m.HTML.replace('"', '&quot;')
    embed = HTML('<iframe srcdoc="{}" '
                 'style="width: {}px; height: {}px; '
                 'border: none"></iframe>'.format(srcdoc, width, height))
    return embed

m.save("sti_map.html")
inline_map(m)
