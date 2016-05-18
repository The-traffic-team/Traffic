import basecar

class SimpleCar(BaseCar):
    """ A simple car class, inherits from BaseCar"""
    
    def __init__(self,x=0,velocity=0,brakeDistance=-1,acceleration=0,maxAcceleration=0,maxDeceleration=0,maxSpeed=0): 
        self._x=x  
        self._velocity=velocity
        self._brakeDistance = brakeDistance
        
    def updatePosition(self,time):
        self._x+=self._velocity*time
        if(0):
            if ((self.neighbourX()-self._x)>self._brakeDistance):
                if((self._velocity+self._acceleration*time)<=self._maxSpeed):
                    self._velocity+=self._acceleration*time
                    self._x+=self._velocity*time
            else:    
                self._velocity-=self._acceleration*time
                self._x+=self._velocity*time
           
