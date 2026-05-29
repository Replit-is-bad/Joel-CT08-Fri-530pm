import random

class Tamagotchi:

    def __init__(self,name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
        self.age = 0

    def status(self):
        print(f"1. {self.name}'s status")
        print(f"2. Hunger: {self.hunger}/100")
        print(f"3. Energy: {self.energy}/100")
        print(f"4. Happiness: {self.happiness}/100")
        print(f"5. Age: {self.age} days")

    def feed(self):
        print(f"\nYou Fed {self.name}.")
        self.hunger -= 15
        if self.hunger < 0 :
            self.hunger == 0
        if random.randint(-5, 10) >= 1:
            self.happiness -= 15
        else:
            self.happiness += 5
        if self.happiness < 0 :
            self.happiness == 0
            print(f"{self.name} is chronically depressesd and died of loneliness.")
            return True
    
    def play(self):
        print(f"\nYou played with {self.name}.")
        self.happiness += random.randint(10,15)
        self.hunger += random.randint(5,10)
        self.energy -= random.randint(5,15)

        if self.happiness > 100:
            self.happiness == 100
        if self.hunger > 100:
            self.hunger == 100
            print(f"{self.name} died of hunger.")
            return True
        if self.energy < 0:
            self.energy == 0
            print(f"{self.name} died of energy loss.")
            return True

    def sleep(self):
        print(f"\nYou put {self.name} to sleep.")
        self.energy += 25
        self.hunger += random.randint(20,35)

        if self.energy > 100:
            self.energy == 100
        if self.hunger > 100:
            self.hunger == 100
            print(f"{self.name} died of hunger.")
            return True

    def grow_older(self):
        self.age += 1

        if self.hunger > 100:
            self.hunger == 100
            print(f"{self.name} died of hunger.")
            return True
        if self.happiness < 0 :
            self.happiness == 0
            print(f"{self.name} is chronically depressesd and died of loneliness.")
            return True

        if self.age >= 15:
            print(f"{self.name} grew up and left you. You won!")
            return True

    def abuse(self):
        print(f"Choose a way to abuse {self.name}:")
        print("\n1. Smack")
        print("2. Shoot")
        print("3. Throw")
        print("4. Kill")
        choice = input("Input your abuse method: ")

    def smack(self):
        print(f"You smacked {self.name}.")
        self.happiness -= 30

        if self.happiness < 0 :
            self.happiness == 0

    def shoot(self):
        print("What weapons would you like to use?")
        print(f"\n1. Bow")
        print(f"2. Glock")
        print(f"3. AK-47")
        print(f"4. Darts")
        choice = input("Pick your weapon: ")
        print(f"\nYou almost killed {self.name} with a {choice}!")
        self.happiness -= 70

# Main code
name = input("What is your tamagotchi's name? ")
tamagotchi = Tamagotchi(name)
while True:
    
