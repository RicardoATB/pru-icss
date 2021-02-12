#!/usr/bin/python3.8

import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos

internal_angles = []
num_vert = int(input("Enter number of vertices: "))
radius = float(input("Enter maximum size (diameter): "))/2
vert_angle = 360/num_vert

# creating iterable list of all internal angles
#internal_angles = [i for i in range(0, 360) if i % vert_angle == 0]
for i in range(0, num_vert+1):
	internal_angles.insert(i, float(i*vert_angle))

with open ("coordinates.txt", "w") as f_out:
	for i in internal_angles:
		# quadrant I
		if (i <= 90):
			x = radius * cos(np.deg2rad(i))
			y = radius * sin(np.deg2rad(i))
			angle = i - 90
		# quadrant II
		if (i <= 180 and i > 90):
			q2_i = 180 - i;
			x = -radius * cos(np.deg2rad(q2_i))
			y = radius * sin(np.deg2rad(q2_i))
			angle = 90 - q2_i
		# quadrant III
		if (i > 180 and i <= 270):
			q3_i = i - 180
			x = radius * cos(np.deg2rad(i))
			y = radius * sin(np.deg2rad(i))
			angle = -270 + q3_i
		# quadrant IV
		if (i > 270 and i <= 360):
			x = radius * cos(np.deg2rad(i))
			y = radius * sin(np.deg2rad(i))
			angle = 180 - i	
	
		f_out.write(str("{:>5.2f}".format(round(x,2))) + " \t" + str("{:>5.2f}".format(round(y,2))) \
		+ "\t# vertex " + str(internal_angles.index(i)+1) + " @ " + str("{:>6.2f}".format(angle)) + str("\u00b0\n"))

# ploting geometric shape
# Must set figsize before plotting it
plt.figure(figsize=(30,30))
data = np.loadtxt("coordinates.txt")
x, y = data.T
plt.plot(*data.T, linewidth=3, marker=".", markersize=40, markerfacecolor='r')

# ploting components
"""
x1, y1 = [-1, 12], [1, 10]
x2, y2 = [-1, 10], [3, -1]
plt.plot(x1, y1, x2, y2, marker = "o")
"""

plt.axis('equal')
plt.show()
