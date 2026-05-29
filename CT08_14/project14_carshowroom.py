import random
import time
class Fighter :

    def __init__(self, name, health, strength, armour, skill,mana):
        self.name = name
        self.health = health
        self.strength = strength
        self.armour = armour
        self.skill = skill
        self.mana = mana

        self.max_health = health
        self.max_mana = mana
        self.active_minion = None

        self.is_alive = True

    def attack(self, target):
        # Random Damage Dealt
        damage = random.randint(-5,self.strength)
        damage_dealt = damage - target.armour
        # Check if the damage is 0 or less than 0
        if damage_dealt <= 0 :
            # Damage dealt to 0 so it will not heal enemy
            damage_dealt == 0
            print(f"{self.name} missed his attack!")
        else:
            # Critical Hit Chance
            critical = random.randint(1 , 100)
            # 20% hit chance
            if critical > 80 :
                # Critical hit x 2 damage
                damage_dealt = damage_dealt * 2
                if damage_dealt <= self.strength:
                    damage_dealt * 2
                target.health -= damage_dealt
                print(f"{self.name} did a critical hit on {target.name} for {damage_dealt}!")
            else:
                # Normal attack
                target.health -= damage_dealt
                print(f"{self.name} attacked {target.name} for {damage_dealt}")
            if self.active_minion:
                self.active_minion.attack(target)
        if target.health <= 0:
            time.sleep(1)
            print(f"{target.name} was brutally destroyed by {self.name}")
        else:
            time.sleep(1)
            print(f"{target.name} is now at {target.health}HP")

    def use_skill(self, target):
        if self.skill == "Sword Dance" and self.mana >= 5 :
            self.mana -= 5
            self.strength *= 2
            time.sleep(1)
            print(f"{self.name} used Sword Dance to increase attck by 100%" )
        elif self.skill == "Summon Skeleton" and self.mana >= 65:
            self.mana -= 65
            self.active_minion = Minion("Skeleton", 5, 5)
            time.sleep(1)
            print(f"{self.name} used Summon Skeleton Minion to spawn one skeleton")
        else:
            time.sleep(1)
            print("Not enough mana")

    def rest(self):
        if self.health >= self.max_health:
            pass
        else:
            self.health += self.max_health * 0.2
        self.mana += self.mana * 0.2
        print(f"{self.name} rested")
        print(f"health and mana restored")

    def npc_turn(self, target):
        npc_choices = ["attack", "skill", "rest"]
        choice = random.choice(npc_choices)

        if self.health < 25 and self.health > 0:
            Bad_dude.rest()
        else:
            if choice == "attack":
                Bad_dude.attack(My_dude)
            elif choice == "skill":
                if self.mana < 65:
                    Bad_dude.attack(My_dude)


class Minion:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

        self.is_alive = True
        self.active_minion = None
    
    def attack(self, target):
        # Random Damage Dealt
        damage = random.randint(0,self.strength)
        damage_dealt = damage - target.armour
        # Check if the damage is 0 or less than 0
                # Normal attack
        target.health -= damage_dealt
        print(f"{self.name} attacked {target.name} for {damage_dealt}")

#MAIN CODE
My_dude = Fighter("Rusty", 70, 25, 10, "Sword Dance", 10)
Bad_dude = Fighter("Mr.Necromancer", 125, 5, 5, "Summon Skeleton", 200)

print(f"You have entered {Bad_dude.name}'s domain...")
time.sleep(2)
print("Prepare for battle!")
time.sleep(1)
round = 0
while My_dude.health > 0 and Bad_dude.health > 0: 
    round += 1

    round_message = f"Round {round}"
    print(round_message.center(20, "-"))
    time.sleep(1)
    print("1. attack")
    print("2. Skill")
    print("3. Rest")
    player_input = input("ENTER YOUR CHOICE: ")

    if player_input == "1":
        My_dude.attack(Bad_dude)
        Bad_dude.npc_turn(My_dude)
    elif player_input == "2":
        My_dude.use_skill(Bad_dude)
        Bad_dude.npc_turn(My_dude)
    elif player_input == "3":
        My_dude.rest
        Bad_dude.npc_turn(My_dude)
    
