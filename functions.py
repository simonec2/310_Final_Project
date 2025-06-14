import urllib.parse, urllib.request, urllib.error, json
import pprint # Module that allows you print complicated data in a more readable way
import keys
import os
from urllib.request import Request


# Spoonacular API - 'https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+flour,+sugar&number=2'
# https://spoonacular.com/food-api/docs#Search-Recipes-by-Ingredients
# Parameters
#     ingredients (string) : A comma-separated list of ingredients that the recipes should contain.
#     number (number): The maximum number of recipes to return (between 1 and 100). Defaults to 10.
#     ranking (number): Whether to maximize used ingredients (1) or minimize missing ingredients (2) first.
#     ignorePantry (boolean): true

def get_recipe_data_safe(ingredients, results_number = 10, ignorePantry = True):

    try:
        params = {
            'ingredients': ingredients,
            'number': results_number,
            'ignorePantry': ignorePantry,
            'apiKey': keys.secret_api_key
        }

        paramstr = urllib.parse.urlencode(params)
        baseurl = 'https://api.spoonacular.com/recipes/findByIngredients'
        recipe_request = baseurl + '?' + paramstr
        print(recipe_request)

        recipes_str = urllib.request.urlopen(Request(recipe_request, headers={'User-Agent':'Project'})).read().decode('utf8')
        recipe_data = json.loads(recipes_str)

        return recipe_data

    except urllib.error.HTTPError as e:
        print(f'Error trying to retrieve data: {e}')
    except urllib.error.URLError as e:
        print(f'Error trying to retrieve data: {e}')
        return None

# recipe_print = get_recipe_data_safe('apples,flour,sugar')
# pprint.pprint(recipe_print)

# 'id' key is what will connect the two APIs, to get matching recipes
# id(number):	716429	-The id of the recipe.
# includeNutrition(boolean):	false	-Include nutrition data in the recipe information. Nutrition data is per serving. If you want the nutrition data for the entire recipe, just multiply by the number of servings.
# addWinePairing	boolean	false	Add a wine pairing to the recipe.
# addTasteData	boolean	false	Add taste data to the recipe.
def get_recipe_info_safe(id, includeNutrition = 'false', addWinePairing = 'false', addTasteData = 'false'):

    try:
        params = {
            'id': id,
            'includeNutrition': includeNutrition,
            'addWinePairing': addWinePairing,
            'addTasteData': addTasteData,
            'apiKey': keys.secret_api_key
        }

        paramstr = urllib.parse.urlencode(params)
        baseurl = 'https://api.spoonacular.com/recipes/' + str(id) + '/information'
        recipe_request = baseurl + '?' + paramstr
        print(recipe_request)

        recipes_str = urllib.request.urlopen(Request(recipe_request, headers={'User-Agent':'Project'})).read().decode('utf8')
        recipe_data = json.loads(recipes_str)

        pprint.pprint(recipe_data)
        return recipe_data

    except urllib.error.HTTPError as e:
        print(f'Error trying to retrieve data: {e}')
    except urllib.error.URLError as e:
        print(f'Error trying to retrieve data: {e}')
        return None

def update_saved_list(new_item):
    static_folder = os.path.join(os.path.dirname(__file__), 'static')
    file_path = os.path.join(static_folder, 'saved.txt')

    # Ensure the static directory exists
    os.makedirs(static_folder, exist_ok=True)

    # Read existing items (one per line)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            items = [line.strip() for line in f if line.strip()]
    else:
        items = []

    # Add the new item
    items.append(new_item)

    # Write the updated list back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        unique_list = list(set(items))
        for item in unique_list:
            f.write(f"{item}\n")


def read_saved_list():
    static_folder = os.path.join(os.path.dirname(__file__), 'static')
    file_path = os.path.join(static_folder, 'saved.txt')

    # Ensure the static directory exists
    os.makedirs(static_folder, exist_ok=True)

    # Read existing items (one per line)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            items = [line.strip() for line in f if line.strip()]
    else:
        items = []
    return items

# recipe_info_print = get_recipe_info_safe('716429')
# pprint.pprint(recipe_info_print)

# def get_recipe(ingredients, max_results):