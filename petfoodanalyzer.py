import streamlit as st
import st_aggrid
from st_aggrid import *

# from IPython.display import HTML, display
import re

from dog_food_analyzer_utils import *
from dog_food_analyzer_dictionaries import *

# from panel_dictionary import panel_rule

import numpy as np
import pandas as pd

import plotly.express as px


# show screen in wide mode while launching the app
st.set_page_config(layout="wide")

# styling with css for margin and padding
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 1rem;
                    padding-bottom: 1rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

# defining a function to read data in minimum time
# @st.cache(allow_output_mutation=True)
# def data_read(file):
#     return pd.read_csv(file, sep='|', encoding='utf-8')


# main_data = data_read(
#     "D:\\Pet Food Reader\\Streamlit\\Data\\Streamlit\\Data\\data_for_streamlit_reduced_20_07_23.csv")



tabs = ["Introduction", 'Ingredient Quality Check',
        'Major Energy Sources', 'CO2 Emissions']
whitespace = 23
intro, ingredient_analyzer, energy, emissions = st.tabs(
    [s.center(whitespace, "\u2001") for s in tabs])


# 1st page
with intro:
    # Title
    st.markdown("<h2 style='color: #2980b9;'>📚 What is this App for?</h2>", unsafe_allow_html=True)

    # Description
    st.markdown(
    """
    <p style='font-size: 18px;'>The Purpose of this App is as follows:</p>
    <ol style='font-size: 18px;'>
        <li>🔍 <strong>Ingredient Quality Check:</strong> Checks the quality of each ingredient pasted by the user in the panel along with an explanation.</li>
        <li>⚡ <strong>Major Energy Sources:</strong> Calculates the contribution of energy by each ingredient and classifies them into "High", "Moderate", or "Low" Energy contributors. This allows the user to understand the majority of energy sources in their diet.</li>
        <li>🌍 <strong>CO2 Emissions:</strong> Calculates the CO2 emission of each ingredient panel and, based on careful assumptions of proportions, provides the total CO2 emission value of the panel on a per 1000 kcal basis.</li>
    </ol>
    """, unsafe_allow_html=True
    )
    # st.markdown("")
#     st.markdown("### Steps:")

#     st.markdown(
# """
# 1. **Ingredient Analyzer section**: Paste the ingredients in the empty space as written on your dog food packaging. If you don't have any, visit [chewy](https://www.chewy.com/)
# 2. **Pet Information section**: Enter the name, gender, species, etc. info of your pet
# 3. **Preferences**: Choose your preferences such as food texture and contents
# 4. **Best Products**: Take a look at the best products and select any two for comparison


# """)

# 2nd page
with ingredient_analyzer:
    # Creating a layout with space for better visual appeal
    space, ingredient_col, space_1, diet_category_col, space_2 = st.columns([0.2, 3, 0.15, 2.5, 0.01])

    # Ingredient Input Section
    with ingredient_col:
        st.markdown("<h2 style='color: #2980b9;'>📝 Enter Ingredient List:</h2>", unsafe_allow_html=True)
        ing_str = st.text_area('Enter Ingredient List:', height=220, label_visibility='collapsed', key='ia')

    # Process the ingredient list
    try:
        # Check if the ingredient string is empty
        if ing_str.strip() == '':
            st.error('❌ Please enter the ingredient list.')
        else:
            # Process the ingredient list
            ing_result = preprocess_ingredients(ing_str)
            ing_result_df = pd.DataFrame(ing_result).T.reset_index().rename(columns={"index": "ingredient"})

            # Display Quality and Type Selection if ingredients are processed
            with diet_category_col:
                if len(ing_result) != 0:
#                     st.markdown(f'##### ✅ The Panel You Entered has {ing_result_df["Quality"].nunique()} Qualities of Ingredients:')
                    st.markdown(f'##### ✅ Select Category of Ingredients:')
                    selected_p_c = st.radio('🔍 Selected Category:', ing_result_df["parent_category"].unique(), label_visibility='collapsed')

                    st.markdown(f'##### 📦 Select the Sub-Category:')
                    selected_qt = st.radio('🔎 Selected Type:', list(ing_result_df[ing_result_df['parent_category'] == selected_p_c]['sub_category'].unique()), label_visibility='collapsed')

            # Display Actual Ingredients and Explanation
            with ingredient_col:
                if len(ing_result) != 0:
#                     st.markdown('#### 📋 Ingredient/s from Selected Category:')
                    
                    ing_result_df_f  = ing_result_df[(ing_result_df['parent_category'] == selected_p_c) & (ing_result_df['sub_category'] == selected_qt)]
                    
#                     st.write(", ".join(list(ing_result_df_f['Ingredient'])))
                    
                    
                    ing_result_df_f_g = ing_result_df_f.groupby(["Quality",
                                            "Quality Description"],
                                           as_index=False).agg({"Ingredient":lambda x: ", ".join(list(x.unique()))})
                    
                    
#                     ing_result_df_f_g_a = ing_result_df_f_g[""]
                        
#                     st.markdown('#### 📋 Ingredients & their Quality:')
#                     st.write(ing_result_df_f_g)
                    for each in ing_result_df_f_g.to_records():
#                         st.write(each)
                        
                        st.markdown(f'#### 📋 {each[1]} Ingredients:')
                        st.markdown(f'***{each[3]}***')
#                     st.markdown(f"{}")
#                     st.write(ing_result_df_f_g[ing_result_df_f_g["Quality"]=='Poor Quality'].iloc[0]['Ingredient'])
                    
#                     st.markdown('#### 📖 Explanation:')
#                     st.markdown(f"{ing_result_df[ing_result_df['Type'] == selected_qt]['Quality Description'].unique()[0]}")

    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
        st.error("❌ Enter Ingredients Properly!")

        
