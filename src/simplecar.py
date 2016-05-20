import numpy as np
from basecar import BaseCar

class SimpleCar(BaseCar):
    """ A simple car class, inherits from BaseCar"""
    
    def __init__(self,x=0,velocity=1,brakeDistance=10,acceleration=20,maxAcceleration=0,maxDeceleration=0,maxSpeed=200,collide=True, trafficManager = None): 
	BaseCar.__init__(self, trafficManager = trafficManager)
        self._x=x  
        self._velocity=velocity
        self._maxSpeed=maxSpeed
        self._driverMax=np.random.choice(range(self._maxSpeed/5,self._maxSpeed-10))
        self._driverMood = 0.007*np.random.choice(range(60,120,5))        
        self._color=np.random.choice('m,y,k'.split(','))
        self._delay=0
        self._collide=collide
        self._acceleration=acceleration/self._driverMood
        self._inacc=self._acceleration
	self._carType='s'

    def updatePosition(self,time):
        isCollision=False
        self._brakeDistance = self._driverMood*self._velocity*self._velocity/(2* self._inacc)        #get current minimum breaking distance
        tempDist=self._neighbourX-self._x  #temporary distance between driver and neighbour in front
        if (tempDist<0):
            tempDist=self.ROADLENGTH+tempDist   #account for wrapping around
        if(self._collide):
            isCollision=self.collision(tempDist,time)
        if self._delay>0:
            self._delay-=1
        elif (tempDist>self._brakeDistance):                             #accelerate if further than brake distance
            if((self._velocity+self._acceleration*time)<=self._driverMax):
                self._velocity+=self._acceleration*time
            isEndRoad=((self._x+self._velocity*time)>=self.ROADLENGTH)
            self._x+=self._velocity*time
            if isEndRoad:
                self._x=self._x%self.ROADLENGTH
        else:                                      #deccelerate if within brake distance
            if (self._velocity-self._acceleration*time>=0):
                self._velocity-=self._acceleration*time
                self._x+=self._velocity*time
                isEndRoad=((self._x+self._velocity*time)>=self.ROADLENGTH)
            else:                                   #safeguard negative velocities
                self._velocity=0
                isEndRoad=((self._x+self._velocity*time)>=self.ROADLENGTH)
            if isEndRoad:
                self._x=self._x%self.ROADLENGTH
        return isCollision
      
    def collision(self,tempDist,time):
        hasCollision=False
        if (tempDist+(self._velocity+self._acceleration*time)*time<25):
            hasCollision=True
            tempVel=self._neighbourV
            self.getNextNeighbour().setVelocity(self._velocity)
            self.getNextNeighbour().setPosition(min((self._neighbourX+15),(self.getNextNeighbour().getNextNeighbour().getPosition())-10))
            self._velocity=tempVel/3
            self._acceleration=self._acceleration/2
            self._x=self._x
            self._delay=5
            self.getNextNeighbour().setDelay(1)
        return hasCollision     
