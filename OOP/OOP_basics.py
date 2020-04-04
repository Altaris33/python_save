#Author Jérémie LAERA
#This program shows basics of OOP uses

class MaxSizeList(object):
    def __init__(self, value):
        self.myList = []
        self.value = value

    def push(self, String):
        try:
            String = str(String)                   #casting String param to a string 
            self.myList.append(String)
        except ValueError:
            print('You can only push strings!')

    def getList(self):
        print(self.myList[-self.value:])

if __name__ == '__main__':
    first = MaxSizeList(7)
    second = MaxSizeList(1)

    first.push('I')
    first.push('Will')
    first.push('Build')
    first.push('An')
    first.push('Application.')
    first.push('Let\'s')
    first.push('Go')

    second.push('Alright')
    second.push('Go')


    first.getList()
    second.getList()
