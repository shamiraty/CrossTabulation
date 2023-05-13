import mysql.connector
import streamlit as st
#establish connection to MYSQL

conn=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="",
    db="students"
)
c=conn.cursor()

#fetchData

@st.cache_data
def viewData():
    c.execute('select * from results_tbl order by rank asc')
    data=c.fetchall()
    return data


def UI():
    st.markdown(""" 
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">

    
<div class="container-fluid">
<div class="card shadow">
<div class="card-body">

<div class="card">
  <div class="card-body">
    <h2 class="text-secondary">⏱ Cross Tabulation By Python </h2>
  </div>
</div>
</div>
</div>
</div>
<br>
<br>

<style>

div[data-testid="stExpander"] div[role="button"] p
{
    font-size: 1.3rem;
}


</style>


    """,unsafe_allow_html=True)