
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

    def __init__(self,x=0,velocity=0,brakeDistance=-1,acceleration=0,maxAcceleration=0,maxDeceleration=0,maxSpeed=0, lane = int(1), lanes = int(4)):
        self._x = x
        self._velocity=velocity
        self._acceleration=maxAcceleration
        self._maxAcceleration = maxAcceleration
        self._maxDeceleration = maxDeceleration
        self._maxSpeed = maxSpeed
        self._brakeDistance = float(-1)
	# Count lanes from 1 but lists start from zero, keep in mind later
        self._lane = lane
	# Number of lanes needed to create lists of neighbours
	self._lanes = lanes
        self._previousNeighbour = [[] for i in xrange(self._lanes)]
        self._nextNeighbour = [[] for i in xrange(self._lanes)]
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

    def getLane(self):
	return self._lane    

    def getNextNeighbour(self):
	return self._nextNeighbour[self._lane -1]

    def setNeighbour(self, nextNeighbour, lane = 1):
        self._nextNeighbour[self._lane - 1]=nextNeighbour

    def saveNeighbourStatus(self):
        self._neighbourX=self._nextNeighbour[self._lane - 1].getPosition()
        self._neighbourV=self._nextNeighbour[self._lane - 1].getVelocity()
    
    def updatePosition(self):
        pass

