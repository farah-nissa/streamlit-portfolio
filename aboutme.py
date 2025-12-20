import streamlit as st

def about_me():
    st.subheader('Hi! My name is Farah.')
    st.write("I'm a data scientist. I love building visualizations and making predictions.")

    pages = ["Project", "Property Price Prediction", "Contact"]
    pill = st.pills("Explore this site!", pages)

    if pill == "Project":
        st.switch_page("pages/project.py")
    elif pill == "Property Price Prediction":
        st.switch_page("pages/property_price_calculator.py")
    elif pill == "Contact":
        st.switch_page("pages/contact.py")