with energy:
    try:
        # Section Header
        st.markdown("<h2 style='color: #2980b9;'>⚡ Energy Contribution Overview:</h2>", unsafe_allow_html=True)
        st.markdown(f"<p>Your Ingredient Panel: <strong>{ing_str}</strong></p>", unsafe_allow_html=True)
        
        

        # Process the ingredients
        e = ingredients_pre(ing_str)

        # Calculate Contribution
        e["Contribution"] = e['Total KCAL'] * 100 / e["Total KCAL"].sum()
        e = e.sort_values(by="Contribution", ascending=False)
#         st.write(f"{e['Total KCAL'].sum()}")

        esf = int(round(e['Energy from Fat'].sum()))
        esp = int(round(e['Energy from Protein'].sum()))
        esc = int(round(e['Energy from Carbs'].sum()))
                  
        est = esf + esp + esc
                  
        st.markdown(f"- <p>Energy from Fat: <strong>{esf} kcal</strong></p>", unsafe_allow_html=True)
        st.markdown(f"- <p>Energy from Protein: <strong>{esp} kcal</strong></p>", unsafe_allow_html=True)
        st.markdown(f"- <p>Energy from Carbs: <strong>{esc} kcal</strong></p>", unsafe_allow_html=True)
        
        st.markdown(f"- <p>Total Energy Deliverered (per kg): <strong>{est} kcal</strong></p>", unsafe_allow_html=True)
#         # Create the Bar Plot
#         fig = px.bar(
#             e,
#             x='Ingredient',
#             y='Contribution',
#             height=650,
#             text=(e['Contribution'].fillna(0).round(0).astype(int).astype(str) + '%')  # Handle NaN and add %
#         )

#         # Update layout to position text above the bars
#         fig.update_traces(textposition='outside')

#         # Update overall layout
#         fig.update_layout(
#             title=f"🧮 Contribution of Energy<br>Total Estimated Energy from the Product: {int(e['KCAL'].sum())} kcal/kg.",
#             xaxis_title='Ingredients 🍽️',
#             yaxis_title='Contributions (%) 📊',
#             template='plotly_white'  # Light theme for better visibility
#         )

#         # Display the figure in Streamlit
#         st.plotly_chart(fig, use_container_width=True)
        

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        st.error("Please ensure your ingredients are entered properly!")

        
# 3rd page
with emissions:
    try:
        # Section Header
        # Using inline styles for headers and text
        st.markdown(
    "<h2 style='color: #2c3e50; font-weight: bold;'>🌍 Environmental Impact of Your Dog's Daily Diet</h2>", 
    unsafe_allow_html=True
)

        st.markdown(
    "<p style='font-size: 19px; '>The Daily CO2 equivalent emissions from a typical dog based on the provided ingredient panel:</p>", 
    unsafe_allow_html=True
)
        st.markdown("---")  # Divider for better separation

        # Calculate emissions
        co2 = round(e["Emissions"].sum() * 1200 / int(e['Total KCAL'].sum()), 2)
        co2_per_year = co2*365

        # Display energy per kg of product
#         st.markdown(f"<p><span class='highlight-text'>Energy per kg of Product:</span> {int(e['KCAL'].sum())} kcal/kg</p>", unsafe_allow_html=True)

        # Spacing for better layout
        st.markdown("### 🐾 CO2 Emissions:")

        # Displaying metrics with icons
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="metric-box">', unsafe_allow_html=True)
            st.metric(label="Per Day 🌱", value=f"{int(round(co2))} kg CO2 eq.")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="metric-box">', unsafe_allow_html=True)
            st.metric(label="Per Year 🌎", value=f"{int(round(co2 * 365))} kg CO2 eq.")
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("---")  # Divider for better separation
        
        # Gallons of gasoline consumed calculation
        gallons_of_gasoline = int(round(co2_per_year / (8887 * 0.001)))  # Convert grams to metric tons

        # Miles driven calculation
        miles_driven = int(round(co2_per_year * 0.001 / (3.91 * 10**-4)))  # Convert kg to metric tons
        

        
        # Displaying additional metrics in the same format
        col3, col4 = st.columns(2)

        # Displaying additional metrics in the same format
        st.markdown(
            "<h3 style='color: #2980b9;'>🚗 Additional Emissions Metrics:</h3>", 
            unsafe_allow_html=True
        )

        # Displaying additional metrics in the same format
        col3, col4 = st.columns(2)

        with col3:
            st.markdown('<div style="margin-bottom: 20px;">', unsafe_allow_html=True)
            st.metric(label="⛽ Gallons of Gasoline Consumed", value=f"{int(round(gallons_of_gasoline))} gallons")
            st.markdown('</div>', unsafe_allow_html=True)

        with col4:
            st.markdown('<div style="margin-bottom: 20px;">', unsafe_allow_html=True)
            st.metric(label="🚙 Miles Driven by Average Vehicle", value=f"{int(round(miles_driven))} miles")
            st.markdown('</div>', unsafe_allow_html=True)

        # Final explanation or note
        st.markdown(
            "<p>These metrics provide further insight into the environmental impact of your pet's diet.</p>", 
            unsafe_allow_html=True
        )
#         st.markdown()
        st.markdown("---")
        
        
        st.markdown(
            "<h3 style='color: #2980b9;'> What is the Additional Cost?:</h3>", 
            unsafe_allow_html=True
        )
        
        st.metric(label="Considering 551.87 pence per gallon", value=f"{int(round(gallons_of_gasoline*5.5187))} £ per year")
        
    except:
        st.error("Please enter valid ingredient data to calculate emissions!")
