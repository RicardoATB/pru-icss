#!/usr/bin/python3.8

import matplotlib.pyplot as plt
import numpy as np

# Must set figsize before plotting it
plt.figure(figsize=(30,30))

data = np.loadtxt("qnx.txt")

x, y = data.T

plt.plot(*data.T)
plt.gca().invert_yaxis()
plt.axis('equal')
plt.show()
