
# coding: utf-8

# In[ ]:

# Format guide
# Use camelcase for functions, classes and variables
# Start Class names with Uppercase
# Start functions and variables with lowercase
# Member variables have a single underscore in front

class BaseCar(object):
    """ Base class for cars"""
    def __init__(self,x=0,velocity=0,brakeDistance=-1,acceleration=0,maxAcceleration=0,maxDeceleration=0,maxSpeed=0,):
        self._x = x
        self._velocity=velocity
        self._acceleration=acceleration
        self._maxAcceleration = acceleration
        self._maxDeceleration = deceleration
        self._maxSpeed = maxSpeed
        self._brakeDistance = float(-1)
        self._previous = int()
        self._nextNeighbour = BaseCar()
        self._lane = int(1)
        self._neighbourX=float()
        self._neighbourV=float()
     
        
        
    def getPosition(self,car):
        return self._x
    
    def getVelocity(self,car):
        return self._velocity
    

    def setNeighbour(self,nextNeighbour):
        self._nextNeighbour=nextNeighbour

    def saveNeighbourStatus(self):
        self._neighbourX=self._nextNeighbour.getPosition()
        self._neighbourV=self._nextNeighbour.getVelocity()
    
    def updatePosition(self):
        pass

