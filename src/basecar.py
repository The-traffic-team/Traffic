
# coding: utf-8

# In[ ]:

# Format guide
# Use camelcase for functions, classes and variables
# Start Class names with Uppercase
# Start functions and variables with lowercase
# Member variables have a single underscore in front

class Basecar:
    """ Base class for cars"""
    def __init__(self,x,velocity,acceleration,maxAcceleration,maxDeceleration,maxSpeed,brakeDistance):
        self._x = x
        self._velocity=velocity
        self._acceleration=acceleration
        self._maxAcceleration = acceleration
        self._maxDeceleration = deceleration
        self._maxSpeed = maxSpeed
        self._brakeDistance = distance
        self._previous = int()
        self._next = int()
        self._lane = int(1)
     
        
        
    def getPosition(self):
        return self._x
        

    
