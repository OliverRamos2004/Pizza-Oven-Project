import time

class Pizza:

    def __new__(cls, ingredients, name):
        try:
            assert "flour" in ingredients, "Missing flour"
            assert "cheese" in ingredients, "Missing cheese"
        except AssertionError as e:
            print(e)
            return None
        else:
            instance = super().__new__(cls)
            return instance

    def __init__(self, ingredients, name):
        self.ingredients = ingredients
        self.name = name

    def __str__(self):
        return f"This is a pizza made with {', '.join(self.ingredients)}."

    def __del__(self):
        print(f"The {self.name} pizza has been eradicated :(")

    def make(self):
        for ingredient in self.ingredients:
            print(f"\rAdding ingredient: {ingredient}", end=" ")
            time.sleep(1)

        print(f"\nThe {self.name} pizza is ready to be cooked!")
