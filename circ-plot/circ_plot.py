#!/usr/bin/python3.8

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import math

def slope(x, y):
		if (x == 0 and y > 0):
			return 1
		elif (x == 0 and y < 0):
			return -1
		elif (x ==0 and y ==0):
			return 0
		else:
			return (y/x)

# Finding a point along a line a certain distance away from another point
# Math formula: https://math.stackexchange.com/questions/175896/finding-a-point-along-a-line-a-certain-distance-away-from-another-point
def comp_center_x(comp_y, x, y, q, m):
	if (q == 1 or q == 4):
		return (x + comp_y/(math.sqrt(1 + m*m)))
	if (q == 2 or q == 3):
		return (x - comp_y/(math.sqrt(1 + m*m)))

def int_angle_comp():
	 return math.atan((comp_x/2)/(comp_y/2))

# Calculate third point of a triangle given two points and angles
# Math formula: https://math.stackexchange.com/questions/1725790/calculate-third-point-of-triangle-from-two-points-and-angles
def comp_center_coord(x, y, comp_vert_x, comp_vert_y):
	#global x3, y3
	comp_center_pair = []
	offset_pair = []
	alp1 = alp2 = alpha
	alp3 = math.pi - 2*alpha
	x1 = x
	y1 = y
	x2 = comp_vert_x
	y2 = comp_vert_y
	u = x2-x1
	v = y2-y1
	a3 = math.sqrt(u*u + v*v)	
	a2 = a3 * math.sin(alp2)/math.sin(alp3)
	RHS1 = x1*u + y1*v + a2*a3*math.cos(alp1)
	RHS2 = y2*u - x2*v - a2*a3*math.sin(alp1)
	comp_center_pair.append((1/(a3*a3))*(u*RHS1 - v*RHS2))
	comp_center_pair.append((1/(a3*a3))*(v*RHS1 + u*RHS2))
	return comp_center_pair

# Ploting components (green rectangles)
def plot_component(q, x, y, angle):
	center_pair = []
	if (q == 1):
		m = slope(x, y)
		comp_vert_x = comp_center_x(comp_y, x, y, q, m)
		comp_vert_y = m*comp_vert_x
		center_pair = comp_center_coord(x, y, comp_vert_x, comp_vert_y)
		offset_x = center_pair[0]
		offset_y = center_pair[1]
		rect = plt.Rectangle((x - (offset_x -x), y - (offset_y - y)), comp_x, comp_y, angle, facecolor="none", ec="green", linewidth = 5)
		plt.gca().add_patch(rect)
	if (q == 2):
		m = slope(x, y)
		comp_vert_x = comp_center_x(comp_y, x, y, q, m)
		comp_vert_y = m*comp_vert_x
		center_pair = comp_center_coord(x, y, comp_vert_x, comp_vert_y)
		offset_x = center_pair[0]
		offset_y = center_pair[1]
		rect = plt.Rectangle((x - (offset_x -x), y - (offset_y - y)), comp_x, comp_y, angle, facecolor="none", ec="green", linewidth = 5)
		plt.gca().add_patch(rect)
	if (q == 3):
		m = slope(x, y)
		comp_vert_x = comp_center_x(comp_y, x, y, q, m)
		comp_vert_y = m*comp_vert_x
		center_pair = comp_center_coord(x, y, comp_vert_x, comp_vert_y)
		offset_x = center_pair[0]
		offset_y = center_pair[1]
		rect = plt.Rectangle((x - (offset_x -x), y - (offset_y - y)), comp_x, comp_y, angle, facecolor="none", ec="green", linewidth =5)
		plt.gca().add_patch(rect)
	if (q == 4):
		m = slope(x, y)
		comp_vert_x = comp_center_x(comp_y, x, y, q, m)
		comp_vert_y = m*comp_vert_x
		center_pair = comp_center_coord(x, y, comp_vert_x, comp_vert_y)
		offset_x = center_pair[0]
		offset_y = center_pair[1]
		rect = plt.Rectangle((x - (offset_x -x), y - (offset_y - y)), comp_x, comp_y, angle, facecolor="none", ec="green", linewidth = 5)
		plt.gca().add_patch(rect)

# ploting connected geometric shape (gray line)
def plot_graph():
	with open("vertices.txt") as f:
    	# skipping first comment row
		lines = (line for line in f if not line.startswith("#"))
		data = np.loadtxt(lines)
	x, y = data.T
	plt.plot(*data.T, linewidth=2, marker=".", markersize=30, markerfacecolor='gray', color = 'silver', zorder = 0)
	plt.axis('equal')
	plt.show()

# deleting last coordinate from "vertices.txt" (as it was just used to close the geometric shape w/ gray line)
def delete_last_coord():
	with open ("vertices.txt", "r+") as f:
		lines = f.readlines()
		lines_minus_last = lines[:-1] # skip last line (same coordinate as the first)
		f.seek(0) # set the pointer to the beginning of the file in order to rewrite the content
		f.truncate() # delete actual file content
		for item in lines_minus_last:
			f.write("{}".format(item))

def main():
	plt.figure(figsize=(30,30))
	internal_angles = []
	vert_angle = 360/num_vert
	tilt_angle = 0

	if (tilt == "y"):
		tilt_angle = 180 - 3*((180 - vert_angle)/2)
	
	# creating iterable list of all internal angles
	for i in range(0, num_vert+1):
		internal_angles.append(float(tilt_angle + i*vert_angle))

	with open ("vertices.txt", "w") as f_out:
		f_out.write("#  X       Y            Comment\n") # table header
		for i in internal_angles:
			# quadrant I
			if (i <= 90):
				x = radius * math.cos(np.deg2rad(i))
				y = radius * math.sin(np.deg2rad(i))
				angle = i - 90
				plot_component(1, x, y, angle)
			# quadrant II
			if (i > 90 and i<= 180):
				q2_i = 180 - i;
				x = -radius * math.cos(np.deg2rad(q2_i))
				y = radius * math.sin(np.deg2rad(q2_i))
				angle = 90 - q2_i
				plot_component(2, x, y, angle)
			# quadrant III
			if (i > 180 and i <= 270):
				q3_i = i - 180
				x = radius * math.cos(np.deg2rad(i))
				y = radius * math.sin(np.deg2rad(i))
				angle = -270 + q3_i
				plot_component(3, x, y, angle)
			# quadrant IV
			if (i > 270):
				x = radius * math.cos(np.deg2rad(i))
				y = radius * math.sin(np.deg2rad(i))
				angle = i - 90	
				plot_component(4, x, y, angle)
	
			f_out.write(str("{:>6.2f}".format(round(x,2))) + " \t" + str("{:>6.2f}".format(round(y,2))) \
			+ "\t# vertex " + str("{:>2.0f}".format(internal_angles.index(i)+1)) + \
			" @ " + str("{:>7.2f}".format(angle)) + str("\u00b0\n"))

	plot_graph()
	delete_last_coord()
	os.system("cat vertices.txt") # print list of coordinates and angles for each vertex

num_vert = int(input("Enter number of vertices of geometric placement: "))
comp_x = float(input("Enter component width footprint (mm): "))
comp_y = float(input("Enter component heigh footprint (mm): "))
radius = (float(input("Enter max diameter of components placement (mm): ")) - comp_y)/2
tilt = input("Bottom side flat to horizontal? (y/n): ")
alpha = int_angle_comp()

main()
