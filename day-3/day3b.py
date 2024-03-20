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
def get_base_ingredients(item, recipes, base_ingredients):
    if item in recipes:
        # If the item can be broken down, do so for each ingredient
        for ingredient in recipes[item]:
            get_base_ingredients(ingredient, recipes, base_ingredients)
    else:
        # If the item is a base ingredient, add it to the set
        base_ingredients.add(item)    
    return base_ingredients

# Read input from a file
with open(r'day-3/day3_input.txt', 'r') as file:  # Corrected the file path
    input_str = file.read()

# Parse the input to get wanted items and recipes
wanted_items, recipes = parse_input(input_str)
# Set to store necessary base ingredients
necessary_ingredients = set()
# Find base ingredients for the first wanted item
for i in range(len(wanted_items)):
    get_base_ingredients(wanted_items[i], recipes, necessary_ingredients)

# Output the total number of base ingredients and what they are
print(len(necessary_ingredients), necessary_ingredients)

# Write the result to a file
with open(r'day-3/day3b_result.txt', 'w') as file:  # Corrected the file path
    file.write(str(len(necessary_ingredients)) + '\n')  # Total count
    for ingredient in necessary_ingredients:
        file.write(ingredient + '\n')  # List each base ingredient
