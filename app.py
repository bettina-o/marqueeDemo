
import streamlit as st
import pandas as pd

#%%
st.write("IT WORKS!")
st.header("Header")

categories = ['a','b','c']
st.multiselect("Pick a category", categories)
if st.button("Click me"):
  st.write("Why did you not select instead?")
if st.checkbox("Select me!"):
  st.write("You selected the checkbox!")
  
