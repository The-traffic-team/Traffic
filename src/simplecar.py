import numpy as np
from basecar import BaseCar

class SimpleCar(BaseCar):
    """ A simple car class, inherits from BaseCar"""
    
    def __init__(self,x=0,velocity=1,brakeDistance=-1,acceleration=0,maxAcceleration=0,maxDeceleration=0,maxSpeed=200): 
        self._x=x  
        self._velocity=velocity
        self._acceleration=acceleration
        self._maxSpeed=maxSpeed
        self._driverMax=np.random.choice(range(self._maxSpeed/2,self._maxSpeed-10))
        self._brakeDistance = np.random.choice(range(0.8,1.2,0.05))*self._driverMax*self._driverMax/(2* self._acceleration)


    def updatePosition(self,time):
        if (self._x>=self.ROADLENGTH):
            self._x+=self._velocity*time
            self._x=self._x%self.ROADLENGTH
        else:
            self._x+=self._velocity*time
        
        self._velocity+=self._acceleration*time
        if(0):
             if ((self._x+self._velocity*time)>=self.ROADLENGTH):
                 self._x+=self._velocity*time
                 self._x=self._x%self.ROADLENGTH
             else:
                 self._x+=self._velocity*time
       
            tempDist=self.neighbourX()-self._x
            if (tempDist<0):
                tempDist=self.ROADLENGTH+tempDist
            if (tempDist>self._brakeDistance):
                if((self._velocity+self._acceleration*time)<=self._driverMax):
                    self._velocity+=self._acceleration*time
                    self._x+=self._velocity*time
            else:
                self._velocity-=self._acceleration*time
                self._x+=self._velocity*time
           
