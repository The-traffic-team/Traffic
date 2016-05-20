import numpy as np
from basecar import BaseCar

class AmbulanceCar(BaseCar):
    """ An ambulance car which drives in its own lane, inherits from BaseCar"""
    
    def __init__(self,x=0,velocity=35,brakeDistance=10,acceleration=40,maxAcceleration=0,maxDeceleration=0,maxSpeed=250,collide=True, trafficManager = None): 
	BaseCar.__init__(self, trafficManager = trafficManager)
        # Start ambulance car in first half of road
        self._x=np.random.rand() * self.ROADLENGTH / 2.
        self._velocity=35
        self._maxSpeed=maxSpeed
        self._driverMax=maxSpeed
        self._driverMood = 0.004*np.random.choice(range(60,120,5))
        # Ambulance gets red color
        self._color='r'
        self._delay=0
        self._collide=collide
        self._acceleration=acceleration/self._driverMood
        self._inacc=self._acceleration
	self._carType='a'
	self._collisionHappened = 0
        # Decide on which lane in the middle of the road the ambulance occurs
        self._lane= np.random.randint(2,high=self._lanes)
        #Close lane in trafficManager after creation of ambulance car
        self._trafficManager._closedLane = self._lane
        # Remove other cars from same lane as ambulance
        laneToFree = self._trafficManager.getLanes()[self._lane - 1]
        for car in laneToFree:
            if(car != self):
                car._lane = car._lane + np.random.choice([-1,1])
        # Add ambulance car to traffic manager
        self._trafficManager.cars.append(self)
        # Sort cars so that each car knows it neighbour after lane is cleared
        self._trafficManager.sortCars()
        
    def updatePosition(self,time):
        self._brakeDistance = self._driverMood*self._velocity*self._velocity/(2* self._inacc)        #get current minimum breaking distance

        if((self._velocity+self._acceleration*time)<=self._driverMax):
            self._velocity+=self._acceleration*time
        isEndRoad=((self._x+self._velocity*time)>=self.ROADLENGTH)
        self._x+=self._velocity*time
        # Delete ambulance if end of road is reached
        if isEndRoad:
            # Free closed lane
            self._trafficManager._closedLane = None
            self._trafficManager.cars.remove(self)

        return [False, False]
      
    def collision(self,tempDist,time):
        return False
