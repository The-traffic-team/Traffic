import numpy as np
from basecar import BaseCar

class BetterCar(BaseCar):
    """ A  car class, having lane chaning, inherits from BaseCar"""
    
    def __init__(self,x=0,velocity=1,brakeDistance=10,acceleration=15,maxAcceleration=0,maxDeceleration=0,maxSpeed=200,collide=True): 
	BaseCar.__init__(self)
        self._x=x  
        self._velocity=velocity
        self._acceleration=acceleration
        self._maxSpeed=maxSpeed
        self._driverMax=np.random.choice(range(self._maxSpeed/5,self._maxSpeed-10))
        self._driverMood = 0.01*np.random.choice(range(40,120,5))        
        self._color=np.random.choice('r,g,b,c,m,y,k'.split(','))
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
        else:
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
