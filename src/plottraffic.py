# coding: utf-8

import matplotlib.pyplot as plt
from scipy.misc import imread
from singleton import Singleton

@Singleton
class Plotter:
    def __init__(self):
        self._backgroundImage = "../roadlanes.png"
        self._roadLength = 5e4
        self._roadWidth = 1e4
        self._trafficManager = None
        
    def initPlot(self, trafficManager ):
        self._trafficManager = trafficManager
        self._roadLength = self._trafficManager.roadLength * 1e3
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        
        
    def updatePlot(self):

        img = imread("../roadlanes.png")
        plt.imshow(img, zorder=0, extent=[0.0, self._roadLength, 0, self._roadWidth])   
        # Lists for positions of cars
        x=[]
        y=[]
        for car in self._trafficManager.cars:
            x.append(car.getPosition())
            y.append(1500)
            # marker size s in pixels
        plt.scatter(x,y,zorder=1,s=500)
        plt.show(False)
        plt.draw()
        plt.gcf().clear()
        #plt.pause(0.005)

            
    def updatePlotnew(self):
        pass
        #drawnow(self.internalUpdatePlot)




