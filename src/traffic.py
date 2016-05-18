import argparse
from singleton import Singleton
from plottraffic import Plotter
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
        baseCar.BaseCar.ROADLENGTH = self.roadlength
        carTuples = []
        for i in range(len(positions)):         
            carTuples.append(positions[i], velocities[i])  
        self.initCars(carTuples)

    def initCars(self, attributes):       
        attributes.sort()
        for attribute in attributes:
            self.cars.append(simpleCar(attributes[0], v=attributes[1]))
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
    positions = [0, 100, 200, 600] 
    velocities = [30 , 30, 30, 30]
     
    trafficControl = TrafficManager.instance()
    trafficControl.initialize(
    plotter = Plotter.instance()
    plotter.initPlot(trafficControl)
 
    for step in range(1000):
        trafficControl.updateCars()
        plotter.updatePlot()
        print "   "
        print "car positions at step %d:" % step
        for car in trafficControl.cars:
            print car.getPosition()
       

    trafficControl.finalize()
        
