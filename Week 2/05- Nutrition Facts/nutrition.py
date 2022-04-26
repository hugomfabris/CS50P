#First we ask for user's input, making it rid of spaces and turning case-insensitive
user_input = input("Item: ").strip().lower()
#Then we crate a dict with fruits as keys and calories as values
fruits = {
    'apple': 130,
    'avocado': 50,
    'banana': 110,
    'cantaloupe': 50,
    'grapefruit': 60,
    'grapes': 90,
    'honeydew melon': 50,
    'kiwifruit': 90,
    'lemon': 10,
    'lime': 20,
    'nextarine': 60,
    'orange': 80,
    'peach': 60,
    'pear': 100,
    'pineapple': 50,
    'plums': 70,
    'strawberries': 50,
    'sweet cherries': 100,
    'tangerine': 50,
    'watermelon': 80
}
#Finally, we print the result
if user_input in fruits:
    print(f"Calories: {fruits[user_input]}")

