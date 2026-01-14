"""
ccoking
"""
import json
# Dein Code kommt hier hin
def adjust_recipe(original_recipe, num_people):

    adjusted_ingredients = {}
    original_servings = original_recipe['servings']
    factor = num_people / original_servings

    for ingredient, amount in original_recipe['ingredients'].items():
        adjusted_ingredients[ingredient] = amount * factor

    adjusted_recipe = {
        'title': original_recipe['title'],
        'ingredients': adjusted_ingredients,
        'servings': num_people
    }
    return adjusted_recipe


def load_recipe(json_string):

    return json.loads(json_string)

if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, '
                   '"Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}')
    # Dein Code kommt hier hin
    print(load_recipe(recipe_json))
