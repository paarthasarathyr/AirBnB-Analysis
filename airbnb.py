import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from streamlit_option_menu import option_menu

# Load the dataset

df = pd.read_csv('airbnb.csv')

# Streamlit application
icon = Image.open("airbnb.jpg")
st.set_page_config(page_title="AirBnB Data Analysis",
                    page_icon=icon,
                    layout="wide",
                    initial_sidebar_state="expanded")

# Page title 
st.markdown("""
        <style>
            .pageTitle {
                text-align: center;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)

# Display the title in the dashboard
st.markdown("""
        <h1 style='text-align: center; color: red;'>Airbnb Navigator: Navigating Market Dynamics and Optimizing Hospitality Strategies</h1>
        <p style='text-align: center; color: red;'>--- by Paarthasarathy Rengasamy</p>
    """, unsafe_allow_html=True)



# CREATING OPTION MENU
selected = option_menu(
    None,
    ["Home", "Data Visualzation"],
    icons=["home", "cloud-upload-alt", "edit"],
    default_index=0,
    orientation="horizontal",
    styles={
        "nav-link": {
            "font-size": "25px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "white",
            "transition": "color 0.3s ease, background-color 0.3s ease"
        },
        "icon": {"font-size": "25px", "color": "black"},  # Change the icon color here
        "container": {
            "max-width": "6000px",
            "padding": "10px",
            "border-radius": "5px"
        },
        "nav-link-selected": {
            "background-color": "Green",
            "color": "black"
        }
    }
)

# HOME PAGE
if selected == "Home":
    st.title('AirBnB Data Analysis')

    st.markdown("## Overview:")
    st.markdown('- The "Airbnb Navigator: Navigating Market Dynamics and Optimizing Hospitality Strategies" project aims to provide a comprehensive analysis of the Airbnb market.')
    st.markdown('-  By leveraging data exploration and visualization techniques, the project explores various facets such as booking trends, popular property types, and the impact of different cancellation policies.')
    st.markdown('- Hosts and stakeholders can utilize the insights gained to optimize their hospitality strategies, enhance property listings, and navigate market dynamics effectively.')    
    st.markdown('- The project combines data-driven exploration with actionable recommendations, empowering users to make informed decisions in the dynamic landscape of Airbnb hosting.')
    
    st.markdown("## Tools and Technologies:")
    st.markdown("- Python Scripting")
    st.markdown("- Data Collection")
    st.markdown("- MongoDB")
    st.markdown("- Data Processing")
    st.markdown("- Streamlit")
    st.markdown("- Data Visualization")
    
    st.markdown("## Outcomes:")
    st.markdown('The project aims to bring tangible benefits to hosts, travelers, Airbnb management and the broader public by providing valuable insights, promoting informed decision-making and contributing to the growth of the sharing economy and local tourism.')
    st.markdown('## Market Insights for Hosts:')
    st.markdown('- The project provides Airbnb hosts with valuable market insights, helping them optimize pricing strategies, understand demand fluctuations, and enhance property listings.')
    st.markdown('- Hosts can make informed decisions to improve occupancy rates, cater to specific guest preferences, and ultimately increase their revenue.')
    st.markdown('## Enhanced Guest Experience:')
    st.markdown('- For travelers and the common public, the project contributes to an improved booking experience by offering insights into pricing trends, property availability, and the popularity of specific locations.')
    st.markdown('- Users can make more informed decisions when choosing accommodations that align with their preferences and travel plans.')            
    st.markdown('## Strategic Planning for Airbnb Management:')
    st.markdown('- Airbnb management can utilize the project to understand market dynamics, identify trends, and make strategic decisions to stay competitive in the dynamic sharing economy.')
    st.markdown('- The insights gained can guide the development of new services, marketing strategies, and platform improvements to enhance the overall Airbnb experience.')
    st.markdown('## Contribution to Local Economy and Tourism:')
    st.markdown('- The project indirectly benefits local economies and the tourism industry by providing insights into location-based preferences and trends.')
    st.markdown('- Stakeholders in the hospitality and tourism sectors can use this information to adapt their offerings and attract more visitors.')
    st.markdown('## Transparency and Informed Decision-Making:')
    st.markdown('- For the common public, the project promotes transparency in the Airbnb market, allowing users to make more informed decisions when booking accommodations')
    st.markdown('- It contributes to a more open and data-driven sharing economy.')


if selected == "Data Visualzation":
    # Sidebar with filters and dropdowns
    st.sidebar.header(':green[Data Explorations]')

    # Country filter
    selected_country = st.sidebar.selectbox('Select Country', ['All'] + df['country'].unique().tolist())

    # Property type filter
    selected_property_type = st.sidebar.multiselect('Select Property Type(s)', df['property_type'].unique())

    # Cancellation policy filter
    selected_cancellation_policy = st.sidebar.multiselect('Select Cancellation Policy(ies)', df['cancellation_policy'].unique())

    # Apply filters
    filtered_df = df.copy()

    if selected_country != 'All':
        filtered_df = filtered_df[filtered_df['country'] == selected_country]

    if selected_property_type:
        filtered_df = filtered_df[filtered_df['property_type'].isin(selected_property_type)]

    if selected_cancellation_policy:
        filtered_df = filtered_df[filtered_df['cancellation_policy'].isin(selected_cancellation_policy)]

    st.subheader(' Exploring Insights with Diverse Data Visualizations in Airbnb Dataset')

    st.markdown('''This project employs diverse data visualization techniques, including stacked bar charts, bubble charts, donut charts, 
                box plot charts, customized bubble charts and horizontal charts. The aim is to extract meaningful insights
                 and present findings in a visually appealing and informative manner.''')

    # Visualize the distribution of property in stacked bar chart

    st.subheader('Property Type Spread Across Different Nations')
    fig_bar = px.bar(filtered_df, x='country', color='property_type', labels={'property_type': 'Property Type'})
    st.plotly_chart(fig_bar)

    st.markdown(':red[Observations]')
    st.markdown('- Upon analyzing the data, it becomes evident that the choice of accommodation is significantly influenced by the type of property. ')
    st.markdown('- Primarily, individuals exhibit a preference for staying in Apartments and Houses, influenced by a variety of factors. Notably, in the United States, there is a notable increase in the popularity of Condominium stays compared to other countries.')
    
                            
    # Price variations by country

    st.subheader('Differences in Prices Across Various Countries')
    price_by_country = filtered_df.groupby('country')['price'].max().reset_index()

    # Visualize price variations among countries
    fig = px.bar(price_by_country, x='country', y='price', title='Maximum Price by Country')
    st.plotly_chart(fig)

    min_price = filtered_df['price'].min()
    max_price = filtered_df['price'].max()
    average_price = filtered_df['price'].mean()

    st.write(f"Min Price: {min_price}")
    st.write(f"Max Price: {max_price}")
    st.write(f"Average Price: {average_price}")

    st.markdown(':red[Observations]')
    st.markdown('- In the travel industry, pricing emerges as a pivotal factor. According to the latest data, Turkey boasts the highest accommodation prices, reaching around 48k, while Portugal presents the most affordable option with a minimum of 9.')
    st.markdown('- Various factors contribute to the elevated prices, such as the abundance of tourist attractions, safety measures, cleanliness standards, and more.')

    # Visualize the cancellation policy distribution using a donut chart

    st.subheader('Diversity of Cancellation Rules Among Accommodations')
    fig_donut = px.pie(filtered_df, names='cancellation_policy')
    st.plotly_chart(fig_donut)

    st.markdown(':red[Observations]')

    st.markdown('- Across all countries, individuals generally favor a range of cancellation policies for accommodation bookings, including options like moderate, flexible, and even strict_14 days with a grace period.')
    st.markdown('- Notably, the United States stands out from other nations, displaying approximately 5% of bookings adhering to the strict_60 cancellation policy.')


    # Visualize the relationship between the number of reviews and the average review scores using a bubble chart

    st.subheader('Comparison of Review Counts and Average Review Scores')
    fig_bubble = px.scatter(filtered_df, x='number_of_reviews', y='review_scores', size='number_of_reviews', color='review_scores')
    st.plotly_chart(fig_bubble)

    st.markdown(':red[Observations]')

    st.markdown('- Reviews and ratings play a crucial role in the realm of accommodation bookings')
    st.markdown('- Elevated reviews and ratings directly correlate with increased booking volumes.')


    st.subheader('Fluctuations in Accommodation Costs')

    # box plot for outliers

    fig = px.box(df, y=["price"])

    st.plotly_chart(fig)

    st.markdown(':red[Observations]')

    st.markdown('- The BoxPlot chart aids in identifying price variations and detecting outliers.')
    st.markdown('- Within this dataset, the prices exhibit a range from the minimum to the maximum of 50k. Specifically, the maximum prices predominantly fall within the 0-20k range.')
    st.markdown('- However, there is an outlier observed at approximately 50k, signifying an exceptional data point in this specific dataset.')

    # Customized bubble chart for reviews and availabilities

    st.subheader('Tailored Bubble Chart Representations')

    x_column = st.selectbox('Select X-Axis Column', ['number_of_reviews', 'bedrooms', 'accommodates'])
    y_column = st.selectbox('Select Y-Axis Column', ['review_scores', 'bathrooms', 'price'])
    size_column = st.selectbox('Select Size Column', ['availability_30', 'availability_60', 'availability_90','availability_365'])
    color_column = st.selectbox('Select Color Column', ['beds', 'extra_people', 'cleaning_fee'])

    fig_custom_bubble = px.scatter(
        filtered_df,
        x=x_column,
        y=y_column,
        size=size_column,
        color=color_column,
        labels={x_column: x_column.capitalize(), y_column: y_column.capitalize()},
        size_max=50,
    )

    st.plotly_chart(fig_custom_bubble)

    st.subheader('Leading Amenities')

    # Preprocess the amenities column
    amenities_list = [amenity.strip('{}').replace('"', '') for amenity in df['amenities']]
    all_amenities = ', '.join(amenities_list).split(', ')
    amenities_counter = Counter(all_amenities)

    # Convert Counter to DataFrame for Plotly
    amenities_df = pd.DataFrame.from_dict(amenities_counter, orient='index', columns=['Count']).reset_index()
    amenities_df.columns = ['Amenity', 'Count']

    # Visualize the frequency of each amenity using a horizontal bar chart

    fig_amenities = px.bar(
        amenities_df.sort_values(by='Count', ascending=False),
        x='Count',
        y='Amenity',
        orientation='h',    
        labels={'Amenity': 'Amenity', 'Count': 'Count'},
    )
    st.plotly_chart(fig_amenities)

    st.markdown(':red[Observations]')

    st.markdown('- Globally, individuals anticipate certain fundamental amenities when reserving accommodations.')
    st.markdown("- Across Airbnb and many hotels or apartments, standard offerings encompass amenities such as a kitchen, Wi-Fi, TV, dryer, office setup, parking, elevators, microwave, fire extinguisher, and more.")
    st.markdown('- The expansion of amenity options is directly linked to fluctuations in accommodation prices.')