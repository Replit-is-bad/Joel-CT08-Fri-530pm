import random
class Animal : # naming convention PascalCase
    # Constructer
    def __init__(self, name, species, food, sound, height, weight):
        # Attributes
        self.name = name
        self.species = species
        self.food = food
        self.sound = sound
        self.height = height
        self.weight = weight

    def self_intro(self):
        print(f"I am {self.name} the {self.species}, I love to eat {self.food} , {self.sound}!")

    def eat_food(self):
        print(f"{self.name} is eating some {self.food}")

    def health_checkup(self):
        self.height += random.randint(1,10)
        self.weight += random.randint(1,5)
        print(f"{self.name} is {self.weight}kg and {self.height}cm")

# Main code
lion = Animal("Leo","Lion","Burgers","Meow",100,190)
rabbit = Animal("Sir Ribbit the 3rd, son of glog glog the 5th","Rabbit","Meat","Roar", 50, 8)

rabbit.self_intro()

rabbit.eat_food()