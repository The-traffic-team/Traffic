
# coding: utf-8

# In[11]:

import matplotlib.pyplot as plt
from scipy.misc import imread
import numpy as np
#from drawnow import drawnow

#x = [1e4,2e4,3e4]
#y = np.ones(3)
#y *= 1500
#markercolor = ['r','g','b']

def initPlot( trafficManager ):
    fig = plt.figure()
    img = imread("../roadlanes.png")
    plt.imshow(img, zorder=0, extent=[0.0, trafficManager.roadLength*1e3, 0, 1e4])   
    

def updatePlot( trafficManager ):
    x=[]
    y=[]
    for car in trafficManager.cars:
        x.append(car.getPosition())
        y.append(1500)

    # marker size s in pixels
    plt.scatter(x,y,zorder=1,s=500) 
    plt.show()
    plt.pause(0.0001)






