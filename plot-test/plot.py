#!/usr/bin/python3.8

import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("qnx.txt")

x, y = data.T

plt.plot(*data.T)
plt.gca().invert_yaxis()
plt.show()
