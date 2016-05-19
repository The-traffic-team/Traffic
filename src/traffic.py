import argparse

from singleton import Singleton
from pyqtgraph.Qt import QtGui, QtCore
from plottraffic import Plotter
import basecar
from logger import Logger
from simplecar import SimpleCar
from fastercar import FasterCar
from bettercar import BetterCar

@Singleton
class TrafficManager:
    """TrafficManager class is in charge of intializing and implementing the traffic simulation"""
    def __init__(self):
        self.cars = []        
        self.roadLength = 0        
        self._lanes = 4
	self._iterations = 1500

    def initialize(self,roadLength, positions, velocities,typeOfCar):    
        print "TrafficManager(): initializing traffic simulation"    
        self.roadLength = roadLength
        basecar.BaseCar.ROADLENGTH = self.roadLength
        carTuples = []
        for i in range(len(positions)):         
            carTuples.append((positions[i], velocities[i],typeOfCar[i]))  
        self.initCars(carTuples)

    def getIterations(self):
        return self._iterations

    def sortCars(self):         
	lanes = self.getLanes()
	for laneNumber in xrange(1, self._lanes + 1):
	    # Get list for each lane
            lane = lanes[laneNumber -1]
	    if(len(lane) > 1):
                # Sort lanes
	        lane.sort(cmp = lambda x, y: cmp(x.getPosition(), y.getPosition()))
		# Find next car for each lane
		for carNumber in xrange(1, len(lane) + 1):
		    if(carNumber  < len(lane)):
			nextNeighbourCar = lane[carNumber]
		    else:
			nextNeighbourCar = lane[0]
		    lane[carNumber -1].setNeighbour(nextNeighbourCar, laneNumber)                                
                                
    def getLanes(self):
        lanelist = [[] for i in xrange(self._lanes)]
        for i in xrange(len(self.cars)):
	    # Lanes start from 1 but list from 0
	    lanelist[self.cars[i].getLane() - 1].append(self.cars[i])
        return lanelist
                        
                                        
    def initCars(self, attributes):       
        attributes.sort()
        for attribute in attributes:
            if(attribute[2] == 's'):
                self.cars.append(SimpleCar(attribute[0], velocity = attribute[1], trafficManager=self))
            else:
                self.cars.append(BetterCar(attribute[0], velocity = attribute[1], trafficManager=self))               
        self.sortCars()

    
    def updateCars(self):
        for car in self.cars:
            car.saveNeighbourStatus()
        
        for car in self.cars:
            car.updatePosition(0.1)        

    def finalize(self):
        print "TrafficManager(): finalizing traffic simulation"




if __name__ == '__main__':

    roadLength = 5000
    positions =  [0  , 100 , 200 , 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 2000] 
    velocities = [10 , 50  , 10  , 35 , 30 , 25 , 10 , 15 , 30 , 45 , 40  , 25  ,  10 ,  20 , 10  , 30  ,  20 ,  35 ,   10]
    typeOfCar  = ['s', 'b' , 'b' , 'b','s' , 'b','b' , 's','s' , 'b', 'b' , 'b' , 'b' , 'b' , 's' , 'b' , 'b' , 'b' , 's' ]
     
    trafficControl = TrafficManager.instance()
    trafficControl.initialize(roadLength, positions, velocities, typeOfCar)
    plotter = Plotter.instance()
    plotter.initPlot(trafficControl)
    logger = Logger.instance()
    logger.init(trafficControl)
    
    for step in range(trafficControl.getIterations()):

        trafficControl.updateCars()
        plotter.updatePlot()
        logger.addEntries()


       



    trafficControl.finalize()
        
    print logger.getResult(1)
    print
    print logger.getResult(2)
    logger.showSummaryPlots()

