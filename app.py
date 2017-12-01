import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import numpy as np


##### Import and Clean Data Frame #####

# STI Rates:
sti = pd.read_csv("data_sources/sti_df.csv")
sti = sti.fillna(0)
sti = sti.replace('<5', 0)
sti['Reported Cases'] = sti['Reported Cases'].astype(int)

#Condom Distribution Centers:

centers = pd.read_csv("data_sources/centers_clean.csv")
num_centers = pd.DataFrame(centers['Community Areas'].value_counts())

#Incidence Reports DataFrame

incidence = pd.read_csv("data_sources/incidences_sti.csv")

### Import Reported Cases Map ###

reported_cases_map = open('reported_cases_map.html','r').read()

### Import Incidence Map ###
incidence_map = open('incidence_map.html','r').read()


##### Define App #####
app = dash.Dash(__name__)
server = app.server

##### Import CSS #############
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/dZVMbK.css"})

container_style = {'border': 'thin lightgrey solid'}

##### Begin Layout #####
app.layout = html.Div([

    html.H1("Reported STIs in Chicago Community Areas (2001 - 2014)"),

    html.Hr(),

    #################___Gender Drop Down___###################
    dcc.Dropdown(
        id = 'gender',
        value = 'ALL',
        options = [
            {'label': 'All', 'value': 'ALL'},
            {'label': 'Male', 'value': 'MALE'},
            {'label': 'Female', 'value': 'FEMALE'},
        ],
    ),
    #################___STI Type Drop Down___#############
    dcc.Dropdown(
        id = 'sti_type',
        value = 'ALL',
        options = [
            {'label': 'All', 'value': 'ALL'},
            {'label': 'Gonhorrea', 'value': 'GON'},
            {'label': 'Chlamydia', 'value': 'CHL'}
        ],
    ),

    #################___Select Year___###################
    dcc.Dropdown(
        id = 'year',
        value = 2014,
        options = [{'label': i, 'value': i} for i in
            sti.Year.unique()
        ]
    ),

    html.H4(id ='text', children = ''),

    #################__BAR CHART OF COMMUNITY AREAS__##########################
    dcc.Graph(id='bar'),

    html.Hr(),

    html.H4(id ='incidence_bar_title', children = ''),
    #################__BAR CHART OF COMMUNITY AREAS__##########################
    dcc.Graph(id='incidence_bar'),

    #################__Line Chart 2000 - 2014__##########################

    html.H4(id = 'incidence_line_title', children = ''),

    dcc.Graph(id = 'incidence_line'),

    html.Hr(),

    ################__Line Chart 2000 - 2014__##########################

    html.H4(id = 'lc_title', children = ''),

    dcc.Graph(id = 'line'),

    html.Hr(),

    #################__Map of Reported Cases & Distribution Centers and Bar Chart__##########################
    html.H4("Condom Distribution Centers in Chicago Community Areas"),

    html.Div(
            className='row',
            children=[
                html.Div(
                    className='six columns',
                    #style=container_style,
                    children= html.Div([
                        html.H4("Reported Cases of STI in Community Areas"),
                        html.Iframe(srcDoc = reported_cases_map, width = 800, height = 800)
                    ])),
                html.Div(
                    className = 'six columns',
                    children = html.Div([
                        html.H4("Incidence Rates and Condom Distribution Centers"),
                        html.Iframe(srcDoc = incidence_map, width = 800, height = 800)
                        ])
                    )
            ]
        ),
        #################__Map of Incidences & Distribution Centers and Bar Chart__##########################
    html.H4("Number of Condom Distribution Centers"),


    html.Div(
        dcc.Graph(
            id = "condom_dist_bar",
            figure = {
                'data':[{
                    'y':num_centers['Community Areas'],
                    'x':num_centers.index,
                    'type':'bar'
                }]
            }
        )
    ),
])


#################___Title for Bar Chart____##########################
@app.callback(
    dash.dependencies.Output('text', 'children'),
    [dash.dependencies.Input('year', 'value'),
    dash.dependencies.Input('gender', 'value'),
    dash.dependencies.Input('sti_type', 'value')])

