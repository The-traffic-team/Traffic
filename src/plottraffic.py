# coding: utf-8

import matplotlib.pyplot as plt
from matplotlib import get_backend
from scipy.misc import imread
from singleton import Singleton

@Singleton
class Plotter:
    def __init__(self):
        self._backgroundImage = "../roadlanes.png"
        self._roadLength = 5e4
        self._roadWidth = self._roadLength  * 663./1657
	self._laneWidth = self._roadWidth / 4.
        self._trafficManager = None
        
    def initPlot(self, trafficManager ):
        self._trafficManager = trafficManager
        self._roadLength = self._trafficManager.roadLength
        self._roadWidth = self._roadLength  * 663./1657
	self._laneWidth = self._roadWidth / 4.
	plt.switch_backend('TkAgg')
	plt.figure(1)
	print "Matplotlib Backend ", get_backend()
	if(get_backend() == 'TkAgg'):
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
            y.append(self._laneWidth - (self._laneWidth/2.))
            # marker size s in pixels
        plt.scatter(x,y,zorder=1,s=500)
        plt.show(False)
        plt.draw()
        plt.pause(1e-60)
        plt.gcf().clear()
        

            
    def updatePlotnew(self):
        pass
        #drawnow(self.internalUpdatePlot)




