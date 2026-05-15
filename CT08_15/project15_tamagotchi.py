class Fighter :
    def __init__(self, name, health, strength, armour, skill,mana):
        self.name = name
        self.health = health
        self.strength = strength
        self.armour = armour
        self.skill = skill
        self.mana = mana

        self.is_alive = True