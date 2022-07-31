"""
USAGE:
$ python nutrition.py

DESCRIPTION:
implement a program that prompts users to input a fruit (case-insensitively)
and then outputs the number of calories in one portion of that fruit,
per the FDA's poster for fruits, which is also available as text.
Capitalization aside, assume that users will input fruits exactly as written
in the poster (e.g., strawberries, not strawberry). Ignore any input that isn't a fruit.
- table: https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version

EXAMPLES:
$ python nutrition.py 
Item: apple
Calories: 130

$ python nutrition.py 
Item: APPle
Calories: 130

$ python nutrition.py
Item: Chocolate

$ python nutrition.py
Item: Banana
Calories: 110
"""

# Dictionary with fruits and calories
fruits = {"apple": 130, "avocado": 50, "banana":110, "cantaloupe":50, "grapefruit":60, "grapes":90, "honeydew melon":50, "kiwifruit":90, "lemon":15, "lime":20, "nectarine":60, "orange":80, "peach":60, "pear":100, "pineapple":50, "plums":70, "strawberries":50, "sweet cherries":100, "tangerine":50, "watermelon":80}
# request for the fruit name
user_item = input("Item: ")
user_item = user_item.lower()
# Check if in-list
# Return calories if exist, otherwise do nothing
if user_item in fruits:
    print(f"Calories: {fruits[user_item]}")