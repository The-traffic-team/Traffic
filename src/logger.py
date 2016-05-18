
# coding: utf-8

# In[5]:

import pandas as pd

from singleton import Singleton
from basecar import BaseCar
from simplecar import SimpleCar

car2 = SimpleCar(x=10)
car3 = SimpleCar(x=2000, velocity= 100)
list = [BaseCar(), car2, car3]

@Singleton
class Logger:
    def __init__(self):
        """ Create an empty list, add data frames for each car object later"""
        self._loggerlist = []
    def initDataFrames(self,list):
        for i in xrange(0,len(list)):
            self._loggerlist.append(pd.DataFrame(columns =  ["x", "lane", "velocity"]))


    def addEntries(self, list):
        """ Goes through list of cars and adds values to data frame"""
        for i in xrange(0,len(list)):
            self._loggerlist[i] = self._loggerlist[i].append({'x': list[i].getPosition(), 'lane': 1}, ignore_index = True)
            
    def getResult(self, numberInList):
        """ Returns result for each car object using the number of the car in the list"""
        return self._loggerlist[numberInList-1]
    

logger = Logger.instance()

logger.initDataFrames(list)
logger.addEntries(list)

car2.updatePosition(10)
car3.updatePosition(10)
logger.addEntries(list)

print logger.getResult(1)
print
print logger.getResult(2)
print
print logger.getResult(3)

