#Author: Jérémie LAERA
#This program illustrates the advanced concepts of inheritance
#Python looks up for method in following order: Instance attributes, class attributes and the
#from the base class
#mro: Method Resolution order

class Data(object):
    def __init__(self, data):
        self.data = data

    def getData(self):
        print(f'Data is: {self.data}')

class Time(Data):
    def getTime(self):
        print(f'Time is: {self.data}')

if __name__ == '__main__':
    data = Data(12)
    time = Time(26)                     #Inherited class -> value passed to __init__ of Data base class 

    data.getData()
    time.getTime()
    time.getData()

    #print()


