#!/usr/bin/python3.8

import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos

num_vert = int(input("Enter number of vertices: "))
radius = int(input("Enter maximum size (diameter): "))/2
vert_angle = 360/num_vert

# creating iterable list of all internal angles
internal_angles = [i for i in range(0, 360) if i % vert_angle == 0]

with open ("coordinates.txt", "w") as f_out:
	for i in internal_angles:
		print ("\nFor angle ", i, ":")
		# quadrant 1
		if (i <= 90):
			x = radius * cos(np.deg2rad(i))
			y = radius * sin(np.deg2rad(i))
		# quadrant 2
		if (i <= 180 and i > 90):
			q2_i = 180 - i;
			x = -radius * cos(np.deg2rad(q2_i))
			y = radius * sin(np.deg2rad(q2_i))
		# quadrant 3
		if (i > 180 and i <= 270):
			q3_i = i - 180
			x = radius * cos(np.deg2rad(i))
			y = radius * sin(np.deg2rad(i))
		# quadrant 4
		if (i > 270 and i <= 360):
			x = radius * cos(np.deg2rad(i))
			y = radius * sin(np.deg2rad(i))		
		
		# saving first coordinate to be added later as the last
		if (internal_angles.index(i) == 0):
			first_x = x
			first_y = y	
	
		print("x = ", round(x,2),", y = ", round(y,2),"\n")
		f_out.write(str(round(x,2)) + " " + str(round(y,2)) + "\n")
		
		# if it's the last coordinate, append the value of the first one
		if (internal_angles.index(i) == (len(internal_angles) - 1)):
			f_out.write(str(round(first_x,2)) + " " + str(round(first_y,2)) + "\n")


# ploting
# Must set figsize before plotting it
plt.figure(figsize=(30,30))
data = np.loadtxt("coordinates.txt")
x, y = data.T
plt.plot(*data.T, linewidth=3)
#plt.gca().invert_yaxis()
plt.axis('equal')
plt.show()
