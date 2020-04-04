#Author: Jérémie LAERA
# This program shall use the notion of inheritance
# Python lloks up for method in following order: Instance attributes, class attributes and the ones from the base class

class Data(object):
    def getData(self):
        print('In data!')

class Time(Data):     #Inheriting from Data class
    def getTime(self):
        print('In Time!')

if __name__ == '__main__':
    data = Data()
    time = Time()

    data.getData()
    time.getTime()
    time.getData()     # Inheriting Data method                