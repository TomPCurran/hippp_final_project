# Introduction to Programming For Public Policy Final Project
### Abby Eskenazi, Charlie Crowther, Tom Curran

We will merge the condom distribution site dataset with all of the STI case datasets. We will merge them based on community area. Currently, the condom distribution site dataset does not include community areas, but it does include addresses. To manage this issue, we will create a map including community areas, census tracts, neighborhoods, physical location of condom distribution centers, and STI rates to visualize the relationship between distance from a condom distribution site and STI rate. We will also run regressions on the relationship between distance from a condom distribution site and rates of chlamydia and gonorrhea by gender. We will push all this information to a website to display it for the final project. We want the user to be able to manipulate the data in a meaningful way, such as changing the geographic groupings (neighborhoods, etc.), STI type, and gender.

## Project Summary

### Description:

### Project Goals:

1) Createa an exaploratory dashboard for users to understand the data. Tool will include interactive data visualazations as well as a map of the community area.

2) Explore the impact that Condom Distribution sites have on the Incidence Rates of Chlamydia and Gonorrhea for males and females in Chicago Community Areas.


## Data
  To accomplish project goals, we used the Chicago Data Portal and downloaded five primary data sets. The .csv files were downloaded from the portal and stored in the folder `data_sources`. The `data_sources` folder contains data for the analysis as well as the cleaned and r estructured data required for the web application. 
  
### Sources:

(description of the data) 

### Repo Structure

 - the main folder in the repository contains several notebooks used to conduct the analysis:
    - `Merge and plots Female Chlamydia.ipynb`: analysis conducted for reported cases and incidence of chlamydia for females in Chicago community areas.
    - `Merge and plots Female Gonorrhea.ipynb`: analysis conducted for reported cases and incidence of gonorrhea for females in Chicago community areas.
    - `Merge and plots Male Chlamydia.ipynb`: analysis conducted for reported cases and incidence of chlamydia for males in Chicago community areas.
    - `Merge and plots Male Chlamydia.ipynb`: analysis conducted for reported cases and incidence of gonorrhea for males in Chicago community areas.
    -`STI Infection Rates Map.ipynb`: notebook for creating the reported cases map for all STIs in chicago community area
    -`Incidence Map.ipynb`: notebook for creating the incidence map as seen on the dashboard tool
    - `app.py`: contains the web application that is deployed on heroku
    - `reported_cases_map.html`: map produced from `STI infection Rates Map.ipynb`
    - `incidence map.html`: map produced from `Incidence Map.ipynb`
    - `data-sources`: folder with all relevant data needed for web application development and analysis
    - `graphs`: contains the .png versions of the graphs generated during the analysis. It does not contain the interactive plotly maps from the web app. 
 

## Investigation

### Exploratory Tool:
['Chicago STIs'](https://hippp-final-project-fall17.herokuapp.com/)

We created a tool that allows user to conduct exploratory data analysis using the data sets collected from the Chicago data portal. The tool consists of several parts:

1) Number of Reported Cases by Community Area
2) Incidence of STI by Community Area
3) Trends in Reported Cases from 2000 - 2014
4) Trends in Incidence of STI from 2000 - 2014
5) Choropleth Maps 
  - Reported Cases Map
  - Incidence Map
  
 6) Number of Condom Distribution Centers by Community Area


### Analysis and Model:

![Incidence Rate of Famle Chlamydia and Number of Condom Distribution Centers 2013](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/graph11.png?raw=true)

![Incidence Rate of Famle Chlamydia and Number of Condom Distribution Centers 2014](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/graph12.png?raw=true)

###place holder for Female Gonorrhea 2013

![Incidence Rate of Female Gonorrhea and Number of Condom Distribution Centers 2014](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/graph16.png?raw=true)

![Incidence Rate of Male Gonorrhea and Number of Condom Distribution Centers 2013](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/graph19.png?raw=true)

![Incidence Rate of Male Gonorrhea and Number of Condom Distribution Centers 2014](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/graph20.png?raw=true)

![Incidence Rate of Male Chlamydia and Number of Condom Distribution Centers 2013](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/graph23.png?raw=true)

![Incidence Rate of Male Chlamydia and Number of Condom Distribution Centers 2014](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/graph24.png?raw=true)

## Conclusion

