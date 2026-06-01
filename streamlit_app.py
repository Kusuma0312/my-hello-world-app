import streamlit as st
import pandas as pd
import numpy as np
st.title("Hello world!")
with st.sidebar:
 st.header("About app")
 st.write("This is my first app")
st.header('This is header with divider',divider='rainbow')
st.markdown('This is created using st.markdown()')
col1,col2 = st.columns(2)
with col1:
 x= st.slider("choose an x value",1,10)
with col2:
 st.write("This value of :blue[**x**] is",x)
Chart_data = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.area_chart(Chart_data)
