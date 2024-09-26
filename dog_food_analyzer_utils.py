## There are two functions in the file
## The first function will create a json file having variables upto the Dog Exclusive Input section (The part where we take name, age, etc.)
## inputs from the user
## The second function will add the variables of remaining parts in the same json.

# importing libraries
import re
import pandas as pd

# importing utils files
import dog_food_analyzer_dictionaries
from dog_food_analyzer_dictionaries import *

import panel_dictionary
from panel_dictionary import panel_rule

from typing import Dict, Union

# Defining the main function that will clean and categorize ingredients
def preprocess_ingredients(ing_str):
    
    '''
    This function will clean and preprocess the ingredient panel and do the categorization of ingredients.
    Input: Ingredient Panel of the product
    Returns: Nested Dictionary and json file of {Category : {preprocessed ingredient name:ingredient name as entered}}
    '''
    try:
        # taking care of flavors
        if ": " in ing_str:
            ing_str_2 = ing_str.split(': ')[1].strip()
        else:
            ing_str_2 = ing_str

        ing_str_2 = re.sub(r"vitamins & minerals", "", ing_str_2, flags = re.IGNORECASE).strip()
        ing_str_2 = re.sub(r"\)\s*([a-zA-Z])", r"), \1", ing_str_2).strip()
        ing_str_2 = re.sub(r"\]\s*([a-zA-Z])", r"], \1", ing_str_2).strip()

        # creating a list of ingredients directly without preprocessing in order to highlight them properly.
        unprocessed_ing_list = ing_str_2.split(", ")

        # replacing vitamins and minerals keywords along with extra other keywords
        ing_str_3 = ing_str_2.lower().replace('vitamins', '').replace('minerals', '').replace('new:', '').replace('original:', '').replace('caloric content', '')

        # iteration for each category (cat wellness dry, dog raw food, etc.) of product to clean and preprocess the ingredient panel
        for cate, values in cleaning_dictionary.items():

            # converting each ingredient panel into string type
            # ingredients_list = [str(i) for i in ingr_list]

            # iterating for cleaning each ingredient string
            for unc, clean in values.items():
                ing_str_3 = ing_str_3.replace(unc, clean)

            # removing extra noises
            ing_str_4 = ing_str_3.replace('[', '')
            ing_str_5 = re.sub('\n', ' ', ing_str_4)
            ing_str_6 = re.sub(r'\s+', ' ', ing_str_5)
            ing_str_7 = re.sub('\xa0', '', ing_str_6).strip()

            for unc, clean in replace_dict.items():
                ing_str_7 = ing_str_7.replace(unc, clean)

            # splitting each ingredient from the ingredient string and storing it in list
            split_ingredients = ing_str_7.split(', ')

            # iterating each ingredient and removing useless parantheses
            ingredients_tokenized = []
            for each in split_ingredients:
                if '(' in each and ')' not in each:
                    s = each.replace('(', '')
                    ingredients_tokenized.append(s)
                elif ')' in each and '(' not in each:
                    s = each.replace(')', '')
                    ingredients_tokenized.append(s)
                else:
                    ingredients_tokenized.append(each)

            # removing tailing fullstops
            new_ingredients = []
            for each in ingredients_tokenized:
                if len(each) != 0 and each[-1] == '.':
                    item = each[:-1].strip()
                    new_ingredients.append(item)
                elif len(each) != 0 and each[0] == ':':
                    item = each[2:].strip()
                    new_ingredients.append(item)
                else:
                    new_ingredients.append(each)

            # removing extra noises from ingredients (Z68980, D80987, etc)
            # for this, splitting ingredients by fullstop
            new_ingredients_split = [each.split('.') for each in new_ingredients]

            # checking pattern of those noises and removing it
            new_ingredients_2 = []
            for each in new_ingredients_split:
                if len(each) == 2:
                    if len(each[1]) == 8 or len(each[1]) == 7:
                        new_ingredients_2.append(each[0].strip())
                    else:
                        new_ingredients_2.append(each)
                else:
                    new_ingredients_2.append(each)

            # Joining again with fullstops as that was the separator for splitting for previous step
            new_product_wise_ingredients = []
            for each in new_ingredients_2:
                if type(each) == list:
                    new_product_wise_ingredients.append(('.').join(each).lower().strip().replace("))", ")").replace("((", "(").strip())
                else:
                    new_product_wise_ingredients.append(each.lower().strip().replace("))", ")").replace("((", "(").strip())

            # converting the list of ingredient panel into dataframe to check if each
            # ingredient belongs to dictionary of standardized ingredients
            ingredients_dict_df = pd.DataFrame(new_product_wise_ingredients,
                                               columns=['Ingredient']).drop_duplicates()

            set_of_already_corrected_ingredient_names = set(
                ingredient_dictionary.keys())

            set_of_current_ingredients = set(
                ingredients_dict_df['Ingredient'].str.lower())

            remaining_set = (set_of_current_ingredients -
                             set_of_already_corrected_ingredient_names.intersection(set_of_current_ingredients))

            # this will break the loop if the remaining unmatched ingredient is nan or empty string
            if ('nan' in remaining_set and '' in remaining_set and len(remaining_set) <= 3) or\
                    (('nan' in remaining_set or '' in remaining_set) and len(remaining_set) == 1):

                break

        # Before we map the ingredients i.e. the preprocessed ingredient to the ingredient as entered, we need to some of the cleaning for that unprocessed ingredient as
        # well.
        # Inconsistent use of the parantheses in the data is to be removed.
        # unprocessed_ing_list_2 = []

    #         # iterating each ingredient and removing useless parantheses
    #         for each in unprocessed_ing_list:
    #             if '(' in each and ')' not in each:
    #                 s = each.replace('(', '')
    #                 unprocessed_ing_list_2.append(s)
    #             elif ')' in each and '(' not in each:
    #                 s = each.replace(')', '')
    #                 unprocessed_ing_list_2.append(s)
    #             else:
    #                 unprocessed_ing_list_2.append(each)

    #         # Inconsistent use of the square brackets in the data is to be removed.
    #         unprocessed_ing_list_3 = []

    #         # iterating each ingredient and removing useless parantheses
    #         for each in unprocessed_ing_list_2:
    #             if '[' in each and ']' not in each:
    #                 s = each.replace('[', '')
    #                 unprocessed_ing_list_3.append(s)
    #             elif ']' in each and '[' not in each:
    #                 s = each.replace(']', '')
    #                 unprocessed_ing_list_3.append(s)
    #             else:
    #                 unprocessed_ing_list_3.append(each)

        # removing tailing fullstops
        unprocessed_ing_list_2 = []
        for each in unprocessed_ing_list:
            if len(each) != 0 and each[-1] == '.':
                item = each[:-1].strip()
                unprocessed_ing_list_2.append(item)
            elif len(each) != 0 and each[0] == ':':
                item = each[2:].strip()
                unprocessed_ing_list_2.append(item)
            else:
                unprocessed_ing_list_2.append(each)

        # removing extra noises from ingredients (Z68980, D80987, etc)
        # for this, splitting ingredients by fullstop
        unprocessed_ing_split = [each.split('.') for each in unprocessed_ing_list_2]

        # checking pattern of those noises and removing it
        unprocessed_ing_list_5 = []
        for each in unprocessed_ing_split:
            if len(each) == 2:
                if len(each[1]) == 8 or len(each[1]) == 7:
                    unprocessed_ing_list_5.append(each[0].strip())
                else:
                    unprocessed_ing_list_5.append(each)
            else:
                unprocessed_ing_list_5.append(each)

        # Joining again with fullstops as that was the separator for splitting for previous step
        unprocessed_ing_list_6 = []
        for each in unprocessed_ing_list_5:
            if type(each) == list:
                unprocessed_ing_list_6.append(('.').join(each).strip().replace("))", ")").replace("((", "(").strip())
            else:
                unprocessed_ing_list_6.append(each.strip().replace("))", ")").replace("((", "(").strip())

        unprocessed_ing_list_7 = [re.sub(r"(vitamins|minerals)", "", each, flags=re.IGNORECASE).replace(":", "").strip() for each in unprocessed_ing_list_6]

        # mapping the ingredients with their parent category using ingredient dictionary and storing it in dictionary with its flavor
        mapping_dict = {k:v for k,v in zip(new_product_wise_ingredients, unprocessed_ing_list_7)}
        new_sorted_dict = {k: {**v, "Ingredient": mapping_dict[k]} for k, v in ingredient_dictionary.items() if k in mapping_dict}
        
    except Exception as err:
        print(err)
        new_sorted_dict = {"Error: ":"Please Enter Ingredients Properly!"}
        # Write the dictionary to a JSON file 
        # with open('json_output.json', 'w') as f:
        # # saving dictionary into json file
        #     json.dump(new_sorted_dict, f)

    return new_sorted_dict

