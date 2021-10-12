from ctypes import alignment
from os import write
from re import template
import streamlit as st
import plotly.graph_objs as go
from preparedata import loadData
import plotly.express as px

df = loadData('most_followed_ig.csv')
sidebar= st.sidebar
st.sidebar.image('icon.png')
sidebar.header('Choose your option')
choices =["ProjectOverview", " facts ","analyseData"]
selOpt =sidebar.selectbox('choose here',choices)

def ProjectOverview():
    st.title('ANALYSES OF POPULAR INSTAGRAMERS')
    st.image('logo.jpeg')
    st.markdown('''
    ## WELCOME TO MY DATA ANALYTICS  PROJECT.
    
    THE MOTIVE OF THIS IS TO ANALYSE THE MOST POPULAR INSTAGRAM CELEBRITY ON THE BASIS OF NUMBERS OF FOLLOWERS THEY HAVE
    ''',unsafe_allow_html=True)

def facts():
     st.title(" SOME FACTS ABOUT PROJECT")
     st.image('instagram.jpg')
     st.markdown('''

    

      The sum of all their followers is a whopping 6.14070613 users.
     That number is misleadingly large however, because if I follow both @instagram and @beyonce, 
     I would be counted twice in there. Still, it’s a big number.
    The total number of posts in this data set is 315,888
    
    ** Parameters used to analyse the popularity of celebreties  -- FOLLOWERS and ENGAGEMENT RATE**


    1.IN THIS PROJECT THE MAIN ASPECT OF ANALYZING THE POPULARITIES OF CELEBS ARE THE FOLLOWERS.AND "SELANA GOMEZ" TOP IN THIS PARAMETER.

    2.SECOND IMPORTANT ASPECT IS THE NUMBER OF POST EACH INSTAGRAMER OF THIS DATASET HAS MADE.

    3.LAST BUT IMPORTANT ASPECT IS THE 'ENGAGEMENT RATE OF EACH POST'

    
    
    
    ''', unsafe_allow_html=True)


    
    

    
               
    



def analyseData():
    df['FOLLOWERS']= df['FOLLOWERS'].apply(lambda a: float(a.split('M')[0]))
    df['FOLLOWERS'].head()
    st.subheader('ANALYSES BY FOLLOWERS')
    st.plotly_chart((px.bar(data_frame = df, y='FOLLOWERS', x='BRAND',   color='RANK')))
    
    





if selOpt == choices[0]:
    ProjectOverview()

elif selOpt ==choices[1]: 
    facts()

elif selOpt == choices[2]:
    analyseData()       

    



    





           

   

    
    

    






    


    

    
   
   



