import random
class Fighter :
    def __init__(self, name, health, strength, armour, skill,mana):
        self.name = name
        self.health = health
        self.strength = strength
        self.armour = armour
        self.skill = skill
        self.mana = mana

        self.is_alive = True

    def attack(self, target):
        # Random Damage Dealt
        damage = self.strength + random.randint(-self.strength,self.strength)
        # Armour Defence
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
                    damage_dealt * 1.7
                print(f"{self.name} did a critical hit on {target.name} for {damage_dealt}!")
            else:
                # Normal attack
                target.health -= damage_dealt
                print(f"{self.name} attacked {target.name} for {damage_dealt}")

        print(f"{target.name} is now at {target.health}HP")

My_dude = Fighter("Rusty", 70, 25, 10, "Sword Dance", 10)
Bad_dude = Fighter("Mr.Necromancer", 125, 5, 5, "Skeleton Army", 200)

My_dude.attack(Bad_dude)