import argparse
from singleton import Singleton
from plottraffic import Plotter
from logger import Logger
from simplecar import SimpleCar


@Singleton
class TrafficManager:
    """TrafficManager class is in charge of intializing and implementing the traffic simulation"""
    def __init__(self):
        print "TrafficManager(): initializing traffic simulation"    
        self.cars = [SimpleCar(0), SimpleCar(x=2000,velocity=100), SimpleCar(x=4000,velocity=200), SimpleCar(x=8000,velocity=300)]                 
        self.roadLength = 50
        self.initCars()

    def initCars(self):
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

     
    trafficControl = TrafficManager.instance()
    plotter = Plotter.instance()
    plotter.initPlot(trafficControl)
    logger = Logger.instance()
    logger.init(trafficControl)
    
    for step in range(100):
        trafficControl.updateCars()
        plotter.updatePlot()
        logger.addEntries()
        print "   "
        print "car positions at step %d:" % step
        for car in trafficControl.cars:
            print car.getPosition()
       

    trafficControl.finalize()
        
print logger.getResult(1)
print
print logger.getResult(2)
