
# coding: utf-8

# In[11]:

import matplotlib.pyplot as plt
from scipy.misc import imread
import numpy as np

x = [1e4,2e4,3e4]
y = np.ones(3)
y *= 1500
markercolor = ['r','g','b']

img = imread("roadlanes.png")
# marker size s in pixels
plt.scatter(x,y,zorder=1,s=500, c = markercolor) 
plt.imshow(img, zorder=0, extent=[0.0, 5e4, 0, 1e4])
plt.show()


# In[ ]:



