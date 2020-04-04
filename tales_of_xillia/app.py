# Sprint 1 ->
    # Create Tales of Xillia characters :
        # a Character has 450 health points, are level 1 at the beginning and can be ko.

class Character:

    def __init__(self,name,health_point,level,isAlive):
        self.name = name
        self.health_point = health_point
        self.level = level
        self.isAlive =isAlive


Jude = Character("Jude", 450, 1, True)
Milla = Character("Milla", 450, 1, True)

print(f'Jude has {Jude.health_point} hps.')
print(f'Milla has {Milla.health_point} hps.')