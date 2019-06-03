class Adventurer:
    def __init__(self, hp, mp, attack, defense, name):
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.name = name
    
    def __str__(self):
        return "There are no strings on me"
    
    def speak(self):
        print(f"My name is {self.name} and I am a mighty warrior")