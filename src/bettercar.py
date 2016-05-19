import numpy as np
from basecar import BaseCar

class BetterCar(BaseCar):
    """ A  car class, having lane chaning, inherits from BaseCar"""
    
    def __init__(self,x=0,velocity=1,brakeDistance=10,acceleration=15,maxAcceleration=0,maxDeceleration=0,maxSpeed=200,collide=True, trafficManager = None): 
	BaseCar.__init__(self, trafficManager = trafficManager)
        self._x=x  
        self._velocity=velocity
        self._acceleration=acceleration
        self._maxSpeed=maxSpeed
        self._driverMax=np.random.choice(range(self._maxSpeed/5,self._maxSpeed-10))
        self._driverMood = 0.01*np.random.choice(range(40,120,5))        
        self._color=np.random.choice('r,g,b,c'.split(','))
        self._delay=0
        self._collide=collide
        self._lane=np.random.randint(1,high=self._lanes+1)

        
    def updatePosition(self,time):
        
        self._brakeDistance = self._driverMood*self._velocity*self._velocity/(2* self._acceleration)        #get current minimum breaking distance
        if(self.getNextNeighbour()):
            tempDist=self._neighbourX-self._x  #temporary distance between driver and neighbour in front
            if (tempDist<0):
                tempDist=self.ROADLENGTH+tempDist   #account for wrapping around
            if(self._collide):
                self.collision(tempDist,time)
            if self._delay>0:
                self._delay-=1
            elif (tempDist>self._brakeDistance):                             #accelerate if further than brake distance
                if not self.changeLane(tempDist,False):
                    if((self._velocity+self._acceleration*time)<=self._driverMax):
                        self._velocity+=self._acceleration*time
                isEndRoad=((self._x+self._velocity*time)>=self.ROADLENGTH)
                self._x+=self._velocity*time
                if isEndRoad:
                    self._x=self._x%self.ROADLENGTH
            else:                                      #deccelerate if within brake distance
                if not self.changeLane(tempDist):
                    if (self._velocity-self._acceleration*time>=0):
                        self._velocity-=self._acceleration*time
                        self._x+=self._velocity*time
                        
                    else:                                   #safeguard negative velocities
                        self._velocity=0
                isEndRoad=((self._x+self._velocity*time)>=self.ROADLENGTH)
                if isEndRoad:
                    self._x=self._x%self.ROADLENGTH
        else:
            if not self.changeLane(self.ROADLENGTH,False):
                if((self._velocity+self._acceleration*time)<=self._driverMax):
                    self._velocity+=self._acceleration*time
                isEndRoad=((self._x+self._velocity*time)>=self.ROADLENGTH)
                self._x+=self._velocity*time
                if isEndRoad:
                    self._x=self._x%self.ROADLENGTH
                    
    def collision(self,tempDist,time):       
        if (tempDist+self._velocity*time<30):
            tempVel=self._neighbourV
            self.getNextNeighbour().setVelocity(self._velocity)
            self.getNextNeighbour().setPosition(self._neighbourX+30)
            self._velocity=tempVel/5
            self._x=self._x-10
            self._delay=10
            self.getNextNeighbour().setDelay(3)

    def changeLane(self,tempDist,above = True):
        makeChange = False
        laneChangedTo = None
        if(above and self._lane < self._trafficManager._lanes):
            # self._lane means lane+1
            laneChangedTo = self._trafficManager.getLanes()[self._lane]
        if(not above and self._lane > 1):
            # self._lane means lane+1
            laneChangedTo = self._trafficManager.getLanes()[self._lane-2]
        if(laneChangedTo): 
            # Add us to the lane and check if enough distance is kept after sorting.
            laneChangedTo.append(self)
            laneChangedTo.sort(cmp = lambda x, y: cmp(x.getPosition(), y.getPosition()))
            indexOfCurrentCar = laneChangedTo.index(self)
            distanceNextCar = 0
            distancePreviousCar = 0
            if(indexOfCurrentCar > 0 and (indexOfCurrentCar < len(laneChangedTo) - 1)):
                distanceNextCar = laneChangedTo[indexOfCurrentCar + 1].getPosition() - self.getPosition()
                distancePreviousCar = self.getPosition() - laneChangedTo[indexOfCurrentCar - 1].getPosition()
                
            elif (indexOfCurrentCar > 0):
                distanceNextCar = self.ROADLENGTH - self.getPosition() + laneChangedTo[0].getPosition()
                distancePreviousCar = self.getPosition() - laneChangedTo[indexOfCurrentCar - 1].getPosition()
            elif (indexOfCurrentCar < len(laneChangedTo) - 1):
                distanceNextCar = laneChangedTo[indexOfCurrentCar + 1].getPosition() - self.getPosition()
                distancePreviousCar = self.getPosition() + self.ROADLENGTH - laneChangedTo[-1].getPosition()
            # Lane is empty, should never occur since laneChangeTo should be false
            else:
                distanceNextCar = self.ROADLENGTH
                distancePreviousCar = self.ROADLENGTH
            # Change lane to lane above if tempDist is less than distanceNextCar
            if(tempDist < distanceNextCar and tempDist < distancePreviousCar):
                makeChange = True
                if(above):          
                    self._lane += 1
                else:
                    self._lane -= 1
	    # Change lane to below also if lots of empty space in lane below 
	    elif (not above and self.ROADLENGTH * 0.25 < distanceNextCar and self.ROADLENGTH * 0.15 < distancePreviousCar):
		makeChange = True 
		self._lane -= 1
        # Change if lower lane is completly empty
        if (not laneChangedTo and not above and self._lane > 1):
            makeChange = True
            self._lane -= 1
        if(makeChange):
            self._trafficManager.sortCars()
            
        return makeChange
