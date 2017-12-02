# Introduction to Programming For Public Policy Final Project
### Abby Eskenazi, Charlie Crowther, Tom Curran

## Project Proposal:
We will merge the condom distribution site dataset with all of the STI case datasets. We will merge them based on community area. Currently, the condom distribution site dataset does not include community areas, but it does include addresses. To manage this issue, we will create a map including community areas, census tracts, neighborhoods, physical location of condom distribution centers, and STI rates to visualize the relationship between distance from a condom distribution site and STI rate. We will also run regressions on the relationship between distance from a condom distribution site and rates of chlamydia and gonorrhea by gender. We will push all this information to a website to display it for the final project. We want the user to be able to manipulate the data in a meaningful way, such as changing the geographic groupings (neighborhoods, etc.), STI type, and gender.

## Project Summary

### Motivation: 
One of the most effective ways to prevent STIs is using latex condoms. According to a 2006 study by Warner, Stone, et.al, condom use is associated with a lower risk of chlamydia and gonorrhea. However, there are still sexually active people who do not use them, perhaps due to a lack of education, availability, and/or prohibitive costs. To examine whether distance and cost act as barriers, we look at whether the number of free condom distribution sites per community area is related to gonorrhea and chlamydia incidence rates for men and women in the years 2013 and 2014.

### Project Goals:

1) Createa an exaploratory dashboard for users to understand the data. Tool will include interactive data visualazations as well as a map of the community area.

2) Explore the impact that Condom Distribution sites have on the Incidence Rates of Chlamydia and Gonorrhea for males and females in Chicago Community Areas.

## Data
  To accomplish project goals, we used the Chicago Data Portal and downloaded five primary data sets. The .csv files were downloaded from the portal and stored in the folder `data_sources`. The `data_sources` folder contains data for the analysis as well as the cleaned and r estructured data required for the web application. 
  
### Sources:
Condom Distribution Sites: This dataset lists several locations across the city where the Chicago Department of Public Health distributes condoms. The data was last updated in November of 2013, which influenced the data we used from the other datasets in our analysis.

