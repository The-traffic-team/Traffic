import numpy as np
from basecar import BaseCar

class SimpleCar(BaseCar):
    """ A simple car class, inherits from BaseCar"""
    
    def __init__(self,x=0,velocity=1,brakeDistance=-1,acceleration=0,maxAcceleration=0,maxDeceleration=0,maxSpeed=0): 
        self._x=x  
        self._velocity=velocity
        self._acceleration=acceleration
        self._brakeDistance = brakeDistance
        self._driverMax=np.random
    def updatePosition(self,time):
        self._x+=self._velocity*time
        self._velocity+=self._acceleration*time
        if(0):
            if ((self.neighbourX()-self._x)>self._brakeDistance):
                if((self._velocity+self._acceleration*time)<=self._maxSpeed):
                    self._velocity+=self._acceleration*time
                    self._x+=self._velocity*time
            else:    
                self._velocity-=self._acceleration*time
                self._x+=self._velocity*time
           
