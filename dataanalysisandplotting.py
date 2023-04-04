import pandas as pd
import matplotlib.pyplot as plt
import os.path
import numpy as np
from os import path
import re
import string 
from string import Formatter
#import plotly.express as px

gdp = pd.read_csv("new_gdp.csv")
pop = pd.read_csv("new_world_population.csv")

pop.set_index('Country/Territory', inplace=True)
gdp.set_index('Country Name', inplace=True)

country_1=["World","Afghanistan","United Arab Emirates","Argentina","Armenia","Australia","Azerbaijan", 'Belgium', 'Bangladesh','Bahrain', 'Brazil']
country_2=["World",'Canada', 'Switzerland', 'Chile', 'China', 'Colombia', 'Cuba', 'Cayman Islands', 'Denmark', 'Spain', 'Finland']
country_3=["World",'France', 'United Kingdom', 'Greece', 'Haiti', 'India', 'Ireland', 'Iraq', 'Iceland', 'Israel', 'Italy']
country_4=["World",'Japan', 'Kazakhstan', 'Kenya', 'Lebanon', 'Libya', 'Sri Lanka', 'Madagascar', 'Mexico', 'Malaysia', 'Nigeria']
country_5=["World",'Netherlands', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Philippines', 'Poland', 'Romania', 'Rwanda', 'Saudi Arabia']
country_6=["World",'Sudan', 'Singapore', 'Sweden', 'Thailand', 'Uganda', 'Ukraine', 'United States', 'Vietnam', 'Zimbabwe']

figure, axis = plt.subplots(3,2)

for country_name in country_1:
#         country_name = input()

    gdp_value = (gdp.loc[country_name, ["1970","1980","1990","2000","2010","2015","2020"]])
    pop_value = (pop.loc[country_name, ["1970 Population","1980 Population","1990 Population","2000 Population","2010 Population","2015 Population","2020 Population"]])

    #print(gdp_value)
    #print(pop_value)
    
    div_value =0
    gdp_capital = []
    result_b = []
    for i in range(0,7):
        div_value = gdp_value[i]/pop_value[i]
        result_b.append(div_value) 
        #print(div_value)
    #print('new')

    data = {
       'year':[1970,1980,1990,2000,2010,2015,2020],
       'gdp_rate': result_b
    }

    # Create dataframe
    df = pd.DataFrame(data)
    #print(df['unemployment_rate'])

    axis[0,0].plot(df['year'], df['gdp_rate'],'', marker='o')
    #plt.subplot(3, 2, 1)
axis[0,0].legend(country_1, loc='upper left', ncol=2, prop={'size': 8})
axis[0,0].set_title('GDP Graph', fontsize=14)
axis[0,0].set_ylabel('GDP/Capital', fontsize=14)



for country_name in country_2:
#         country_name = input()

    gdp_value = (gdp.loc[country_name, ["1970","1980","1990","2000","2010","2015","2020"]])
    pop_value = (pop.loc[country_name, ["1970 Population","1980 Population","1990 Population","2000 Population","2010 Population","2015 Population","2020 Population"]])

    div_value =0
    gdp_capital = []
    result_b = []
    for i in range(0,7):
        div_value = gdp_value[i]/pop_value[i]
        result_b.append(div_value) 

    data = {
       'year':[1970,1980,1990,2000,2010,2015,2020],
       'gdp_rate': result_b
    }

    # Create dataframe
    df = pd.DataFrame(data)
    axis[0,1].plot(df['year'], df['gdp_rate'],'', marker='o')
    #plt.subplot(3, 2, 2)

axis[0,1].legend(country_2, loc='upper left' , ncol=2, prop={'size': 8})
axis[0,1].set_title('GDP Graph', fontsize=14)
axis[0,1].set_ylabel('GDP/Capital', fontsize=14)

for country_name in country_3:
#         country_name = input()

    gdp_value = (gdp.loc[country_name, ["1970","1980","1990","2000","2010","2015","2020"]])
    pop_value = (pop.loc[country_name, ["1970 Population","1980 Population","1990 Population","2000 Population","2010 Population","2015 Population","2020 Population"]])

    div_value =0
    gdp_capital = []
    result_b = []
    for i in range(0,7):
        div_value = gdp_value[i]/pop_value[i]
        result_b.append(div_value) 

    data = {
       'year':[1970,1980,1990,2000,2010,2015,2020],
       'gdp_rate': result_b
    }

    # Create dataframe
    df = pd.DataFrame(data)
    axis[1,0].plot(df['year'], df['gdp_rate'],'', marker='o')
    

axis[1,0].legend(country_3, loc='upper left' , ncol=2, prop={'size': 8})
axis[1,0].set_ylabel('GDP/Capital', fontsize=14)


for country_name in country_4:
#         country_name = input()

    gdp_value = (gdp.loc[country_name, ["1970","1980","1990","2000","2010","2015","2020"]])
    pop_value = (pop.loc[country_name, ["1970 Population","1980 Population","1990 Population","2000 Population","2010 Population","2015 Population","2020 Population"]])

    div_value =0
    gdp_capital = []
    result_b = []
    for i in range(0,7):
        div_value = gdp_value[i]/pop_value[i]
        result_b.append(div_value) 

    data = {
       'year':[1970,1980,1990,2000,2010,2015,2020],
       'gdp_rate': result_b
    }

    # Create dataframe
    df = pd.DataFrame(data)
    axis[1,1].plot(df['year'], df['gdp_rate'],'', marker='o')
    
axis[1,1].legend(country_4, loc='upper left', ncol=2, prop={'size': 8})
axis[1,1].set_ylabel('GDP/Capital', fontsize=14)


for country_name in country_5:
#         country_name = input()

    gdp_value = (gdp.loc[country_name, ["1970","1980","1990","2000","2010","2015","2020"]])
    pop_value = (pop.loc[country_name, ["1970 Population","1980 Population","1990 Population","2000 Population","2010 Population","2015 Population","2020 Population"]])

    div_value =0
    gdp_capital = []
    result_b = []
    for i in range(0,7):
        div_value = gdp_value[i]/pop_value[i]
        result_b.append(div_value) 

    data = {
       'year':[1970,1980,1990,2000,2010,2015,2020],
       'gdp_rate': result_b
    }

    # Create dataframe
    df = pd.DataFrame(data)
    axis[2,0].plot(df['year'], df['gdp_rate'],'', marker='o')
    

axis[2,0].legend(country_5, loc='upper left', ncol=2, prop={'size': 8})
axis[2,0].set_ylabel('GDP/Capital', fontsize=14)
axis[2,0].set_xlabel('Year', fontsize=14)

for country_name in country_6:
#         country_name = input()

    gdp_value = (gdp.loc[country_name, ["1970","1980","1990","2000","2010","2015","2020"]])
    pop_value = (pop.loc[country_name, ["1970 Population","1980 Population","1990 Population","2000 Population","2010 Population","2015 Population","2020 Population"]])

    div_value =0
    gdp_capital = []
    result_b = []
    for i in range(0,7):
        div_value = gdp_value[i]/pop_value[i]
        result_b.append(div_value) 

    data = {
       'year':[1970,1980,1990,2000,2010,2015,2020],
       'gdp_rate': result_b
    }

    # Create dataframe
    df = pd.DataFrame(data)
    axis[2,1].plot(df['year'], df['gdp_rate'],'', marker='o')
    

axis[2,1].legend(country_6, loc='upper left', ncol=2, prop={'size': 8})
axis[2,1].set_ylabel('GDP/Capital', fontsize=14)
axis[2,1].set_xlabel('Year', fontsize=14)
plt.show()

