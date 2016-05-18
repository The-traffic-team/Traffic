
# coding: utf-8

# In[5]:

import pandas as pd
from singleton import Singleton


@Singleton
class Logger:
    def __init__(self):
        """ Create an empty list, add data frames for each car object later"""
        self._loggerlist = []
        self._trafficManager = None
        
    def init(self,TrafficManager):
        """ Give TrafficManager to have car list later"""
        self._trafficManager = TrafficManager
        list = self._trafficManager.cars
        for i in xrange(0,len(list)):
            self._loggerlist.append(pd.DataFrame(columns =  ["x", "lane", "velocity"]))


    def addEntries(self):
        """ Goes through list of cars and adds values to data frame"""
        list = self._trafficManager.cars
        for i in xrange(0,len(list)):
            self._loggerlist[i] = self._loggerlist[i].append({'x': list[i].getPosition(), 'lane': 1}, ignore_index = True)
            
    def getResult(self, numberInList):
        """ Returns result for each car object using the number of the car in the list"""
        return self._loggerlist[numberInList-1]
        
    
    def showSummaryPlots(self):
        """plots summary of current statistics"""
        self._loggerlist[0]
                    





