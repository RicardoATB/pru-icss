#!/usr/bin/python3.8

import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos
"""
# Must set figsize before plotting it
plt.figure(figsize=(30,30))

data = np.loadtxt("qnx.txt")

x, y = data.T

plt.plot(*data.T, linewidth=3)
#plt.gca().invert_yaxis()
plt.axis('equal')
plt.show()
"""

num_vert = int(input("Enter number of vertices: "))
radius = int(input("Enter maximum size (diameter): "))/2
print("\n")
vert_angle = 360/num_vert

# creating iterable list of all internal angles
int_angles = [i for i in range(0, 360) if i % vert_angle == 0]

for i in int_angles:
	print ("For angle ", i, ":")
	# quadrant 1
	if (i <= 90):
		x = radius * cos(np.deg2rad(i))
		y = radius * sin(np.deg2rad(i))
	# quadrant 2
	if (i <= 180 and i >90):
		q2_i = 90 - i;
		x = -radius * cos(np.deg2rad(q2_i))
		y = -radius * sin(np.deg2rad(q2_i))
	# quadrant 3
	if (i > 180 and i <= 270):
		q3_i = 180 - i
		x = radius * sin(np.deg2rad(i))
		y = radius * cos(np.deg2rad(i))
	# quadrant 4
	if (i > 270 and i <=360):
		x = radius * cos(np.deg2rad(i))
		y = radius * sin(np.deg2rad(i))
				

	print("x = ", round(x,2),", y = ", round(y,2),"\n")
