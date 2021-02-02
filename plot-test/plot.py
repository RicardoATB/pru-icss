#!/usr/bin/python3.8

import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("flower.txt")

x, y = data.T
#plt.scatter(x,y)

plt.plot(*data.T)
plt.show()
