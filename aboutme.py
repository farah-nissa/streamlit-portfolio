import streamlit as st
import time

def about_me():
    st.subheader('Hi! My name is Farah.')
    st.write("I'm a data scientist. I love building visualizations and making predictions.")
    if st.button("Explore this site"):
        with st.spinner('Loading projects...'):
            time.sleep(1)  
        if st.button('Explore Jakarta Population'):
            st.switch_page("Project")
        if st.button('Explore Jakarta Property Price'):
            st.switch_page("property_price_calculator.py")