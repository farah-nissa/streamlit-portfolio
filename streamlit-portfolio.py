import streamlit as st

st.set_page_config(layout='wide')
st.title("Farah's Portfolio")

st.sidebar.title('Navigation')

page = st.sidebar.radio('Pages', ['About Me', 'Project', 'Property Price Prediction', 'Contact'])

if page == 'About Me':
    import aboutme 
    aboutme.about_me()
elif page == 'Project':
    import project 
    project.project_display()
elif page == 'Property Price Prediction':
    import property_price_calculator
    property_price_calculator.property_calculator()
elif page == 'Contact':
    import contact 
    contact.show_contant()

