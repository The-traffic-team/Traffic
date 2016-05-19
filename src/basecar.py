
# coding: utf-8

# In[ ]:

# Format guide
# Use camelcase for functions, classes and variables
# Start Class names with Uppercase
# Start functions and variables with lowercase
# Member variables have a single underscore in front

class BaseCar:
    """ Base class for cars"""
    ROADLENGTH=200

    def __init__(self,x=0,velocity=0,brakeDistance=-1,acceleration=0,maxAcceleration=0,maxDeceleration=0,maxSpeed=0):
        self._x = x
        self._velocity=velocity
        self._acceleration=maxAcceleration
        self._maxAcceleration = maxAcceleration
        self._maxDeceleration = maxDeceleration
        self._maxSpeed = maxSpeed
        self._brakeDistance = float(-1)
        self._previous = None
        self._nextNeighbour = None
        self._lane = int(1)
        self._neighbourX=float()
        self._neighbourV=float()
        self._delay=0
    def setPosition(self,newpos):
        self._x=newpos
    
    def setVelocity(self,newvelocity):
        self._velocity=newvelocity

    def setAcceleration(self,newacc):
        self._acceleration=newacc

    def setDelay(self,delay):
        self._delay=delay
        
    def getPosition(self):
        return self._x
    
    def getVelocity(self):
        return self._velocity

    def getAcceleration(self):
        return self._acceleration
    

    def setNeighbour(self,nextNeighbour):
        self._nextNeighbour=nextNeighbour

    def saveNeighbourStatus(self):
        self._neighbourX=self._nextNeighbour.getPosition()
        self._neighbourV=self._nextNeighbour.getVelocity()
    
    def updatePosition(self):
        pass

