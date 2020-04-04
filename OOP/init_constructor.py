#Author: Jérémie LAERA
#This example shows the use of __init__ constructor

class Character():

    #__init__ -> constructor that stes values as soon as objects are created
    #__init__ -> is a keyword hence it has ti be named like it is
    def __init__(self):
        print('Calling init')
        self.pv = 350
        self.pm = 40
        self.phrase = 'New Character'

    def incrementPv(self):
        self.pv += 60

    def incrementPm(self):
        self.pm += 6   

    def catchphrase(self, phrase):
        self.phrase = 'Hey! I must be a genius!'     

Lloyd = Character()
Genis = Character()
Kratos = Character()
Colette = Character()
Raine = Character()
Sheena = Character()
Zelos = Character()
Presea = Character()
Regal = Character()

print(f'Lloyd initial PV are : {Lloyd.pv}')
print(f'Genis initial PV are : {Genis.pv}')
print(f'Kratos initial PV are : {Kratos.pv}')
print(f'Colette initial PV are : {Colette.pv}')
print(f'Raine initial PV are : {Raine.pv}')
print(f'Sheena initial PV are : {Sheena.pv}')
print(f'Zelos initial PV are : {Zelos.pv}')
print(f'Presea initial PV are : {Presea.pv}')
print(f'Regal initial PV are : {Regal.pv}')

Lloyd.incrementPv()
Lloyd.incrementPm()

print(f'After gaining PV and PM Lloyd has {Lloyd.pv} PV and {Lloyd.pm} PM.')
print('The others still have the same stats...')

