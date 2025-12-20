import streamlit as st
import time

def about_me():
    st.subheader('Hi! My name is Farah.')
    st.write("I'm a data scientist. I love building visualizations and making predictions.")
    st.write('Explore this site!')
    st.button('Explore Jakarta Population', on_click=lambda: st.experimental_set_query_params(page="Project"))
    st.button('Explore Jakarta Property Price', on_click=lambda: st.experimental_set_query_params(page="Property Price Prediction"))