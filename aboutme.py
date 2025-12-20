import streamlit as st

def about_me():
    st.subheader('Hi! My name is Farah.')
    st.write("I'm a data scientist. I love building visualizations and making predictions.")

    st.write('Explore this site!')

    if st.button("Property Price Calculator"):
        import property_price_calculator
        property_price_calculator.property_calculator()