import numpy as np
from basecar import BaseCar

class SimpleCar(BaseCar):
    """ A simple car class, inherits from BaseCar"""
    
    def __init__(self,x=0,velocity=1,brakeDistance=10,acceleration=20,maxAcceleration=0,maxDeceleration=0,maxSpeed=200,collide=True): 
	BaseCar.__init__(self)
        self._x=x  
        self._velocity=velocity
        self._maxSpeed=maxSpeed
        self._driverMax=np.random.choice(range(self._maxSpeed/5,self._maxSpeed-10))
        self._driverMood = 0.01*np.random.choice(range(60,120,5))        
        self._color=np.random.choice('r,g,b,c,m,y,k'.split(','))
        self._delay=0
        self._collide=collide
        self._acceleration=acceleration/self._driverMood
#        print self._driverMood
    def updatePosition(self,time):
        self._brakeDistance = self._driverMood*self._velocity*self._velocity/(2* self._acceleration)        #get current minimum breaking distance
        if(1):
            tempDist=self._neighbourX-self._x  #temporary distance between driver and neighbour in front
            if (tempDist<0):
                tempDist=self.ROADLENGTH+tempDist   #account for wrapping around
            if(self._collide):
                self.collision(tempDist,time)
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
                    
    def collision(self,tempDist,time):       
        if (tempDist+self._velocity*time<36):
            tempVel=self._neighbourV
            self.getNextNeighbour().setVelocity(self._velocity)
            self.getNextNeighbour().setPosition(min(self._neighbourX+20,self.getNextNeighbour().getNextNeighbour().getPosition()))
            self._velocity=tempVel/2
            self._acceleration=self._acceleration/2
            self._x=self._x
            self._delay=6
            self.getNextNeighbour().setDelay(1)
