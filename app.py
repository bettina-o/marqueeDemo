
import streamlit as st
import pandas as pd

#%%
st.write("IT WORKS!")
st.header("Header")

categories = ['a','b','c']
st.multiselect("Pick a category", categories)
st.sidebar.button("Click me")

#by putting the word sidebar, it does it in a menu which can be hidden
if st.checkbox("Select me!"):
  st.write("You selected the checkbox!")
  
