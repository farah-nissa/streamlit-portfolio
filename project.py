import streamlit as st
import pandas as pd 
import plotly.express as px

def project_display():

    st.header('Jakarta Population Through the Years')

    population_data = {
        'Year': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023,
                2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023,
                2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023,
                2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023,
                2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023,
                2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        'City' : ['Jakarta Pusat', 'Jakarta Pusat', 'Jakarta Pusat', 'Jakarta Pusat', 'Jakarta Pusat', 
                'Jakarta Pusat', 'Jakarta Pusat', 'Jakarta Pusat', 'Jakarta Pusat', 'Jakarta Pusat', 
                'Jakarta Timur', 'Jakarta Timur', 'Jakarta Timur', 'Jakarta Timur', 'Jakarta Timur', 
                'Jakarta Timur', 'Jakarta Timur', 'Jakarta Timur', 'Jakarta Timur', 'Jakarta Timur', 
                'Jakarta Barat', 'Jakarta Barat', 'Jakarta Barat', 'Jakarta Barat', 'Jakarta Barat', 
                'Jakarta Barat', 'Jakarta Barat', 'Jakarta Barat', 'Jakarta Barat', 'Jakarta Barat', 
                'Jakarta Selatan', 'Jakarta Selatan', 'Jakarta Selatan', 'Jakarta Selatan', 'Jakarta Selatan', 
                'Jakarta Selatan', 'Jakarta Selatan', 'Jakarta Selatan', 'Jakarta Selatan', 'Jakarta Selatan', 
                'Jakarta Utara', 'Jakarta Utara', 'Jakarta Utara', 'Jakarta Utara', 'Jakarta Utara', 
                'Jakarta Utara', 'Jakarta Utara', 'Jakarta Utara', 'Jakarta Utara', 'Jakarta Utara', 
                'Kep. Seribu', 'Kep. Seribu', 'Kep. Seribu', 'Kep. Seribu', 'Kep. Seribu', 
                'Kep. Seribu', 'Kep. Seribu', 'Kep. Seribu', 'Kep. Seribu', 'Kep. Seribu'],
        'Population' : [910381, 914182, 917754, 921344, 924686,
                        928109, 1056896, 1057465, 1053482, 1049314,
                        2817994, 2843816, 2868910, 2892783, 2916018,
                        2937859, 3037139, 3051866, 3066074, 3079618,
                        2430410, 2463560, 2496002, 2528065, 2559362,
                        2589933, 2434511, 2446687, 2458707, 2470054,
                        2164070, 2185711, 2206732, 2226830, 2246137,
                        2264699, 2226812, 2232442, 2234262, 2235606,
                        1729444, 1747315, 1764614, 1781316, 1797292,
                        1812915, 1778981, 1788981, 1799220, 1808985,
                        23011, 23340, 23616, 23897, 24134,
                        24295, 27749, 27996, 28262, 28523]
    }
    
    data = pd.DataFrame(population_data)

    st.markdown('### Filter Year')
    min_year = data['Year'].min()
    max_year = data['Year'].max()

    year_range = st.slider('Choose Range:', min_year, max_year, (min_year, max_year), key='year_range')
    st.write(f'You chose range: {year_range[0]}-{year_range[1]}')

    filtered_data = data[(data['Year'] >= year_range[0]) & (data['Year'] <= year_range[1])]
    
    fig = px.line(filtered_data, x='Year', y='Population', color, title='Jakarta Population Through the Years')fig.update_layout(
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='right',
        x=1
        )
    )
    st.plotly_chart(fig, use_container_width=True)