def update_text(year, gender, sti_type):

    gender = gender.lower()
    if sti_type == "CHL":
        sti_type = 'Chlamydia'
    elif sti_type == 'GON':
        sty_type = 'Gonohorrea'

    if (gender == 'all') & (sti_type == 'all'):
        return 'Total Reported Cases for {} in Chicago Community Areas'.format(year)
    elif (gender != 'all') & (sti_type != 'all'):
        return 'Reported Cases of {} for {}s in {} in Chicago Community Areas'.format(sti_type, gender, year)
    elif (gender == 'all' )& (sti_type != 'all'):
        return 'Total Reported Cases of {} in {}'.format(sti_type, year)
    elif (gender != 'all') & (sti_type == 'all'):
        return 'Total Reported STI Cases for {} in {}'.format(gender, year)



#################___Reported Cases Bar Chart____##########################

@app.callback(
    dash.dependencies.Output('bar', 'figure'),
    [dash.dependencies.Input('year', 'value'),
    dash.dependencies.Input('gender', 'value'),
    dash.dependencies.Input('sti_type', 'value')])


def update_figure(year, gender, sti_type):

    if (gender == 'ALL') & (sti_type == 'ALL'):
        df = sti.groupby(['Community Area Name', 'Year'])['Reported Cases'].sum().reset_index()
        df = df[df['Year'] == year]
    elif (gender != 'ALL') & (sti_type == 'ALL'):
        df = sti.groupby(['Community Area Name', 'Year', 'Gender'])['Reported Cases'].sum().reset_index()
        df = df[(df['Year'] == year) & (df['Gender'] == gender)]
    elif (gender == 'ALL') & (sti_type != 'ALL'):
        df = sti.groupby(['Community Area Name', 'Year', 'STI Name'])['Reported Cases'].sum().reset_index()
        df = df[(df['Year'] == year) & (df['STI Name'] == sti_type)]
    elif (gender != 'ALL') & (sti_type != 'ALL'):
        df = sti[(sti['Year'] == year) & (sti['Gender'] == gender) & (sti['STI Name'] == sti_type)]

    return {
        'data': [{
            'y': df['Reported Cases'],
            'x': df['Community Area Name'],
            'type': 'bar'
        }],
        'layout': {
            'title': 'Reported Cases by Chicago Commmunity Area'
        }
    }

#################___incidence_bar_title____##########################
@app.callback(
    dash.dependencies.Output('incidence_bar_title', 'children'),
    [dash.dependencies.Input('year', 'value'),
    dash.dependencies.Input('gender', 'value'),
    dash.dependencies.Input('sti_type', 'value')])

def update_text(year, gender, sti_type):

    gender = gender.lower()
    if sti_type == "CHL":
        sti_type = 'Chlamydia'
    elif sti_type == 'GON':
        sty_type = 'Gonohorrea'

    if (gender == 'all') & (sti_type == 'all'):
        return 'Incidence for {} in Chicago Community Areas'.format(year)
    elif (gender != 'all') & (sti_type != 'all'):
        return 'Incidence of {} for {}s in {} in Chicago Community Areas'.format(sti_type, gender, year)
    elif (gender == 'all' )& (sti_type != 'all'):
        return 'Incidence of {} in {}'.format(sti_type, year)
    elif (gender != 'all') & (sti_type == 'all'):
        return 'Incidence for {} in {}'.format(gender, year)

#################Incidence Bar Chart____##########################
@app.callback(
    dash.dependencies.Output('incidence_bar', 'figure'),
    [dash.dependencies.Input('year', 'value'),
    dash.dependencies.Input('gender', 'value'),
    dash.dependencies.Input('sti_type', 'value')])


def update_incidence_bar(year, gender, sti_type):

    if (gender == 'ALL') & (sti_type == 'ALL'):
        df_inc = incidence.groupby(['Community Area Name', 'Year'])['Incidences'].sum().reset_index()
        df_inc = df_inc[df_inc['Year'] == year]
    elif (gender != 'ALL') & (sti_type == 'ALL'):
        df_inc = incidence.groupby(['Community Area Name', 'Year', 'Gender'])['Incidences'].sum().reset_index()
        df_inc = df_inc[(df_inc['Year'] == year) & (df_inc['Gender'] == gender)]
    elif (gender == 'ALL') & (sti_type != 'ALL'):
        df_inc = incidence.groupby(['Community Area Name', 'Year', 'STI Name'])['Incidences'].sum().reset_index()
        df_inc = df_inc[(df_inc['Year'] == year) & (df_inc['STI Name'] == sti_type)]
    elif (gender != 'ALL') & (sti_type != 'ALL'):
        df_inc = incidence[(incidence['Year'] == year) & (incidence['Gender'] == gender) & (incidence['STI Name'] == sti_type)]

    return {
        'data': [{
            'y': df_inc['Incidences'],
            'x': df_inc['Community Area Name'],
            'type': 'bar'
        }],
        'layout': {
            'title': 'Incidence (Per 100,000 People) by Chicago Commmunity Area'
        }
    }

