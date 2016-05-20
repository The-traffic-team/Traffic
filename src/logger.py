
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
        self._analysis = []
        self._trafficManager = None
  
        
    def init(self,TrafficManager):
        """ Give TrafficManager to have car list later"""
        self._trafficManager = TrafficManager
        self._roadLength = self._trafficManager.roadLength
        list = self._trafficManager.cars
        for i in xrange(0,len(list)):
            self._loggerlist.append(pd.DataFrame(columns =  ["x [m]", "velocity [m/s]", "lane", "acceleration [m/s2]"]))
            self._analysis.append(pd.DataFrame(columns = ["total distance [m]", "lane switches", "deviation from ideal speed [m/s]" ]))


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
        opacity = 0.96**(nCars)
        carList = self._trafficManager.cars
        analysisVars = self._analysis[0].columns.values
        for car in xrange(0,nCars):
            startPos =  self._loggerlist[car]['x [m]'][0]
            totalDist = 0
            lastPos = startPos
            lastLane = self._loggerlist[car]['lane'][0]
            laneChanges = 0
            idealSpeed = carList[car].getDriverMax()
            for stepnum in range(len(self._loggerlist[car]['x [m]'])):
                currentPos = self._loggerlist[car]['x [m]'][stepnum]
                
                if  currentPos > lastPos:
                    totalDist +=  currentPos - lastPos
                elif currentPos < lastPos:
                    totalDist += currentPos + self._roadLength - lastPos 
                else:
                    totalDist += 0
                lastPos = currentPos

                currentLane = self._loggerlist[car]['lane'][stepnum]
                if currentLane == lastLane:
                    laneChanges += 0
                else:
                    laneChanges += 1
                lastLane = currentLane
                
                speedDeviation =  self._loggerlist[car]['velocity [m/s]'][stepnum] - idealSpeed
                self._analysis[car] = self._analysis[car].append({'total distance [m]' : totalDist, 'lane switches' : laneChanges,
                                            'deviation from ideal speed [m/s]' : speedDeviation}, ignore_index = True)



        
        fig, axes = plt.subplots(nrows = len(variables))        
        
        for car in xrange(0,nCars):
            pltNumber = 0
            for variable in variables:       
                self._loggerlist[car][variable].plot(ax=axes[pltNumber], alpha=opacity)
                if variable == "lane":
                    axes[pltNumber].set_ylim(0,5)
                axes[pltNumber].set_ylabel(variable)
                pltNumber += 1
        
        plt.figure(1)
        fig, axes = plt.subplots(nrows = len(analysisVars))                    
        for car in xrange(0,nCars):
            pltNumber = 0
            for variable in analysisVars:
                self._analysis[car][variable].plot(ax=axes[pltNumber], alpha=opacity)
                axes[pltNumber].set_ylabel(variable)
                pltNumber += 1

        plt.show()     
        




