#!/usr/bin/python3.8

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
from math import sin, cos, sqrt

def slope(x, y, q):
	if (q == 1 or q == 3):
		return (y/x)
	if (q == 2 or q == 4):
		return (y/x)

def comp_center_x(comp_y, x, y, q, m):
	if (q == 1 or q == 4):
		return (x + comp_y/(sqrt(1 + m*m)))
	if (q == 2 or q == 3):
		return (x - comp_y/(sqrt(1 + m*m)))

def plot_component(q, comp_x, comp_y, x, y, angle):
	# ploting components
	if (q == 1):
		m = slope(x, y, q)
		x_offset = comp_center_x(comp_y, x, y, q, m)
		y_offset = m*x_offset
		plt.plot(x_offset, y_offset, 'o', color='black', markersize = 20, markerfacecolor = 'g');
		rect = plt.Rectangle((x,y), comp_x, comp_y, angle, fc='blue', ec="red")
		plt.gca().add_patch(rect)
	if (q == 2):
		m = slope(x, y, q)
		x_offset = comp_center_x(comp_y, x, y, q, m)
		y_offset = m*x_offset
		plt.plot(x_offset, y_offset, 'o', color='black', markersize = 20, markerfacecolor = 'g');
		rect = plt.Rectangle((x,y), comp_x, comp_y, angle, fc='blue', ec="red")
		plt.gca().add_patch(rect)
	if (q == 3):
		m = slope(x, y, q)
		x_offset = comp_center_x(comp_y, x, y, q, m)
		y_offset = m*x_offset
		plt.plot(x_offset, y_offset, 'o', color='black', markersize = 20, markerfacecolor = 'g');
		rect = plt.Rectangle((x,y), comp_x, comp_y, angle, fc='blue', ec="red")
		plt.gca().add_patch(rect)
	if (q == 4):
		m = slope(x, y, q)
		x_offset = comp_center_x(comp_y, x, y, q, m)
		y_offset = m*x_offset
		plt.plot(x_offset, y_offset, 'o', color='black', markersize = 20, markerfacecolor = 'g');
		rect = plt.Rectangle((x,y), comp_x, comp_y, angle, fc='blue', ec="red")
		plt.gca().add_patch(rect)

def plot_graph():
	# ploting geometric shape
	# Must set figsize before plotting it
	data = np.loadtxt("temp.txt")
	x, y = data.T
	plt.plot(*data.T, linewidth=3, marker=".", markersize=40, markerfacecolor='r')

	# deleting last coordinate from "coordinates.txt" (as it was just used to close the shape)
	with open ("temp.txt") as f_in, open ("vertices.txt", "w") as f_out:
		lines = f_in.readlines()
		lines = lines[:-1]
		#f_out.seek(0)	# set the pointer to the beginning of the file in order to rewrite the content
		for item in lines:
			f_out.write("{}".format(item))
	os.remove("temp.txt")

	plt.axis('equal')
	plt.show()

def main():
	plt.figure(figsize=(30,30))
	internal_angles = []
	num_vert = int(input("Enter number of vertices: "))
	radius = float(input("Enter maximum size (diameter): "))/2
	comp_x = float(input("Enter component width (x): "))
	comp_y = float(input("Enter component heigh (y): "))
	vert_angle = 360/num_vert

	# creating iterable list of all internal angles
	for i in range(0, num_vert+1):
		internal_angles.insert(i, float(i*vert_angle))

	with open ("temp.txt", "w") as f_out:
		for i in internal_angles:
			# quadrant I
			if (i <= 90):
				x = radius * cos(np.deg2rad(i))
				y = radius * sin(np.deg2rad(i))
				angle = i - 90
				plot_component(1, comp_x, comp_y, x, y, angle)
			# quadrant II
			if (i <= 180 and i > 90):
				q2_i = 180 - i;
				x = -radius * cos(np.deg2rad(q2_i))
				y = radius * sin(np.deg2rad(q2_i))
				angle = 90 - q2_i
				plot_component(2, comp_x, comp_y, x, y, angle)
			# quadrant III
			if (i > 180 and i <= 270):
				q3_i = i - 180
				x = radius * cos(np.deg2rad(i))
				y = radius * sin(np.deg2rad(i))
				angle = -270 + q3_i
				plot_component(3, comp_x, comp_y, x, y, angle)
			# quadrant IV
			if (i > 270 and i <= 360):
				x = radius * cos(np.deg2rad(i))
				y = radius * sin(np.deg2rad(i))
				angle = i - 90	
				plot_component(4, comp_x, comp_y, x, y, angle)
	
			f_out.write(str("{:>5.2f}".format(round(x,2))) + " \t" + str("{:>5.2f}".format(round(y,2))) \
			+ "\t# vertex " + str(internal_angles.index(i)+1) + " @ " + str("{:>7.2f}".format(angle)) + str("\u00b0\n"))

	plot_graph()

main()
