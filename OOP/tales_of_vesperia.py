# TALES OF VESPERIA OOP PYTHON PROGRAM

class Character():

    def __init__(self,name,attack,defense,agility,hp,pm):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.agility = agility
        self.hp = hp
        self.pm = pm

    def __str__(self):
        return f"{self.name} has {self.attack}, {self.defense}, {self.agility}, {self.hp}, {self.pm}"    
    
    def __del__(self):
        print("A character will be deleted if the del method is performed.")

    def weapon(self):
        raise NotImplementedError("Subclass must implement this abstract method")

    def artes(self, list_artes):
        raise NotImplementedError("Subclass must implement this abstract method")

    def reverse_name(self):
        raise NotImplementedError("Subclass must implement this abstract method")

# Specific characters
class Yuri(Character):

    def weapon(self):
        return f"{self.name} has a sword !"

    def artes(self,name,list_artes):
        return f"{self.name} has the following artes : {self.list_artes}"

class Repede(Character):

    def weapon(self):
        return f"{self.name} has a knife !"        

class Estelle(Character):

    def weapon(self):
        return f"{self.name} has a sword !"

    def artes(self,name,list_artes):
        return f"{self.name} has the following artes :{self.list_artes}"

    def reverse_name(self,name):
        return {self.name[::-1]}

yuri = Yuri('Yuri', 256, 178, 100, 850, 60)
yuri.weapon()     
print(yuri.weapon())