import argparse

@Singleton
class TrafficManager:
    """TrafficManager class is in charge of intializing and implementing the traffic simulation"""
    def __init__(self)
        print "TrafficManager(): initializing traffic simulation"    
        self.cars = [SimpleCar(0), SimpleCar(20), SimpleCar(40), SimpleCar(80)]                 
        self.roadLength = 50
        self.initCars()

    def initCars():
        for i in range(len(self.cars) - 1):
            self.cars[i].setNeighbour(self.cars[i+1])
        self.cars[-1].setNeighbour(self.cars[0])
    
    def updateCars():
        for car in self.cars:
            car.saveState()
        
        for car in self.cars:
            car.update(1)        

    def finalize():
        print "TrafficManager(): finalizing traffic simulation"


if __name__ == '__main__':

    ` 
    trafficControl = TrafficManager().instance()
    initPlot(trafficControl)
 
    for step in range(10000):
        trafficControl.updateCars()
        plot(trafficControl.cars) 
        log(trafficControl.cars)    

    trafficControl.finalize()
        
