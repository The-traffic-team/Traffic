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
        self._driverMood = 0.004*np.random.choice(range(60,120,5))        
        self._color=np.random.choice('m,y,k'.split(','))
        self._delay=0
        self._collide=collide
        self._acceleration=acceleration/self._driverMood
        self._inacc=self._acceleration
	self._carType='s'
	self._collisionHappened = 0

    def updatePosition(self,time):
        flags=[False,False]
        isCollision=False
        honkFlag=False
        self._brakeDistance = self._driverMood*self._velocity*self._velocity/(2* self._inacc)        #get current minimum breaking distance
        tempDist=self._neighbourX-self._x  #temporary distance between driver and neighbour in front
        if (tempDist<0):
            tempDist=self.ROADLENGTH+tempDist   #account for wrapping around
        if(self._collide):
            isCollision=self.collision(tempDist,time)
        if self._delay>0:
            self._delay-=1
        elif (tempDist-(self._velocity+self._acceleration*time)*time>self._brakeDistance):                             #accelerate if further than brake distance
            self._patience=10
            if((self._velocity+self._acceleration*time)<=self._driverMax):
                self._velocity+=self._acceleration*time
            isEndRoad=((self._x+self._velocity*time)>=self.ROADLENGTH)
            self._x+=self._velocity*time
            if isEndRoad:
                self._x=self._x%self.ROADLENGTH
                
        else:                                      #deccelerate if within brake distance
            if (self._velocity-self._acceleration*time>=0):
                self._patience-=1
                self._velocity-=self._acceleration*time
                self._x+=self._velocity*time
                isEndRoad=((self._x+self._velocity*time)>=self.ROADLENGTH)
            else:                                   #safeguard negative velocities
                self._patience-=1
                self._velocity=0
                isEndRoad=((self._x+self._velocity*time)>=self.ROADLENGTH)
            if isEndRoad:
                self._x=self._x%self.ROADLENGTH
            if self._patience<=0:
                honkFlag=True
                if not isCollision:
                     self.getNextNeighbour().setAcceleration(self.getNextNeighbour().getAcceleration()*1.05)
        flags[0]=isCollision
        flags[1]=honkFlag
        return flags
      
    def collision(self,tempDist,time):
        hasCollision=False
        if (tempDist-(self._velocity+self._acceleration*time)*time<35):
	    # Set red color for car if collision happened
	    self._collisionHappened = 10
            hasCollision=True
            tempVel=self._neighbourV
            self.getNextNeighbour().setVelocity(self._velocity)
            self.getNextNeighbour().setPosition(max(self._neighbourX+1,min((self._neighbourX+18),(self.getNextNeighbour().getNextNeighbour().getPosition())-18)))
            self._velocity=tempVel/2
            self._acceleration=0.8*self._acceleration
            self.getNextNeighbour().setAcceleration(self.getNextNeighbour().getAcceleration()*1.25)
            self._driverMax=self._driverMax*0.8
            self.getNextNeighbour().setDriverMax(self.getNextNeighbour().getDriverMax()*1.25)
            self._x=self._x
            self._delay=3
            self.getNextNeighbour().setDelay(1)
            
        return hasCollision     
