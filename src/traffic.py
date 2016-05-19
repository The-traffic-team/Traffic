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

    def initialize(self,roadLength, positions, velocities):    
        print "TrafficManager(): initializing traffic simulation"    
        self.roadLength = roadLength
        basecar.BaseCar.ROADLENGTH = self.roadLength
        carTuples = []
        for i in range(len(positions)):         
            carTuples.append((positions[i], velocities[i]))  
        self.initCars(carTuples)

    def sortCars(self):
	lanelist = [[] for i in xrange(self._lanes)]
        for i in xrange(len(self.cars)):
		# Lanes start from 1 but list from 0
		lanelist[self.cars[i].getLane() - 1].append(self.cars[i])
	print lanelist
	# set Neighbours , use car number and remember that it starts with 1
	for laneNumber in xrange(1, self._lanes + 1):
		# Get list for each lane
		lane = lanelist[laneNumber -1]
		if(len(lane) > 1):
		# Sort lanes
			lane.sort(cmp = lambda x, y: cmp(x.getPosition(), y.getPosition()))
			print lane
			# Find next car for each lane
		        for carNumber in xrange(1, len(lane) + 1):
				if(carNumber  < len(lane)):
					nextNeighbourCar = lane[carNumber]
				else:
					nextNeighbourCar = lane[0]
				lane[carNumber -1].setNeighbour(nextNeighbourCar, laneNumber)

    def initCars(self, attributes):       
        attributes.sort()
        for attribute in attributes:
            self.cars.append(BetterCar(attribute[0], velocity = attribute[1]))
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
    positions = [0,200, 400, 600, 800, 1000, 1200, 1400, 1600, 2000] 
    velocities = [10,10,30,10,10,40,10,10,20,10]
     
    trafficControl = TrafficManager.instance()
    trafficControl.initialize(roadLength, positions, velocities)
    plotter = Plotter.instance()
    plotter.initPlot(trafficControl)
    logger = Logger.instance()
    logger.init(trafficControl)
    
    for step in range(500):

        trafficControl.updateCars()
        plotter.updatePlot()
        logger.addEntries()


       



    trafficControl.finalize()
        
    print logger.getResult(1)
    print
    print logger.getResult(2)
    logger.showSummaryPlots()

