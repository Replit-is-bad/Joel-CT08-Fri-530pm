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
        damage = self.strength + random.randint(-self.strength,self.strength)
        damage_dealt = damage - target.armour
        if damage_dealt <= 0 :
            critical = random.randint(1 , 100)
            if critical > 80 :
                damage_dealt * 1.5
                print(f"{self.name} did a critical hit on {target.name}!")
            else:
                if damage_dealt >= 0:
                    target.health -= damage_dealt
                    print(f"{self.name} attacked {target.name} for {damage_dealt}")
                else:
                    damage_dealt == 0
                    print(f"{self.name} missed his attack!")

        print(f"{target.name} is now at {target.health}HP")

My_dude = Fighter("Rusty", 70, 25, 10, "Sword Dance", 10)
Bad_dude = Fighter("Mr.Necromancer", 125, 5, 5, "Skeleton Army", 200)

My_dude.attack(Bad_dude)