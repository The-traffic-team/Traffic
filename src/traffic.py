import argparse
import numpy as np

from singleton import Singleton
from pyqtgraph.Qt import QtGui, QtCore
from plottraffic import Plotter
import basecar
from logger import Logger
from simplecar import SimpleCar
from fastercar import FasterCar
from bettercar import BetterCar
from sound import SoundWorld
import numpy as np
from ambulancecar import AmbulanceCar

@Singleton
class TrafficManager:
    """TrafficManager class is in charge of intializing and implementing the traffic simulation"""
    def __init__(self):
        self.cars = []        
        self.roadLength = 0        
        self._lanes = 4
	self._iterations = 1500
	self._closedLane =  None
    
	

    def initialize(self,roadLength, positions, velocities,typeOfCar, iterations = 500, lanes = 4):    
        print "TrafficManager(): initializing traffic simulation"    
        self.roadLength = roadLength
        self._lanes = lanes          
        self._iterations = iterations
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
        hasCollision=False
        honkFlag=False
        for car in self.cars:
            car.saveNeighbourStatus()
        
        for car in self.cars:
            flags=car.updatePosition(0.1)
            if flags[0]:
                hasCollision=True
            if flags[1]:
                honkFlag=True
        return [hasCollision,honkFlag]    


    def finalize(self):
        print "TrafficManager(): finalizing traffic simulation"


def typeID( value ):
    if value > 0:
        return 'b'
    else:
        return 's'

if __name__ == '__main__':
    
    parser= argparse.ArgumentParser(description="Traffic simulator with configurable options")
    parser.add_argument( '-n', '--nCars', help="total number of cars to add", default = 20)
    #parser.add_argument( '-l', '--nLanes', help="total number of lanes available", default=4)
    parser.add_argument( '-L', '--roadLength', help="roadLength", default = 5000)
    parser.add_argument( '-s', '--percentSimple', help="percentage of simple cars", default = 0.2)
    parser.add_argument( '-i', '--iterations', help="iterations to run", default = 500)
    args = parser.parse_args()
    
    
    

    print float(args.percentSimple)
    roadLength = int(args.roadLength)
    nCars = int(args.nCars)
    nLanes = 4
    nSimple =  float(args.percentSimple)
    nSimple *= nCars
    nIter = int(args.iterations)
    if (roadLength <= 0)  or (nCars <= 0) or (nLanes <= 0) or (nLanes > 4) or (nSimple < 0) or (nSimple > nCars) or (nIter < 0):
        print "roadLength, number of Car, and number of lanes must all be more than 0!"
        print "percent simple cars must be between 0 and 1, number of lanes cannot exceed 4"
        exit(1)

    elif (roadLength*nLanes)/nCars < 10:
        print "Too many Cars for this size Road!"
        exit(2)
 

    positions =  [0  , 100 , 200 , 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 2000] 
    velocities = [10 , 50  , 10  , 35 , 30 , 25 , 10 , 15 , 30 , 45 , 40  , 25  ,  10 ,  20 , 10  , 30  ,  20 ,  35 ,   10]
    typeOfCar  = ['s', 'b' , 'b' , 'b','s' , 'b','b' , 's','s' , 'b', 'b' , 'b' , 'b' , 'b' , 's' , 'b' , 'b' , 'b' , 's' ]
    
    positions = range(0, roadLength, roadLength/nCars)
    velocities = [ np.random.randint(0,50) for i in range(0,nCars)]
    randLow = -1 * int(100 * float(args.percentSimple))
    randHigh = int(100 * (1 -float( args.percentSimple)))
    typeOfCar = [ typeID(np.random.randint(randLow, randHigh)) for i in range(0, nCars)] 
 
    trafficControl = TrafficManager.instance()
    trafficControl.initialize(roadLength, positions, velocities, typeOfCar, lanes=nLanes, iterations = nIter )
    plotter = Plotter.instance()
    plotter.initPlot(trafficControl)
    logger = Logger.instance()
    logger.init(trafficControl)
    soundWorld =SoundWorld()
    soundWorld.ambientSound()

    # decide randomly when ambulance car arrives
    arrivalOfAmbulance = int(trafficControl.getIterations() * np.random.rand() * 0.5 + 0.1 * trafficControl.getIterations())
    
    for step in range(trafficControl.getIterations()):
        flags=trafficControl.updateCars()
        isCollision=flags[0]
        honkFlag=flags[1]        
        if isCollision:
            soundWorld.crash()
        elif honkFlag:
            soundWorld.honk()

        if (step == arrivalOfAmbulance):
            AmbulanceCar(0,25, trafficManager=trafficControl)

            
        plotter.updatePlot()
        logger.addEntries()
	# after each step make sure that cars have  proper neighbour, will cost time, but increases accurancy
	trafficControl.sortCars()

       



    trafficControl.finalize()
        
    print logger.getResult(1)
    print
    print logger.getResult(2)
    logger.showSummaryPlots()