Public Health Statistics- Chlamydiacases among males aged 15-44 in Chicago, by year, 2000-2014. This dataset lists the annual number of newly reported, laboratory-confirmed cases of chlamydia among males aged 15 to 44 years as well as annual chlamydia incidence rate (cases per 100,000 males aged 15 to 44 years) by Chicago community area, for years 2000 to 2014. [here](https://data.cityofchicago.org/api/views/35yf-6dy3/files/99f0a9d9-330b-4c1d-abab-6c37302d8e19?download=true&filename=CHLAMYDIA_MALES_AGED_15_44_2000_2014_Dataset_Description.pdf)

Public Health Statistics- Chlamydia cases among females aged 15-44 in Chicago, by year, 2000-2014: This dataset lists the annual number of newly reported, laboratory-confirmed cases of chlamydia among females aged 15 to 44 years old as well as annual chlamydia incidence rate (cases per 100,000 females aged 15 to 44 years) by Chicago community area, for years 2000 to 2014. [here](https://data.cityofchicago.org/api/views/bz6k-73ti/files/4e6db1e1-2014-4a50-9184-997bcd6e969b?download=true&filename=CHLAMYDIA_FEMALES_AGED_15_44_2000_2014_Dataset_Description.pdf)

Public Health statistics- Gonorrhea cases for males aged 15-44 in Chicago, by year, 2000-2014. The annual number of newly reported, laboratory-confirmed cases of gonorrhea among males aged 15 to 44 years as well as annual gonorrhea incidence rate (cases per 100,000 males aged 15-44 years) by Chicago community area, for years 2000 to 2014. [here](https://data.cityofchicago.org/api/views/m5qn-gmjx/files/02497fbf-f6ab-4f94-81d4-92dd1f64ca17?download=true&filename=GONORRHEA_MALES_AGED_15_44_2000_2014_Dataset_Description.pdf)

Public Health Statistics- Gonorrhea cases for females aged 15-44 in Chicago, by year, 2000-2014. The annual number of newly reported, laboratory-confirmed cases of gonorrhea among females aged 15 to 44 years as well as annual gonorrhea incidence rate (cases per 100,000 females aged 15-44 years) by Chicago community area, for years 2000 – 2014. [here](https://data.cityofchicago.org/api/views/cgjw-mn43/files/f8dc78d5-09fb-4ef7-8eee-62fc45763bac?download=true&filename=GONORRHEA_FEMALES_AGED_15_44_2000_2014_Dataset_Description.pdf)

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

**Regression Analysis**
The analysis was performed using python, pandas, seaborn, and statsmodels.

We separately regressed the incidence rate of chlamydia and gonorrhea among men and women in all 77 community areas in Chicago on the number of condom distribution centers in each community area. Although the STI datasets include incidence rates from 2000 to 2014, we only used the data from 2013 and 2014 because the condom distribution center data was updated in 2013. We assume that these condom distribution centers existed as of 2013.

We did not find a significant correlation between STI incidence rate and number of condom distribution centers. This was true in the years 2013 and 2014 for the incidence rates of male gonorrhea, female gonorrhea, male chlamydia and female chlamydia. As shown in the statistical tables, every R-squared measure is less than .1, demonstrating that the number of condom distribution centers explains a minimal amount of the variation in STI incidence rates.

**Outlier Identified**:
The community area of Lakeview is an outlier both in the number of condom distribution centers within its boundary (18) and the low incidence of chlamydia and gonorrhea among men and women in 2013 and 2014. Although Lakeview is clearly differentiated from the group, the pull of the outlier is not strong enough to skew the results into being significant, so we did not choose to remove the outlier as a part of our analysis.

We also recognize that this analysis is not complete because we did not control for other outside factors. To improve the analysis, we could control for race, poverty rate, education level, sex education models, and culture, using OLS and/or fixed effects.

### Plots and Regression Tables:

![Incidence Rate of Famle Chlamydia and Number of Condom Distribution Centers 2013](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/graph11.png?raw=true)

![Regression of Incidence Rate of Female Chlamydia and Condom Distribution Centers 2013](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/Female%20Chlamydia%20stats%202013.png?raw=true)

*** 

![Incidence Rate of Famle Chlamydia and Number of Condom Distribution Centers 2014](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/graph12.png?raw=true)

![Regression of Incidence Rate of Female Chlamydia and Condom Distribution Centers 2013](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/Female%20Chl%202014%20Reg.png?raw=true)

***

![Incidence Rate of Female Gonorrhea and Number of Condom Distribution Centers 2013](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/graph15_2.png?raw=true)

![Regression of Incidence Rate of Female Gonorrhea and Condom Distribution Centers 2013](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/Female%20Gon%202013%20REg.png?raw=true)

***

![Incidence Rate of Female Gonorrhea and Number of Condom Distribution Centers 2014](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/graph16.png?raw=true)

![Regression of Incidence Rate of Female Gonorrhea and Condom Distribution Centers 2014](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/Female%20Gon%202014%20Reg.png?raw=true)

***
![Incidence Rate of Male Gonorrhea and Number of Condom Distribution Centers 2013](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/graph19.png?raw=true)

![Regression of Incidence Rate of Male Chlamydia and Condom Distribution Centers 2013](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/Male%20Gonorrhea%20stats%202013.png?raw=true)

***

![Incidence Rate of Male Gonorrhea and Number of Condom Distribution Centers 2014](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/graph20.png?raw=true)

![Regression of Incidence Rate of Male Gonorrhea and Condom Distribution Centers 2014](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/Male%20Gonorrhea%20stats%202014.png?raw=true)

**

![Incidence Rate of Male Chlamydia and Number of Condom Distribution Centers 2013](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/graph23.png?raw=true)

![Regression of Incidence Rate of Male Chlamydia and Condom Distribution Centers 2013](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/Male%20Chlamydia%20stats%202013.png?raw=true)

***

![Incidence Rate of Male Chlamydia and Number of Condom Distribution Centers 2014](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/graph24.png?raw=true)

![Regression of Incidence Rate of Male Chlamydia and Condom Distribution Centers 2014](https://github.com/TCurran4589/hippp_final_project/blob/master/graphs/Male%20Chlamydia%20stats%202014.png?raw=true)

## Conclusion

Conclusion

We did not find a statistically significant relationship between STI incidence rates and proximity to condom distribution centers for any of the combinations of STIs and gender. The fact that we did not control for other variables is one reason that these results may not have been statistically significant. If we were to continue with this project, we would include a number of additional regressors as discussed prior. The inclusion of these regressors would provide a richer analysis of the relationships explored in this project.