#################___Title for Line Chart____##########################
@app.callback(
    dash.dependencies.Output('lc_title', 'children'),
    [dash.dependencies.Input('gender', 'value'),
    dash.dependencies.Input('sti_type', 'value')])

def update_text(gender, sti_type):

    gender = gender.lower()
    if sti_type == "CHL":
        sti_type = 'Chlamydia'
    elif sti_type == 'GON':
        sty_type = 'Gonohorrea'

    if (gender == 'all') & (sti_type == 'all'):
        return 'Total Reported Cases in Chicago Community Areas'
    elif (gender != 'all') & (sti_type != 'all'):
        return 'Reported Cases of {} for {}s in Chicago Community Areas'.format(sti_type, gender)
    elif (gender == 'all' )& (sti_type != 'all'):
        return 'Total Reported Cases of {}'.format(sti_type)
    elif (gender != 'all') & (sti_type == 'all'):
        return 'Total Reported STI Cases for {}'.format(gender,)

#################___ Line Chart__##########################
@app.callback(
    dash.dependencies.Output('line', 'figure'),
    [dash.dependencies.Input('gender', 'value'),
    dash.dependencies.Input('sti_type', 'value')])

def update_linegraph(gender, sti_type):

    #if both options selected are ALL, want to show 4 traces (one for both Genders in each STI)
    if (gender == 'ALL') & (sti_type == 'ALL'):

        #male chl
        m_chl = sti[(sti['Gender'] == 'MALE') & (sti['STI Name'] == 'CHL')]
        m_chl = pd.DataFrame(m_chl.groupby('Year')['Reported Cases'].sum())

        #male GON
        m_gon = sti[(sti['Gender'] == 'MALE') & (sti['STI Name'] == 'GON')]
        m_gon = pd.DataFrame(m_gon.groupby('Year')['Reported Cases'].sum())

        #female CHL
        f_chl = sti[(sti['Gender'] == 'FEMALE') & (sti['STI Name'] == 'CHL')]
        f_chl = pd.DataFrame(f_chl.groupby('Year')['Reported Cases'].sum())

        #female GON
        f_gon = sti[(sti['Gender'] == 'FEMALE') & (sti['STI Name'] == 'GON')]
        f_gon = pd.DataFrame(f_gon.groupby('Year')['Reported Cases'].sum())


        return{
            'data':[
                {
                    'x': m_chl.index,
                    'y':m_chl['Reported Cases'],
                    'name': 'Male Chlamydia'
                },
                {
                    'x': m_gon.index,
                    'y': m_gon['Reported Cases'],
                    'name': 'Male Gonohorrea'
                },
                {
                    'x': f_chl.index,
                    'y': f_chl['Reported Cases'],
                    'name': 'Female Chlamydia'
                },
                {
                    'x': f_gon.index,
                    'y': f_gon['Reported Cases'],
                    'name': 'Female Gonohorrea'
                }
            ],
            'layout':{
                'title': 'Trends in STI Reported Cases'
            }


        }
    elif (gender != 'ALL') & (sti_type != 'ALL'):
        lg_df = sti[(sti['Gender'] == gender) & (sti['STI Name'] == sti_type)]
        lg_df = pd.DataFrame(lg_df.groupby('Year')['Reported Cases'].sum())
        return{
            'data':[{

                'x': lg_df.index,
                'y': lg_df['Reported Cases']
            }],
            'layout':{
                'title': 'Trends in STI Reported Cases'
            }


        }
    elif (gender != 'ALL') & (sti_type == 'ALL'):

        #filter Gender
        df = sti[sti['Gender'] == gender]

        #Total number of Reported Male STI
        chl = df[(df['STI Name'] == 'CHL')]
        chl = pd.DataFrame(chl.groupby('Year')['Reported Cases'].sum())


        gon = df[(df['STI Name'] == 'GON')]
        gon = pd.DataFrame(gon.groupby('Year')['Reported Cases'].sum())

        return{
                'data':[
                    {
                        'x': chl.index,
                        'y':chl['Reported Cases'],
                        'name': 'Chlamydia'
                    },
                    {
                        'x': gon.index,
                        'y': gon['Reported Cases'],
                        'name': 'Gonohorrea'
                    }
                ],
                'layout':{
                    'title': 'Trends in STI Reported Cases'
                }

            }
    elif (gender == 'ALL') & (sti_type != 'ALL'):
        #filter Gender
        df = sti[sti['STI Name'] == sti_type]

        #Total number of Reported Male STI
        male = df[(df['Gender'] == 'MALE')]
        male = pd.DataFrame(male.groupby('Year')['Reported Cases'].sum())

        #fTotale Number of Reported Female STI
        female = df[(df['Gender'] == 'FEMALE')]
        female = pd.DataFrame(female.groupby('Year')['Reported Cases'].sum())

        return{
                'data':[
                    {
                        'x': male.index,
                        'y':male['Reported Cases'],
                        'name': 'Male Reported Cases'
                    },
                    {
                        'x': female.index,
                        'y': female['Reported Cases'],
                        'name': 'Female Reported Cases'
                    }
                ],
                'layout':{
                    'title': 'Trends in STI Reported Cases'
                }

            }
    elif (gender != 'All') & (sti_type =='All'):
        #Total number of Reported Male STI
        chl = sti[(sti['STI Name'] == 'CHL')]
        chl = pd.DataFrame(chl.groupby('Year')['Reported Cases'].sum())

        #fTotale Number of Reported Female STI
        gon = sti[(sti['STI Name'] == 'GON')]
        gon = pd.DataFrame(gon.groupby('Year')['Reported Cases'].sum())

        return{
                'data':[
                    {
                        'x': gon.index,
                        'y':gon['Reported Cases'],
                        'name': 'Reported Cases of Gonohorrea'
                    },
                    {
                        'x': chl.index,
                        'y': chl['Reported Cases'],
                        'name': 'Reported Cases of Chlamydia'
                    }
                ],
                'layout':{
                    'title': 'Trends in STI Reported Cases'
                }

            }
