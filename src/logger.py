
# coding: utf-8

# In[5]:

import pandas as pd
from PyQt4 import QtGui, QtCore
import matplotlib as mp
if mp.get_backend() == 'Qt5Agg':
    mp.use("Qt4Agg")

import matplotlib.pyplot as plt
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
            self._loggerlist.append(pd.DataFrame(columns =  ["x [m]", "velocity [m/s]", "lane", "acceleration [m/s2]"]))


    def addEntries(self):
        """ Goes through list of cars and adds values to data frame"""
        list = self._trafficManager.cars
        for i in xrange(0,len(list)):
            self._loggerlist[i] = self._loggerlist[i].append({'x [m]': list[i].getPosition(), 
                                                            'lane': list[i].getLane(), 
                                                            'velocity [m/s]' : list[i].getVelocity(), 
                                                            'acceleration [m/s2]' : list[i].getAcceleration()}, 
                                                             ignore_index = True)
            
    def getResult(self, numberInList):
        """ Returns result for each car object using the number of the car in the list"""
        return self._loggerlist[numberInList-1]
        
    
    def showSummaryPlots(self):
        """plots summary of current statistics"""
        variables = self._loggerlist[0].columns.values
        nCars = len(self._trafficManager.cars);
        fig, axes = plt.subplots(nrows = len(variables))
        for car in xrange(0,nCars):
            pltNumber = 0
            for variable in variables:       
                self._loggerlist[car][variable].plot(ax=axes[pltNumber])
                if variable == "lane":
                    axes[pltNumber].set_ylim(0,5)
                axes[pltNumber].set_ylabel(variable)
                pltNumber += 1
        plt.show()     
        