def ingredients_pre(ing_str: str) -> Dict[str, Union[str, float, int, list]]:
    '''
    This function will clean and preprocess the ingredient panel and do the categorization of ingredients.
    Input: Ingredient Panel of the product, Diet category chosen by user - "Dry" or "Wet"

    Returns two dictionaries: The first dictionary is for dog's impact and the second dictionary is for categorization of ingredients.
    
    Example output of impact:
    {'highlighting_ingredients': ['Chicken Broth', 'Turkey', 'Pork Liver'],
     'co2_emission_from_ingredients_per_day': 36.06,
     'co2_emission_from_ingredients_per_year': 13160.52,
     'min_threshold': 22,
     'max_threshold': 42,
     'miles': 33745,
     'not_in_our_sub_category_list': []}
     
     Example output of ingredient analyzer
     {'Amino acids': {'Description': 'Essential building blocks of proteins important for muscle development and overall health in pets.',
      'l-lysine': 'L-Lysine',
      'taurine': 'Taurine'},
     'Animal products': {'Description': '',
      'chicken broth': 'Chicken Broth',
      'turkey': 'Turkey',
      'pork liver': 'Pork Liver',
      'chicken': 'Chicken'},
     'Fats and oils': {'Description': '', 'soybean oil': 'Soybean Oil'},
     .
     .
     .
     'Grains': {'Description': '', 'rice': 'Rice', 'rice starch': 'Rice Starch'}
    '''
    try:
        if ing_str in panel_rule:
            rule=panel_rule[ing_str]
        else:
            rule="NA"
        
        
        # taking care of flavors
        if ": " in ing_str:
            ing_str_2 = ing_str.split(': ')[1].strip()
        else:
            ing_str_2 = ing_str

        ing_str_2 = re.sub(r"vitamins & minerals", "", ing_str_2, flags = re.IGNORECASE).strip()
        ing_str_2 = re.sub(r"\)\s*([a-zA-Z])", r"), \1", ing_str_2).strip()
        ing_str_2 = re.sub(r"\]\s*([a-zA-Z])", r"], \1", ing_str_2).strip()
        

        # creating a list of ingredients directly without preprocessing in order to highlight them properly.
        unprocessed_ing_list = ing_str_2.split(", ")

        # replacing vitamins and minerals keywords along with extra other keywords
        ing_str_3 = ing_str_2.lower().replace('vitamnins.', 'vitamins').replace('vitamins', '').replace('minerals.', 'minerals').replace('fructo-oligo-saccharides', 'fructooligosaccharides').replace('new:', '').replace('original:', '').replace('caloric content', '')
        ing_str_3 = re.sub(r'\(\d+(\.\d+)?%\)', "", ing_str_3).strip()
        ing_str_3 = ing_str_3.replace("fats", "fat")

        # iteration for each category (cat wellness dry, dog raw food, etc.) of product to clean and preprocess the ingredient panel
        for cate, values in cleaning_dictionary.items():

            # converting each ingredient panel into string type
            # ingredients_list = [str(i) for i in ingr_list]

            # iterating for cleaning each ingredient string
            for unc, clean in values.items():
                ing_str_3 = ing_str_3.replace(unc, clean)

            # removing extra noises
            ing_str_4 = ing_str_3.replace('[', '')
            ing_str_5 = re.sub('\n', ' ', ing_str_4)
            ing_str_6 = re.sub(r'\s+', ' ', ing_str_5)
            ing_str_7 = re.sub('\xa0', '', ing_str_6).strip()

            for unc, clean in replace_dict.items():
                ing_str_7 = ing_str_7.replace(unc, clean)

            # splitting each ingredient from the ingredient string and storing it in list
            split_ingredients = ing_str_7.split(', ')

            # iterating each ingredient and removing useless parantheses
            ingredients_tokenized = []
            for each in split_ingredients:
                if '(' in each and ')' not in each:
                    s = each.replace('(', '')
                    ingredients_tokenized.append(s)
                elif ')' in each and '(' not in each:
                    s = each.replace(')', '')
                    ingredients_tokenized.append(s)
                else:
                    ingredients_tokenized.append(each)

            # removing tailing fullstops
            new_ingredients = []
            for each in ingredients_tokenized:
                if len(each) != 0 and each[-1] == '.':
                    item = each[:-1].strip()
                    new_ingredients.append(item)
                elif len(each) != 0 and each[0] == ':':
                    item = each[2:].strip()
                    new_ingredients.append(item)
                else:
                    new_ingredients.append(each)

            # removing extra noises from ingredients (Z68980, D80987, etc)
            # for this, splitting ingredients by fullstop
            new_ingredients_split = [each.split('.') for each in new_ingredients]

            # checking pattern of those noises and removing it
            new_ingredients_2 = []
            for each in new_ingredients_split:
                if len(each) == 2:
                    if len(each[1]) == 8 or len(each[1]) == 7:
                        new_ingredients_2.append(each[0].strip())
                    else:
                        new_ingredients_2.append(each)
                else:
                    new_ingredients_2.append(each)

            # Joining again with fullstops as that was the separator for splitting for previous step
            new_product_wise_ingredients = []
            for each in new_ingredients_2:
                if type(each) == list:
                    new_product_wise_ingredients.append(('.').join(each).lower().strip().replace("))", ")").replace("((", "(").strip())
                else:
                    new_product_wise_ingredients.append(each.lower().strip().replace("))", ")").replace("((", "(").strip())

            # converting the list of ingredient panel into dataframe to check if each
            # ingredient belongs to dictionary of standardized ingredients
            ingredients_dict_df = pd.DataFrame(new_product_wise_ingredients,
                                               columns=['Ingredient']).drop_duplicates()

            set_of_already_corrected_ingredient_names = set(
                ingredient_dictionary.keys())

            set_of_current_ingredients = set(
                ingredients_dict_df['Ingredient'].str.lower())

            remaining_set = (set_of_current_ingredients -
                             set_of_already_corrected_ingredient_names.intersection(set_of_current_ingredients))

            # this will break the loop if the remaining unmatched ingredient is nan or empty string
            if ('nan' in remaining_set and '' in remaining_set and len(remaining_set) <= 3) or\
                    (('nan' in remaining_set or '' in remaining_set) and len(remaining_set) == 1):

                break

        # removing tailing fullstops
        unprocessed_ing_list_2 = []
        for each in unprocessed_ing_list:
            if len(each) != 0 and each[-1] == '.':
                item = each[:-1].strip()
                unprocessed_ing_list_2.append(item)
            elif len(each) != 0 and each[0] == ':':
                item = each[2:].strip()
                unprocessed_ing_list_2.append(item)
            else:
                unprocessed_ing_list_2.append(each)

        # removing extra noises from ingredients (Z68980, D80987, etc)
        # for this, splitting ingredients by fullstop
        unprocessed_ing_split = [each.split('.') for each in unprocessed_ing_list_2]

        # checking pattern of those noises and removing it
        unprocessed_ing_list_5 = []
        for each in unprocessed_ing_split:
            if len(each) == 2:
                if len(each[1]) == 8 or len(each[1]) == 7:
                    unprocessed_ing_list_5.append(each[0].strip())
                else:
                    unprocessed_ing_list_5.append(each)
            else:
                unprocessed_ing_list_5.append(each)

        # Joining again with fullstops as that was the separator for splitting for previous step
        unprocessed_ing_list_6 = []
        for each in unprocessed_ing_list_5:
            if type(each) == list:
                unprocessed_ing_list_6.append(('.').join(each).strip().replace("))", ")").replace("((", "(").strip())
            else:
                unprocessed_ing_list_6.append(each.strip().replace("))", ")").replace("((", "(").strip())

        unprocessed_ing_list_7 = [re.sub(r"(vitamins|minerals)", "", each, flags=re.IGNORECASE).replace(":", "").strip() for each in unprocessed_ing_list_6]
        unprocessed_ing_list_f = []
        for each in unprocessed_ing_list_7:
            if each!="":
                unprocessed_ing_list_f.append(each)
        
        unprocessed_ing_list_8 = []
        for ingre in unprocessed_ing_list_7:
            if "(" in ingre and ")" not in ingre:
                ingre = ingre.replace(r"(", "")
            elif ")" in ingre and "(" not in ingre:
                ingre = ingre.replace(r")", "")
            elif "[" in ingre and "]" not in ingre:
                ingre = ingre.replace(r"[", "")
            elif "]" in ingre and "[" not in ingre:
                ingre = ingre.replace(r"]", "")
            elif "]" not in ingre and "[" not in ingre and ")" not in ingre and "(" not in ingre:
                ingre = ingre
            unprocessed_ing_list_8.append(ingre)
        
        d = {}
        for each in new_product_wise_ingredients:
            if each in set(ingredient_dictionary.keys()):
                parent_cat = ingredient_dictionary[each]["Type"]
                d[each] = parent_cat
            elif each not in set(ingredient_dictionary.keys()) and each!="":
                d[each] = "Undefined"
                
        # mapping the ingredients with their parent category using ingredient dictionary and storing it in dictionary with its flavor
        mapping_dict = {}
        if len(new_product_wise_ingredients) == len(unprocessed_ing_list_f):
            mapping_dict = {k:v for k,v in zip(new_product_wise_ingredients, unprocessed_ing_list_f)}
        else:
            mapping_dict = "Please Enter Ingredients Properly!"
            
        

        ingredients = list(mapping_dict.keys())

        n = len(ingredients)
        proportions = {ingredient: 0.0 for ingredient in ingredients}

        # Start assigning proportions
        base_proportion = 100 / n  # Initial equal distribution

        # Assigning proportions in a decreasing manner
        for i in range(n):
            proportions[ingredients[i]] = base_proportion * (n - i) / n  # Reduce proportion for each subsequent ingredient

        # Calculate the total assigned proportions
        total_assigned = sum(proportions.values())

        # If the total is less than 100, we need to adjust
        if total_assigned < 100:
            difference = 100 - total_assigned

            # Increase the last ingredient to balance the difference
            proportions[ingredients[-1]] += difference

        # Ensure all proportions are non-zero and decreasing
        for i in range(1, n):
            if proportions[ingredients[i]] >= proportions[ingredients[i - 1]]:
                proportions[ingredients[i]] = max(0, proportions[ingredients[i - 1]] - 0.01)  # Ensure it's less than the predecessor

        # Final adjustment to ensure they all add up to 100
        total_final = sum(proportions.values())

        # Normalize to ensure they sum to 100
        if total_final != 100:
            scale_factor = 100 / total_final
            for ingredient in proportions:
                proportions[ingredient] *= scale_factor

        # Round off the proportions to two decimal places
        for ingredient in proportions:
            proportions[ingredient] = round(proportions[ingredient], 2)
            
        
        return_dict = {k: {"Ingredient":mapping_dict[k], 
                           "Type":d[k], 
                           "Proportion":proportions[k],
                          "CO2":ingredient_dictionary[k]['emission'],
                          'sub':ingredient_dictionary[k]['sub_category']} for k in mapping_dict}
        
        e_dict = {}
        for each in return_dict.items():
            e_dict[each[0]] = [each[1]['Ingredient'], energy_contributions[each[1]['Type']]*(each[1]['Proportion']/100)]
            
        e_df = pd.DataFrame.from_dict(e_dict)
        e_df = e_df.T.reset_index().rename(columns={"index":"ing",
                                                    0:"Ingredient",
                                                    1:"KCAL"})
        e_df = e_df.sort_values(by='KCAL',
                               ascending=False)
        
        e_df['Emissions'] = [(return_dict[each]['Proportion']/100)*return_dict[each]['CO2'] for each in e_df['ing']]
        e_df['Emissions'] = [each*kcal/1000 for kcal, each in zip(e_df["KCAL"], e_df['Emissions'])]
        
        
#         em_dict = {}
#         for each in return_dict.items():
#             em_dict[each[0]] = each
        
    except Exception as err:
        co2_index = 0
        print(err)
        mapping_dict = {"Error: ":"Please Enter Ingredients Properly!"}
        return_dict = mapping_dict
        # Write the dictionary to a JSON file 
#         with open('json_output.json', 'w') as f:
#         # saving dictionary into json file
#             json.dump(return_dict, f, indent = 1)
    
    return e_df