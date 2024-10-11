from pizzaanswers import Pizza  # Import your Pizza class
from ovenanswer import Oven     # Import your Oven class

"""
Project: Pizza and Oven OOP Interaction

Description:
This script demonstrates Object-Oriented Programming (OOP) in Python by modeling a pizza and an oven. 
Users can create a pizza with specific ingredients and place it into an oven to cook. The pizza must 
contain specific required ingredients (like flour and cheese) to be valid.

Classes:
1. Pizza: Represents a pizza with a set of ingredients. It can be 'made' by simulating the addition of 
   ingredients one by one.
2. Oven: Represents an oven that can be opened, filled with food (pizza), closed, and used to cook the 
   items inside.

Instructions:
1. Ensure that `pizzaanswers.py` and `ovenanswer.py` are in the same directory as this script.
2. Run the script `CookPizzaOven.py` to simulate creating a pizza and cooking it in an oven.

Usage:
- A pizza is created with a set of ingredients. If it contains the necessary ingredients (flour and cheese), 
  the script continues to simulate preparing the pizza.
- The oven is then opened, the pizza is placed inside, and the oven is closed.
- The pizza is cooked for a specified amount of time and at a set temperature.
- Once cooking is complete, the pizza is removed from the oven.

Example Usage:
    # Creating a pizza
    ingredients = ["flour", "cheese", "tomato sauce", "pepperoni"]
    my_pizza = Pizza(ingredients, "Pepperoni Pizza")

    # Opening the oven and placing the pizza inside
    my_oven = Oven(brand="Whirlpool", dimensions=[20, 20, 20], capacity=1)
    my_oven.open()
    my_oven.put_in(my_pizza)
    my_oven.close()

    # Cooking the pizza at 400 degrees for 3 minutes
    my_oven.cook(time_in_minutes=3, temperature=400)

    # Taking the pizza out
    my_oven.open()
    my_oven.take_out()

Notes:
- Ensure the oven is open before putting in or taking out the pizza.
- Make sure that the pizza has flour and cheese as ingredients; otherwise, it will not be created.
- The cooking time in this script is shortened for testing purposes. Adjust as necessary.

Author: [Oliver Ramos]
"""


# Create a Pizza object
ingredients = ["flour", "cheese", "tomato sauce", "pepperoni"]
my_pizza = Pizza(ingredients, "Pepperoni Pizza")

# Check if pizza creation succeeded (i.e., it has flour and cheese)
if my_pizza is not None:
    print(my_pizza)  # Print the pizza description
    my_pizza.make()  # Simulate making the pizza

    # Create an Oven object
    my_oven = Oven(brand="Whirlpool", dimensions=[20, 20, 20], capacity=1)

    # Open the oven, put the pizza in, and close it
    my_oven.open()
    my_oven.put_in(my_pizza)
    my_oven.close()

    # Cook the pizza at 400 degrees for 3 seconds (as a test)
    my_oven.cook(time_in_minutes=3, temperature=400)

    # Open the oven and take out the pizza
    my_oven.open()
    my_oven.take_out()
else:
    print("Pizza creation failed. Missing key ingredients.")
