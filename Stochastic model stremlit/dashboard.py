# -*- coding: utf-8 -*-
#"""
#Spyder Editor

#This is a temporary script file.
#""

# Import related library
import pandas as pd
import result
import streamlit as st
import plotly_express as pe
import pandas




# Title
st.title("Stochastic Model Predictions")

# Subheader
st.subheader('This dashboard will display result of prediction made by stochastic model.')

# pulling result from dataframe
data = pd.DataFrame(result.res_dct["data"])

# Add widget
st.sidebar.title("Filters:")
option = st.sidebar.selectbox("Stocks:", ("ALL",) + tuple(list(data.symbol)))

#st.header("Filter")

if option == "ALL":
    st.subheader("All Predictions :")
    st.write(data)

elif option == "{}".format(option):
    st.subheader("{}".format(option))
    st.write(data[data.symbol == option])
    
    
# Title
#st.title("Charts")

###############################

# Add widget
#st.sidebar.title("Filters:")
result = st.sidebar.selectbox("Result:", ('','Winning Rate','Precision'))



df_wr = pandas.read_csv('Winning rate function.csv')
df_pre = pandas.read_csv('Precision function.csv')
df_wr = df_wr.rename(columns={'Winning_Rate': 'Value of winning rate'})
df_pre = df_pre.rename(columns={'Result_precision': 'Value of precision'})

if result== 'Precision':
    st.subheader('Total Precision :')
    df_sort=df_pre.sort_values(by="Year")
    df_resetindex=df_sort.reset_index(drop=True)
    Graph_precision=pe.bar(data_frame=df_resetindex,x='Sector',y='Value of precision',color='Year',title='Precision')
    #st.write(Graph_precision.show())
    st.plotly_chart(Graph_precision)

if result== 'Winning Rate':
    st.subheader('Total Winning Rate :')
    df_sort=df_wr.sort_values(by="Year")
    df_resetindex=df_sort.reset_index(drop=True)
    Graph_wr=pe.bar(data_frame=df_resetindex,x='Sector',y='Value of winning rate',color='Year',title='Winning Rate')    
    st.plotly_chart(Graph_wr)

# Add widget
year = st.sidebar.selectbox("Year:", ('','2016','2017','2018','2019','2020'))


#graph sort by year winning rate
def graph_year_wr(year_):
    year=year_
    df_all=df_wr[df_wr.Year==year].sort_values(by="Value of winning rate")
    df_graph=pe.bar(data_frame=df_all,x='Sector',y='Value of winning rate',title='Winning Rate {}'.format(year))
    df_resetindex=df_all.set_index('Year',inplace=False)
    #print(df_resetindex)
    return df_graph

#graph sort by year precision
def graph_year_pre(year_):
    year=year_
    df_all=df_pre[df_pre.Year==year].sort_values(by="Value of precision")
    df_graph=pe.bar(data_frame=df_all,x='Sector',y='Value of precision',title='Precision {}'.format(year))
    df_resetindex=df_all.set_index('Year',inplace=False)
    #print(df_resetindex)
    return df_graph

st.subheader('Yearly Performance :')
if year =='2016':
    st.plotly_chart(graph_year_wr(2016))
    st.plotly_chart(graph_year_pre(2016))

if year =='2017':
    st.plotly_chart(graph_year_wr(2017))
    st.plotly_chart(graph_year_pre(2017))

if year =='2018':
    st.plotly_chart(graph_year_wr(2018))
    st.plotly_chart(graph_year_pre(2018))

if year =='2019':
    st.plotly_chart(graph_year_wr(2019))
    st.plotly_chart(graph_year_pre(2019))

if year =='2020':
    st.plotly_chart(graph_year_wr(2020))
    st.plotly_chart(graph_year_pre(2020))

# Add widget
# Graph sort by sector
sector = st.sidebar.selectbox("Sector:", ('','Technology','Construction',
'Property','Energy','Finance Services','Utilities','Plantation',
'Industrial Products & Services','Healthcare','Consumer Products & Services',
'Telecommunications & Media','Transportation & Logistics'))

def graph_sector_wr(sector_):
    sector=sector_
    df_sector=df_wr[df_wr.Sector==sector].sort_values(by="Year")
    df_graph=pe.bar(data_frame=df_sector,x='Year',y='Value of winning rate',title='Winning Rate for {}'.format(sector))
    return df_graph

def graph_sector_pre(sector_):
    sector=sector_
    df_sector=df_pre[df_pre.Sector==sector].sort_values(by="Year")
    df_graph=pe.bar(data_frame=df_sector,x='Year',y='Value of precision',title='Precision for {}'.format(sector))
    return df_graph

st.subheader('Sector Performance :')
if sector =='Technology':
    st.plotly_chart(graph_sector_wr('Technology'))
    st.plotly_chart(graph_sector_pre('Technology'))

if sector =='Construction':
    st.plotly_chart(graph_sector_wr('Construction'))
    st.plotly_chart(graph_sector_pre('Construction'))

if sector =='Property':
    st.plotly_chart(graph_sector_wr('Property'))
    st.plotly_chart(graph_sector_pre('Property'))

if sector =='Energy':
    st.plotly_chart(graph_sector_wr('Energy'))
    st.plotly_chart(graph_sector_pre('Energy'))

if sector =='Finance Services':
    st.plotly_chart(graph_sector_wr('Finance Services'))
    st.plotly_chart(graph_sector_pre('Finance Services'))

if sector =='Utilities':
    st.plotly_chart(graph_sector_wr('Utilities'))
    st.plotly_chart(graph_sector_pre('Utilities'))

if sector =='Plantation':
    st.plotly_chart(graph_sector_wr('Plantation'))
    st.plotly_chart(graph_sector_pre('Plantation'))

if sector =='Industrial Products & Services':
    st.plotly_chart(graph_sector_wr('Industrial Products & Services'))
    st.plotly_chart(graph_sector_pre('Industrial Products & Services'))

if sector =='Healthcare':
    st.plotly_chart(graph_sector_wr('Healthcare'))
    st.plotly_chart(graph_sector_pre('Healthcare'))

if sector =='Consumer Products & Services':
    st.plotly_chart(graph_sector_wr('Consumer Products & Services'))
    st.plotly_chart(graph_sector_pre('Consumer Products & Services'))

if sector =='Telecommunications & Media':
    st.plotly_chart(graph_sector_wr('Telecommunications & Media'))
    st.plotly_chart(graph_sector_pre('Telecommunications & Media'))

if sector =='Transportation & Logistics':
    st.plotly_chart(graph_sector_wr('Transportation & Logistics'))
    st.plotly_chart(graph_sector_pre('Transportation & Logistics'))






    

# watchlist chart
# precision chart
#############################