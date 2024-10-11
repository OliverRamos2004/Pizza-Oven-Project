import time

class Oven:
    
    def __new__(cls, brand, dimensions, capacity=1):
        try:
            assert len(dimensions) == 3, "Incorrect dimensions"
        except AssertionError as e:
            print(e)
            return
        else:
            instance = super().__new__(cls)
            return instance

    def __init__(self, brand, dimensions, capacity=1):
        self.brand = brand
        self.dimensions = dimensions
        self.capacity = capacity
        self.door = False
        self.occupied = []

    def __str__(self):
        return f"This is an oven. The brand is {self.brand}."

    def __del__(self):
        print(f"The {self.brand} oven has been deleted")

    def open(self):
        self.door = True
        print("Door is open")
        time.sleep(1)

    def close(self):
        self.door = False
        print("Door is now closed")
        time.sleep(1)

    def put_in(self, *foods):
        try:
            assert self.door, "Please open the door first"
            assert (len(self.occupied) + len(foods)) <= self.capacity, "Oven cannot hold so many foods"
        except AssertionError as e:
            print(e)
        else:
            self.occupied.extend(foods)
            print(f"Put {', '.join([f.name for f in foods])} in the oven.")
            time.sleep(1)

    def take_out(self):
        try:
            assert self.door, "Please open the door"
            assert len(self.occupied) > 0, "Oven is empty!"
        except AssertionError as e:
            print(e)
        else:
            print(f"Taken out {', '.join([f.name for f in self.occupied])}")
            self.occupied = []

    def cook(self, time_in_minutes, temperature):
        try:
            assert len(self.occupied) > 0, "Oven is empty!"
        except AssertionError as e:
            print(e)
        else:
            print(f"Cooking at {temperature} degrees for {time_in_minutes} minutes...")
            time.sleep(time_in_minutes)
            print("Cooking done!")
