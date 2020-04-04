# one piece class = creates characters

class Character():

   def __init__(self,weapon,name):
       self.weapon = weapon
       self.name = name

luffy = Character('Gum gum devil fruit','Monkey D Luffy')
zoro = Character('Santoryu style', 'Roronoa Zoro')

type(luffy)
type(zoro)

print(luffy.name)
print(zoro.name)


print('One Piece characters have been created.')
