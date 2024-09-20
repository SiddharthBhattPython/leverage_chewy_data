import streamlit as st
import st_aggrid
from st_aggrid import *

from IPython.display import HTML, display
import re

from dog_food_analyzer_utils import *
from dog_food_analyzer_dictionaries import *

import numpy as np
import pandas as pd


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


#1st page
with intro:
    st.markdown("## What is this App for?")
    st.markdown(
"""
The Purpose of this App is as Follows:
1. Ingredient Quality Check: Checks the quality of each ingredient pasted by the user in the panel along with explanation
2. Major Energy Sources: Calculates the contribution of energy by each ingredient and classifies into "High", "Moderate", "Low" Energy contributors. The user can know majority of energy is coming from what "Type" of ingredient.
3. CO2 Emissions: Calculates the CO2 emission of each ingredient panel and based on careful assumption of proportions, provides the total CO2 emission value of the panel per 1000 kcal basis.
"""
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

    space, ingredient_col, space_1, diet_category_col, space_2 = st.columns([0.2, 3, 0.15, 2.5, 0.01])
    
#     with diet_category_col:
#         st.markdown('#### Select Food Category:')
#         diet_category = st.radio('Selected Category:', [
#                                 'Dry', 'Wet'], label_visibility='collapsed', horizontal=True)
    
    
    with ingredient_col:
        st.markdown('#### Enter Ingredient List:')
        ing_str = st.text_area('Enter Ingredient List:', height= 220,  label_visibility = 'collapsed', key='ia') 
        
        if ing_str == '':
            st.error('Please enter the ingredient list.')
            ing_str ='.'
            
            
        ing_result = preprocess_ingredients(ing_str)
        ing_result_df = pd.DataFrame(ing_result).T.reset_index().rename(columns={"index":"ingredient"})
        # st.write(ing_result)
        
        
    with diet_category_col:
#         st.markdown(ing_result)
    
        if len(ing_result) != 0:
            
            st.markdown(f'##### The Panel You Entered has {ing_result_df["Quality"].nunique()} Qualities of Ingredients:')
            selected_p_c = st.radio('Selected Category:', ing_result_df["Quality"].unique(), label_visibility = 'collapsed')
            
            st.markdown(f'##### Select the Type of Ingredients')
            selected_qt = st.radio('Selected Category:', list(ing_result_df[ing_result_df['Quality']==selected_p_c]['Type'].unique()), label_visibility = 'collapsed')
            
                
    with ingredient_col:
    
        if len(ing_result) != 0:
            
            st.markdown('#### Actual Ingredients in the Panel:')
            
#             if list(ing_result[selected_p_c].keys())[0] != 'Description':
            st.write(", ".join(list(ing_result_df[ing_result_df['Type']==selected_qt]['Ingredient'])))
#             else:
#                 st.write(', '.join(list(ing_result[selected_p_c].values())[1:]))
        
#             if list(ing_result[selected_p_c].values())[0] != '':
            st.markdown('#### Explanation:')
            st.markdown(f"{(ing_result_df[ing_result_df['Type']==selected_qt]['Quality Description'].unique()[0])}")
                
            
        
        
