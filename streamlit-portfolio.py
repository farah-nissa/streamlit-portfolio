import streamlit as st

st.set_page_vonfig(layout='wide')
st.title("Farah's Portfolio")
st.header('Data Scientist')

st.sidebar/title('Navigation')

page = st.sidebar.radio('Pages', ['About Me', 'Project', 'Prediction', 'Contact'])
