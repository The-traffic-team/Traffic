import basecar

class SimpleCar(BaseCar):
    """ A simple car class, inherits from BaseCar"""

    def __init__(self,x=0,velocity=0,acceleration=0,maxAcceleration=0,maxDeceleration=0,maxSpeed=0,brakeDistance=-1): 
        self._x=x  
        self._velocity=velocity
         
