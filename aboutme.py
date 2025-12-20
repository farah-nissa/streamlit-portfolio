import streamlit as st

def about_me():
    st.subheader('Hi! My name is Farah.')
    st.write("I'm a data scientist. I love building visualizations and making predictions.")

    pages = ["Project", "Property Price Prediction", "Contact"]
    pill = st.pills("Explore this site!", pages)

    if pill == "Project":
        st.switch_page("Project")
    elif pill == "Property Price Prediction":
        st.switch_page("Property Price Prediction")
    elif pill == "Contact":
        st.switch_page("Contact")