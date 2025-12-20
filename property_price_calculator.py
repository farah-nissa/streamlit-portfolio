import streamlit as st

def property_calculator():
    with st.container():
        st.header("Property Price Calculator")
        st.write("Calculate the budget you need for a property in Jakarta.")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            with st.container():
                st.subheader("District")
                district_list = ["Menteng", "Setiabudi", "Pulo Gadung", "PIK", 'Pluit', 'Cibubur', 'Cilandak', 'Kebayoran Baru', 'Kebayoran Lama', 'Kemang', 'Muara Angke', 'Kembangan', 'Jagakarsa', 'Ciracas', 'Tebet', 'Kelapa Gading', 'Cengkareng', 'Tanjung Barat', 'Cakung']
                selected_district = st.selectbox("Select District", district_list, label_visibility="collapsed")
                if selected_district == 'Menteng': 
                    a = 1
                elif selected_district in ['Setiabudi', 'Kebayoran Baru']: 
                    a = 0.9
                elif selected_district in ['PIK', 'Kemang', 'Kebayoran Lama']: 
                    a = 0.7
                elif selected_district in ['Pluit', 'Tebet', 'Cilandak', 'Kembangan','Kelapa Gading']: 
                    a = 0.6
                elif selected_district in ['Pulo Gadung', 'Tanjung Barat']: 
                    a = 0.45
                elif selected_district in ['Cibubur', 'Muara Angke', 'Jagakarsa']: 
                    a = 0.35
                else: 
                    a = 0.25

        with col2:
            with st.container():
                st.subheader("Total Area")
                area_options = ['50-100 sqm', '100-150 sqm', '150-200 sqm', '200-250 sqm', '250-300 sqm', '300-400 sqm', '400-600 sqm', '600-800 sqm', '800-1000 sqm']
                selected_area = st.selectbox("Select Area", area_options, label_visibility="collapsed")
                if selected_area == '50-100 sqm': 
                    b = 0.1
                elif selected_area == '100-150 sqm': 
                    b = 0.2
                elif selected_area == '150-200 sqm': 
                    b = 0.3
                elif selected_area == '200-250 sqm': 
                    b = 0.4
                elif selected_area == '250-300 sqm': 
                    b = 0.5
                elif selected_area == '300-400 sqm': 
                    b = 0.6
                elif selected_area == '400-600 sqm': 
                    b = 0.7
                elif selected_area == '600-800 sqm': 
                    b = 0.8
                elif selected_area == '800-1000 sqm': 
                    b = 1

        with col3:
            with st.container():
                st.subheader("Street Width")
                lane_options = ['1 lane', '2 lanes', '3 lanes', '4 lanes']
                selected_lane = st.selectbox('Select Lane', lane_options, label_visibility="collapsed")
                if selected_lane == '1 lane': 
                    c = 0.5
                elif selected_lane == '2 lanes': 
                    c = 0.65
                elif selected_lane == '3 lanes': 
                    c = 0.8
                elif selected_lane == '4 lanes': 
                    c = 1

        with col4:
            with st.container():
                st.subheader("Building Type")
                building_types = ['Landed House (New)', 'Landed House (Old)', 'Apartment (>2010 Building)', 'Apartment (<2009 Building)', 'Land']
                selected_building = st.selectbox('Select Type', building_types, label_visibility="collapsed")
                if selected_building == 'Landed House (New)': 
                    d = 1
                if selected_building == 'Landed House (Old)': 
                    d = 0.75
                elif selected_building == 'Apartment (>2010 Building)': 
                    d = 0.85
                elif selected_building == 'Apartment (<2009 Building)': 
                    d = 0.55
                elif selected_building == 'Land': 
                    d = 0.65

        if st.button("Calculate Price"):
            st.write(f"IDR {round((a*b*c*d)*60, 2)} billion")