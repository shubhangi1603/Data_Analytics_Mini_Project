
import streamlit as st
from preparedata import loadData
import plotly.express as px


df = loadData('most_followed_ig.csv')
sidebar= st.sidebar
st.sidebar.image('insta.gif')
sidebar.header('Choose your option')
choices =["ProjectOverview", " facts ","analyseData"]
selOpt =sidebar.selectbox('choose here',choices)



def ProjectOverview():

    st.title('TOP 100 MOST FOLLOWED CELEBRITIES')
    st.image('logo.jpeg')
    st.markdown('''
    ## WELCOME TO MY DATA ANALYTICS  PROJECT.
    
    THE MOTIVE OF THIS IS TO ANALYSE THAT WHO IS  MOST POPULAR CELEBRITY OF INSTAGRAM.
    AND FOR THIS ANALYSES WE HAVE SOME PARAMETERS ACCORDING TO THE DATA SET USED IN THIS PROJECT.
    AND THE MAIN ASPECT IN THE NUMBER OF FOLLOWERS.AND SOME OTHER FACTS ARE ALSO INCLUDED LET'S SEE WHO  WILL TOP IN THIS LIST. 
    ''',unsafe_allow_html=True)

    df['FOLLOWERS']= df['FOLLOWERS'].apply(lambda a: float(a.split('M')[0]))
    df['FOLLOWERS'].head()
    st.plotly_chart(px.bar(data_frame = df, y='FOLLOWERS', x='BRAND',   color='RANK',template='xgridoff',title='Analyses by most number of followers'))
    st.plotly_chart(px.bar(data_frame = df, x='FOLLOWERS', y='BRAND',   color='RANK',template='ygridoff',title='Analyses by least number of followers'))
    
    
 
    

def facts():
     st.title(" SOME FACTS ABOUT PROJECT")
     st.image('icon.png',width= 350)
     st.markdown('''
    The sum of all their followers is a whopping 6.14070613 users.
    That number is misleadingly large however, because if I follow both @instagram and @beyonce, 
    I would be counted twice in there. Still, it’s a big number.
    The total number of posts in this data set is 315,888
    
    ** Parameters used to analyse the popularity of celebreties  -- FOLLOWERS and ENGAGEMENT RATE**


    1.IN THIS PROJECT THE MAIN ASPECT OF ANALYZING THE POPULARITIES OF CELEBS ARE THE FOLLOWERS.AND "SALENA GOMEZ" TOP IN THIS PARAMETER.

    2.SECOND IMPORTANT ASPECT IS THE NUMBER OF POST EACH INSTAGRAMER OF THIS DATASET HAS MADE.

    3.LAST BUT IMPORTANT ASPECT IS THE 'ENGAGEMENT RATE OF EACH POST'
   

    ''', unsafe_allow_html=True)
    
      
    



def analyseData():
    df['FOLLOWERS']= df['FOLLOWERS'].apply(lambda a: float(a.split('M')[0]))
    df['FOLLOWERS'].head()
    
    st.plotly_chart(px. scatter_3d( data_frame= df, x ='BRAND' ,y= 'CATEGORIES 1', z = 'FOLLOWERS' ,color='RANK' ,height= 700, template= 'plotly_dark',title='Analyses by Categories 1'))
    st.plotly_chart(px.box(df, y='FOLLOWERS', x='CATEGORIES 2',points='all',title='ANALYSES by Categories 2',template='xgridoff'))
    df['ER']= df['ER'].apply(lambda a: float(a.split('%')[0]))
    df['ER'].head()
    st.plotly_chart(px.bar(data_frame = df, y='ER', x='BRAND',   color='RANK',template='ygridoff',title='Analyses By The Engagement Rate '))
    st.plotly_chart(px.scatter(df, y='FOLLOWERS',x='ER',color='BRAND',template='xgridoff',title='Analyses by Followers and engagement rate '))
    most_types =df.groupby('CATEGORIES 1',as_index=False).mean()
    most_types.head()
    st.plotly_chart(px.pie(data_frame = most_types,labels = 'BRAND',values= 'FOLLOWERS', names='CATEGORIES 1',template='ggplot2',title='Analyses by most number of followers based on categories 1'))
    df['MEDIA POSTED']= df['MEDIA POSTED'].apply(lambda a: str(a.split('k')[0]))
    df['MEDIA POSTED'].head()
    st.plotly_chart(px.density_heatmap(df,y='MEDIA POSTED',template='xgridoff',title='Analyses by Media Posted'))






if selOpt == choices[0]:
     ProjectOverview()
elif selOpt == choices[1]:
    facts()
elif selOpt == choices[2]:
     analyseData()








    

               








 
    



    





           

   

    
    

    






    


    

    
   
   



