import streamlit as st
import pandas as pd 
#uncomment this line for mysql
from query import *

#set page
st.set_page_config(page_title="Dashboard",page_icon="🌓",layout="wide")

UI()

#uncomment these two lines if using Mysql database
#result=viewData()
#df=pd.DataFrame(result,columns=["name","gender","history","geography","kiswahili","civics","maths","total","average","grade","comment","rank","stream","id"])

df=pd.read_csv("results.csv")

#side bar: switcher
gender=st.sidebar.multiselect(
    label="Select Gender",
    options=df["gender"].unique(),
    default=df["gender"].unique(),
    )

stream=st.sidebar.multiselect(
    label="select Stream",
    options=df["stream"].unique(),
    default=df["stream"].unique(),
    )
comment=st.sidebar.multiselect(
    label="select Comment",
    options=df["comment"].unique(),
     default=df["comment"].unique(),
    )
#get selected item

df_selection=df.query(
    "gender==@gender & stream==@stream & comment==@comment"
)

#method to dowload dataframe as excel
@st.cache_resource
def convert_df(dataConvert):
    return dataConvert.to_csv(index=True).encode('utf=8')

with st.expander("⏱ Filter Tabulation"):
 #plot tabulation
 tab=pd.crosstab([df_selection["gender"],df_selection["comment"]],df_selection["stream"],margins=True)
 st.dataframe(tab,use_container_width=True)
 #downloading link
 csv1=convert_df(tab)
 st.download_button("Press to Download",csv1,"yourfile.csv",key='download-csv')


with st.expander("⏱ All Student List"):
 #plot tabulation
 showData=st.multiselect('Filter Now',df_selection.columns,default=["name","gender","history","geography","kiswahili","civics","maths","total","average","grade","comment","rank","stream"])
 st.dataframe(df_selection[showData],use_container_width=True)
 #downloading link
 csv2=convert_df(df_selection[showData])
 st.download_button("Press to Download",csv2,"yourfile.csv",key='download-csv-file')

with st.expander("⏱ Search student by name"):
    text_search=st.text_input("Search by Name",value="",placeholder="Enter name or stream")
    #filter data using mask
    m1=df["stream"].str.contains(text_search)
    m2=df["name"].str.contains(text_search)
    df_search=df[m1 | m2]
    if text_search:
        st.caption(f"results of: {text_search}")
        st.dataframe(df_search,use_container_width=True )
    else:
        text_search=""


