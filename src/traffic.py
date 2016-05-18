import argparse

from singleton import Singleton
from plottraffic import Plotter
import basecar
from logger import Logger
from simplecar import SimpleCar


@Singleton
class TrafficManager:
    """TrafficManager class is in charge of intializing and implementing the traffic simulation"""
    def __init__(self):
        self.cars = []        
        self.roadLength = 0        

    def initialize(self,roadLength, positions, velocities):    
        print "TrafficManager(): initializing traffic simulation"    
        self.roadLength = roadLength
        basecar.BaseCar.ROADLENGTH = self.roadLength
        carTuples = []
        for i in range(len(positions)):         
            carTuples.append((positions[i], velocities[i]))  
        self.initCars(carTuples)

    def initCars(self, attributes):       
        attributes.sort()
        for attribute in attributes:
            self.cars.append(SimpleCar(attribute[0], velocity = attribute[1]))
        for i in range(len(self.cars) - 1):
            self.cars[i].setNeighbour(self.cars[i+1])
        self.cars[-1].setNeighbour(self.cars[0])
    
    def updateCars(self):
        for car in self.cars:
            car.saveNeighbourStatus()
        
        for car in self.cars:
            car.updatePosition(1)        

    def finalize(self):
        print "TrafficManager(): finalizing traffic simulation"




if __name__ == '__main__':

    roadLength = 1000
    positions = [0, 200, 800, 600] 
    velocities = [30 , 60, 30, 30]
     
    trafficControl = TrafficManager.instance()
    trafficControl.initialize(roadLength, positions, velocities)
    plotter = Plotter.instance()
    plotter.initPlot(trafficControl)
    logger = Logger.instance()
    logger.init(trafficControl)
    
    for step in range(500):
        trafficControl.updateCars()
        #plotter.updatePlot()
        logger.addEntries()


       

    trafficControl.finalize()
        
    print logger.getResult(1)
    print
    print logger.getResult(2)
    logger.showSummaryPlots()

