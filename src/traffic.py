import argparse
from singleton import Singleton

import plottraffic
from simplecar import SimpleCar

@Singleton
class TrafficManager:
    """TrafficManager class is in charge of intializing and implementing the traffic simulation"""
    def __init__(self):
        print "TrafficManager(): initializing traffic simulation"    
        self.cars = [SimpleCar(0), SimpleCar(20), SimpleCar(40), SimpleCar(80)]                 
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
            car.updatePosition(5)        

    def finalize(self):
        print "TrafficManager(): finalizing traffic simulation"




if __name__ == '__main__':

     
    trafficControl = TrafficManager.instance()
    plottraffic.initPlot(trafficControl)
 
    for step in range(1000):
        trafficControl.updateCars()
        plottraffic.updatePlot(trafficControl) 
        print "   "
        print "car positions at step %d:" % step
        for car in trafficControl.cars:
            print car.getPosition()
       

    trafficControl.finalize()
        
