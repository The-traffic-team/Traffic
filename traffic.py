
# coding: utf-8

# In[ ]:

# Format guide
# Use camelcase for functions, classes and variables
# Start Class names with Uppercase
# Start functions and variables with lowercase
# Member variables have a single underscore in front

class Basecar:
    """ Base class for cars"""
    def __init__(self,x,acceleration,deceleration,maxspeed,distance):
        self._x = x
        self._acceleration = acceleration
        self._deceleration = deceleration
        self._maxspeed = maxspeed
        self._distance = distance
        self._previous = int()
        self._next = int()
        

        

