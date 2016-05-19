
# coding: utf-8

# In[5]:

import pandas as pd
from PyQt4 import QtGui, QtCore
import matplotlib as mp
mp.use("Qt4Agg")

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
        variables = self._loggerlist[0].columns.values
        nCars = len(self._trafficManager.cars);
        fig, axes = mp.pyplot.subplots(nrows = len(variables))
        for car in xrange(0,nCars):
            pltNumber = 0
            for variable in variables:       
                self._loggerlist[car][variable].plot(ax=axes[pltNumber])
                pltNumber += 1
        mp.pyplot.show()     
        




