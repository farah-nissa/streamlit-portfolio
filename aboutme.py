import streamlit as st
import time

def about_me():
    st.subheader('Hi! My name is Farah.')
    st.write("I'm a data scientist. I love building visualizations and making predictions.")
    st.write('Explore this site!')
    if st.button('Explore Jakarta Population'):
        st.experimental_set_query_params(page="Project")
    if st.button('Explore Jakarta Property Price'):
        st.experimental_set_query_params(page="Property Price Prediction")