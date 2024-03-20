# Parses the input string into wanted items and recipes
def parse_input(input_str):
    # Split input into parts for wanted items and recipes
    wanted_part, recipes_part = input_str.split("\n\n")
    # Extract wanted items
    wanted_items = wanted_part.split(": ")[1].split(", ")
    # Parse recipes into a dictionary
    recipes = {}
    for recipe in recipes_part.split("\n"):
        item, ingredients = recipe.split(" = ")
        recipes[item] = ingredients.split(" + ")
    return wanted_items, recipes

# Recursively finds the base ingredients for a given item
def get_all_ingredients(item, recipes, all_ingredients, add_item=True):
    # If the item is a base ingredient, add it to the set
    if add_item:
        all_ingredients.add(item)
    # Check if the item can be broken down
    if item in recipes:
        # Get all the ingredients for each ingredient
        for ingredient in recipes[item]:
            # Recursively call the function to get all the ingredients
            get_all_ingredients(ingredient, recipes, all_ingredients)  
    return all_ingredients

# Read input from a file
with open(r'day-3/day3_input.txt', 'r') as file:  # Corrected the file path
    input_str = file.read()

# Parse the input to get wanted items and recipes
wanted_items, recipes = parse_input(input_str)
# Set to store necessary base ingredients
necessary_ingredients = set()
# Find base ingredients for the first wanted item
get_all_ingredients(wanted_items[0], recipes, necessary_ingredients, False)

# Output the total number of base ingredients and what they are
print(len(necessary_ingredients), necessary_ingredients)

# Write the result to a file
with open(r'day-3/day3_result.txt', 'w') as file:  # Corrected the file path
    file.write(str(len(necessary_ingredients)) + '\n')  # Total count
    for ingredient in necessary_ingredients:
        file.write(ingredient + '\n')  # List each base ingredient