#################___Title for Incidence Line Chart____##########################
@app.callback(
    dash.dependencies.Output('incidence_line_title', 'children'),
    [dash.dependencies.Input('gender', 'value'),
    dash.dependencies.Input('sti_type', 'value')])

def update_incidence_text(gender, sti_type):

    gender = gender.lower()
    if sti_type == "CHL":
        sti_type = 'Chlamydia'
    elif sti_type == 'GON':
        sty_type = 'Gonohorrea'

    if (gender == 'all') & (sti_type == 'all'):
        return 'Total Incidence in Chicago Community Areas'
    elif (gender != 'all') & (sti_type != 'all'):
        return 'Incidence of {} for {}s in Chicago Community Areas'.format(sti_type, gender)
    elif (gender == 'all' )& (sti_type != 'all'):
        return 'Total Incidence of {}'.format(sti_type)
    elif (gender != 'all') & (sti_type == 'all'):
        return 'Total Reported STI Cases for {}'.format(gender,)

#################___ Incidence Line Chart__##########################
@app.callback(
    dash.dependencies.Output('incidence_line', 'figure'),
    [dash.dependencies.Input('gender', 'value'),
    dash.dependencies.Input('sti_type', 'value')])

def update_incidence_linegraph(gender, sti_type):

    #if both options selected are ALL, want to show 4 traces (one for both Genders in each STI)
    if (gender == 'ALL') & (sti_type == 'ALL'):

        #male chl
        m_chl_inc = incidence[(incidence['Gender'] == 'MALE') & (incidence['STI Name'] == 'CHL')]
        m_chl_inc = pd.DataFrame(m_chl_inc.groupby('Year')['Incidences'].sum())

        #male GON
        m_gon_inc = incidence[(incidence['Gender'] == 'MALE') & (incidence['STI Name'] == 'GON')]
        m_gon_inc = pd.DataFrame(m_gon_inc.groupby('Year')['Incidences'].sum())

        #female CHL
        f_chl_inc = incidence[(incidence['Gender'] == 'FEMALE') & (incidence['STI Name'] == 'CHL')]
        f_chl_inc = pd.DataFrame(f_chl_inc.groupby('Year')['Incidences'].sum())

        #female GON
        f_gon_inc = incidence[(incidence['Gender'] == 'FEMALE') & (incidence['STI Name'] == 'GON')]
        f_gon_inc = pd.DataFrame(f_gon_inc.groupby('Year')['Incidences'].sum())


        return{
            'data':[
                {
                    'x': m_chl_inc.index,
                    'y':m_chl_inc['Incidences'],
                    'name': 'Male Chlamydia'
                },
                {
                    'x': m_gon_inc.index,
                    'y': m_gon_inc['Incidences'],
                    'name': 'Male Gonohorrea'
                },
                {
                    'x': f_chl_inc.index,
                    'y': f_chl_inc['Incidences'],
                    'name': 'Female Chlamydia'
                },
                {
                    'x': f_gon_inc.index,
                    'y': f_gon_inc['Incidences'],
                    'name': 'Female Gonohorrea'
                }
            ],
            'layout':{
                'title': 'Trends in STI Incidences'
            }


        }
    elif (gender != 'ALL') & (sti_type != 'ALL'):
        lg_df = incidence[(incidence['Gender'] == gender) & (incidence['STI Name'] == sti_type)]
        lg_df = pd.DataFrame(lg_df.groupby('Year')['Incidences'].sum())
        return{
            'data':[{

                'x': lg_df.index,
                'y': lg_df['Incidences']
            }],
            'layout':{
                'title': 'Trends in STI Incidence'
            }


        }
    elif (gender != 'ALL') & (sti_type == 'ALL'):

        #filter Gender
        df = incidence[incidence['Gender'] == gender]

        #Total number of Reported Male STI
        chl = df[(df['STI Name'] == 'CHL')]
        chl = pd.DataFrame(chl.groupby('Year')['Incidences'].sum())


        gon = df[(df['STI Name'] == 'GON')]
        gon = pd.DataFrame(gon.groupby('Year')['Incidences'].sum())

        return{
                'data':[
                    {
                        'x': chl.index,
                        'y':chl['Incidences'],
                        'name': 'Chlamydia'
                    },
                    {
                        'x': gon.index,
                        'y': gon['Incidences'],
                        'name': 'Gonohorrea'
                    }
                ],
                'layout':{
                    'title': 'Trends in STI Incidence'
                }

            }
    elif (gender == 'ALL') & (sti_type != 'ALL'):
        #filter Gender
        df = incidence[incidence['STI Name'] == sti_type]

        #Total number of Reported Male STI
        male = df[(df['Gender'] == 'MALE')]
        male = pd.DataFrame(male.groupby('Year')['Incidences'].sum())

        #fTotale Number of Reported Female STI
        female = df[(df['Gender'] == 'FEMALE')]
        female = pd.DataFrame(female.groupby('Year')['Incidences'].sum())

        return{
                'data':[
                    {
                        'x': male.index,
                        'y':male['Incidences'],
                        'name': 'Male Incidence'
                    },
                    {
                        'x': female.index,
                        'y': female['Incidences'],
                        'name': 'Female Incidence'
                    }
                ],
                'layout':{
                    'title': 'Trends in STI Incidence'
                }

            }
    elif (gender != 'All') & (sti_type =='All'):
        #Total number of Reported Male STI
        chl = incidence[(incidence['STI Name'] == 'CHL')]
        chl = pd.DataFrame(chl.groupby('Year')['Incidences'].sum())

        #fTotale Number of Reported Female STI
        gon = incidence[(incidence['STI Name'] == 'GON')]
        gon = pd.DataFrame(gon.groupby('Year')['Incidences'].sum())

        return{
                'data':[
                    {
                        'x': gon.index,
                        'y':gon['Incidences'],
                        'name': 'Incidence of Gonohorrea'
                    },
                    {
                        'x': chl.index,
                        'y': chl['Incidences'],
                        'name': 'Incidence of Chlamydia'
                    }
                ],
                'layout':{
                    'title': 'Trends in STI Incidence'
                }

            }

if __name__ == '__main__':
    app.run_server(debug=True)
