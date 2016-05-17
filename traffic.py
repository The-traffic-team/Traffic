
# coding: utf-8

# In[ ]:

class basecar:
    """ Base class for cars"""
    def __init__(self,x,acceleration,deceleration,maxspeed,distance):
        self.x = x
        self.acceleration = acceleration
        self.deceleration = deceleration
        self.maxspeed = maxspeed
        self.distance = distance
        self.previous = int()
        self.next = int()
        

        

