import streamlit as st
import pyTigerGraph as tg
import pandas as pd
import flat_table
import streamlit.components.v1 as components

TG_HOST = "https://oh-yea.i.tgcloud.io"
TG_USERNAME = "tigergraph"
TG_PASSWORD = "123qwe"
TG_GRAPHNAME = "MyGraph"
TG_SECRET = "rhepq4eepl7shelknibv3svemcrmtf27"

conn = tg.TigerGraphConnection(
    host = TG_HOST,
    username = TG_USERNAME,
    password = TG_PASSWORD,
    graphname = TG_GRAPHNAME,
)

conn.getToken(TG_SECRET)

st.title("Streamlit Test")

text = st.text_input("Enter Prescriber")

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')



left_column, right_column, o,  = st.beta_columns(3)

with o:
    components.iframe("https://docs.streamlit.io/en/latest")
pressed = left_column.button('Press me?')



if pressed:
    right_column.write("Woohoo!")

#st.beta_container()

if(text):
    query = conn.runInstalledQuery("getPatients", {"inputPrescriber": text})
    st.text(query)

st.title("Streamlit Test")