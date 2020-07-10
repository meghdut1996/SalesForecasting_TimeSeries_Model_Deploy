#Core packages
import streamlit as st
# import os,glob

#EDA packages
import pandas as pd
import numpy as np
# from PIL import Image


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
    
    
    #Exploratory data analysis
    if choice_activities=='EDA':
        st.subheader('Exploratory Data Analysis')
        data=st.file_uploader("Upload Dataset",type=["csv","xlsx"]) 
        if data is not None:
            df=pd.read_csv(data)
          
            if st.checkbox("Show Dataset"):
                number=st.number_input("Enter Number of rows to view")
                st.dataframe(df.head(int(number)))
 
            if st.checkbox("Show Shape"):
                st.write(df.shape)
            
            if st.checkbox("Show Columns"):
                all_columns=df.columns.to_list()
                st.write(all_columns,end='')
                
            if st.checkbox("Show Data Types"):
                st.write(df.dtypes)
                
            if st.checkbox("Select Multiple Columns to Show"):
                all_columns=df.columns.to_list()
                selected_columns=st.multiselect("Select Columns",all_columns)
                new_df=df[selected_columns]
                st.dataframe(new_df)
                              
            if st.checkbox("Show Summary"):
                st.write(df.describe(include='all'))
            
            if st.checkbox("Show Null Values"):
                missing_feature=df.isnull().sum()
                st.write(missing_feature)
              
            if st.checkbox("Show Value Counts"):
                st.text("Value Counts By Target/Class")
                st.write(df.iloc[:,-1].value_counts())
                
  
    
    #Data Visualization    
    elif choice_activities=='Visualization':
        st.subheader('Data Visualization')
        data=st.file_uploader("Upload Dataset",type=["csv","xlsx"]) 
        if data is not None:
            df=pd.read_csv(data)
            st.dataframe(df.head(7))
            
            
        if st.checkbox("Co-relation between Features (Heatmap)"):
            st.write(sns.heatmap(df.corr(),annot=True))
            st.pyplot()
      
        if st.checkbox("Pie plot"):
            all_columns=df.columns.to_list()
            columns_to_plot=st.selectbox("Select One Column",all_columns)
            if st.button("Generate Pie Plot"):
                st.success("Generating Pie Plot")
                st.write(df[columns_to_plot].value_counts().plot.pie(autopct="%1.1f%%"))
                st.pyplot()
                
        if st.checkbox("Plot of Value Counts"):
            st.text("Value Counts By Target")
            all_columns_names = df.columns.tolist()
            primary_col = st.selectbox("Primary Columm to GroupBy",all_columns_names)
            selected_columns_names = st.multiselect("Select Columns",all_columns_names)
            if st.button("Plot"):
                st.text("Generate Plot")
                if selected_columns_names:
                    vc_plot = df.groupby(primary_col)[selected_columns_names].count()
                else:
                    vc_plot = df.iloc[:,-1].value_counts()
                st.write(vc_plot.plot(kind="bar"))
                st.pyplot()
                
        st.subheader("Customizable Plot") 
        type_of_plot=st.selectbox("Select type of Plot",["Area","Bar","Histogram","line","Box","KDE"])
        all_columns_names=df.columns.tolist()
        selected_columns_names=st.multiselect("Select Columns to plot",all_columns_names)
        
        if st.button("Generate Plot"):
            st.success("Generating Customized plot of {} for {}".format(type_of_plot,selected_columns_names))
            
            if type_of_plot=="Area":
                cus_data=df[selected_columns_names]
                st.area_chart(cus_data)
                
            elif type_of_plot=="Bar":
                cus_data=df[selected_columns_names]
                st.bar_chart(cus_data)
                
            elif type_of_plot=="line":
                cus_data=df[selected_columns_names]
                st.line_chart(cus_data)
                
            elif type_of_plot=="Histogram":
                cus_data=df[selected_columns_names]
                plt.hist(cus_data,bins=20)
                st.pyplot()
                
            elif type_of_plot=="":
                cus_data=df[selected_columns_names]
                st.line_chart(cus_data)
             
            #custom plot
            elif type_of_plot:
                cust_plot=df[selected_columns_names].plot(kind=type_of_plot)
                st.write(cust_plot)
                st.pylot()
                                        
    #For Model Building   
    elif choice_activities=='Model Building':
        st.subheader('Building ML Model')
        data=st.file_uploader("Upload Dataset",type=["csv","xlsx"]) 
        if data is not None:
            df=pd.read_csv(data)
            st.dataframe(df.head(7))
 
    # About   
    elif choice_activities=='About':
        st.subheader('About')
        st.info("Built with Streamlit")
        st.info("A Simple Forecasting App for Exploring Time Series Dataset")
        st.info("Maintained by Meghdut Nandy")
        
        
        if st.button("Thanks"):
            st.balloons()
            
            
            

if __name__=='__main__':
    main()









