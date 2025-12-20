import streamlit as st

def about_me():
    st.subheader('Hi! My name is Farah.')
    st.write("I'm a data scientist. I love building visualizations and making predictions.")
    if st.button("Explore this site"):
        with st.spinner('Loading...'):
            st.write("")  # placeholder for loading
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Explore Jakarta Population'):
                # navigate to project.py page
                st.experimental_rerun()  # or use st.switch_page() if Streamlit 1.30+
        with col2:
            if st.button('Explore Jakarta Property Price'):
                # navigate to property_price_calculator.py page
                st.experimental_rerun()  # or use st.switch_page() if Streamlit 1.30+