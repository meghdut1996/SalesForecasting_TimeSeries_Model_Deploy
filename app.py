#Core packages
import streamlit as st
# import os,glob




#Data Vizulization packages
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
from matplotlib.pylab import rcParams
rcParams['figure.figsize']=15,10

#Time Series packages
# from statsmodels.tsa.seasonal import seasonal_decompose


def main():
    st.image('img/stock.jfif',width=300)
    html_temp = """
    <div style="background-color:Crimson;"><p style="color:white;font-size:30px;padding:10px">Time Series Analysis</p></div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)  
    html_temp1 = """
    <div style="background-color:Teal;"><p style="color:white;font-size:20px;padding:10px">Sale Forecasting</p></div>
    """
    st.markdown(html_temp1,unsafe_allow_html=True) 
    DATE_TIME='date/time'    
    activities=["EDA","Visualization","Model Building","About"]
    choice_activities=st.sidebar.selectbox("Select Activity",activities)
    
    
    
            
            

if __name__=='__main__':
    main()









