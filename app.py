import streamlit as st
import plotly.graph_objs as go
from preparedata import loadData
import plotly.express as px

df = loadData('most_followed_ig.csv')

st.title('ANALAYSIS OF POPULAR CELEBRITIES')
sidebar= st.sidebar
sidebar.header('Choose your option')
choices =['Project overview','Analyses']
selOpt =sidebar.selectbox('choose option you want',choices)
st.image('logo.jpeg')

def analyseData():
    st.header('visulization here')
    if selOpt == 'Project overview':

        analyseData()

    elif selOpt == 'Analyses':

        analyseData()   



def init():
    

    st.markdown("""
    ### Perameters of analysis
1. On the bases of numbers of followers
2. Most ranked
3. Categories wise
4. Number of posts made

**Mentioned parameters will give the better understanding of project.
  

""",unsafe_allow_html=True)
st.write('')
st.markdown("""
### Analyse of most trending clebrities of instagram
    How we gonna analyse the popularity of each celebrity ?
    : We have some parameters for anlysing this


""",unsafe_allow_html=True)
    
init()

def analyseData():
    st.subheader('MOST FOLLOWED IG CELEBES BY RANK')
    st.plotly_chart(px.histogram(data_frame = df, x ='BRAND', y ='RANK', color='FOLLOWERS',template='plotly_white' ))
    st.plotly_chart( px.bar(data_frame= df ,  x='RANK', y='BRAND',
             hover_data=['MEDIA POSTED', 'FOLLOWERS'], color='RANK',
             labels={'BRAND':'BRAND'}, template='seaborn'))
    st.plotly_chart(px.bar(data_frame= df, x='BRAND', y ='CATEGORIES 1', color='FOLLOWERS',
                    template='seaborn'))
    st.plotly_chart(px.bar(data_frame= df ,  x='BRAND', y=  'CATEGORIES 2',
             hover_data=['MEDIA POSTED', 'ER'], color='FOLLOWERS' ,
             labels={'FOLLOWERS':'FOLLOWERS'}))
    st.plotly_chart(px.scatter_3d(data_frame= df, x ='BRAND' ,y= 'CATEGORIES 1', z = 'CATEGORIES 2' ,color='iPOSTS ON HASHTAG' ,height= 700,   color_continuous_scale=px.colors.convert_colorscale_to_rgb  ,template= 'plotly_white'))         
    st.plotly_chart(px.scatter(df, x="BRAND", y="CATEGORIES 1", color='FOLLOWERS', template='ggplot2'))
    st.plotly_chart(px.bar(data_frame = df, x ='BRAND', y ='CATEGORIES 2' ,color= 'MEDIA POSTED' , template='seaborn'))  
    st.plotly_chart(px.bar(data_frame = df, x ='BRAND', y ='CATEGORIES 1' ,color= 'iPOSTS ON HASHTAG' , template='seaborn'))  
    st.plotly_chart(px.scatter(df, x="BRAND", y="CATEGORIES 2", color='MEDIA POSTED', template='seaborn')) 
    st.plotly_chart(px.bar(df, x="BRAND", y="CATEGORIES 2", color="RANK",
             hover_data=["ER", "FOLLOWERS"],
             height=400,template='seaborn')
             )              

analyseData()             
           

   

    
    

    






    


    

    
   
   



