#!/usr/bin/python3.8

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
#from math import sin, cos, sqrt, atan, pi
import math


def slope(x, y, q):
	if (q == 1 or q == 3):
		return (y/x)
	if (q == 2 or q == 4):
		return (y/x)

def comp_center_x(comp_y, x, y, q, m):
	if (q == 1 or q == 4):
		return (x + comp_y/(math.sqrt(1 + m*m)))
	if (q == 2 or q == 3):
		return (x - comp_y/(math.sqrt(1 + m*m)))

"""
x1=0;y1=0;x2=6;y2=0; % initial data
alp1=2*pi/3;alp2=pi/6; % initial data
u=x2-x1;v=y2-y1;a3=sqrt(u^2+v^2);
alp3=pi-alp1-alp2;
a2=a3*sin(alp2)/sin(alp3);
RHS1=x1*u+y1*v+a2*a3*cos(alp1);
RHS2=y2*u-x2*v-a2*a3*sin(alp1);
x3=(1/a3^2)*(u*RHS1-v*RHS2);
y3=(1/a3^2)*(v*RHS1+u*RHS2);
"""

x3 = y3 = 0

def int_angle_comp():
	 return math.atan((comp_x/2)/(comp_y/2))

def comp_center_coord(x, y, comp_vert_x, comp_vert_y):
	global x3, y3
	offset_pair = []
	alp1 = alp2 = alpha
	alp3 = math.pi - 2*alpha
	x1 = x
	y1 = y
	x2 = comp_vert_x
	y2 = comp_vert_y
	#x1=0;y1=0;x2=6;y2=0		 			# initial data
	#alp1=2*pi/3;alp2=pi/6				# initial data
	u = x2-x1
	v = y2-y1
	a3 = math.sqrt(u*u + v*v)	
	#alp3=pi-alp1-alp2
	a2 = a3 * math.sin(alp2)/math.sin(alp3)
	RHS1 = x1*u + y1*v + a2*a3*math.cos(alp1)
	RHS2 = y2*u - x2*v - a2*a3*math.sin(alp1)
	
	#offset_pair.append((1/a3*a3)*(u*RHS1 - v*RHS2))
	#offset_pair.append((1/a3*a3)*(v*RHS1 + u*RHS2))
	
	x3 = (1/(a3*a3))*(u*RHS1 - v*RHS2)
	y3 = (1/(a3*a3))*(v*RHS1 + u*RHS2)

	print ("x3 = ", x3, ", y3 = ", y3)
	#return offset_pair
	
def plot_component(q, x, y, angle):
	# ploting components
	if (q == 1):
		m = slope(x, y, q)
		comp_vert_x = comp_center_x(comp_y, x, y, q, m)
		comp_vert_y = m*comp_vert_x
		plt.plot(comp_vert_x, comp_vert_y, 'o', color='black', markersize = 20, markerfacecolor = 'g');
		
		comp_center_coord(x, y, comp_vert_x, comp_vert_y)
		plt.plot(x3, y3, 'o', color='black', markersize = 20, markerfacecolor = [0,1,1,1])
		

		rect = plt.Rectangle((x,y), comp_x, comp_y, angle, fc='blue', ec="red")
		plt.gca().add_patch(rect)
	if (q == 2):
		m = slope(x, y, q)
		comp_vert_x = comp_center_x(comp_y, x, y, q, m)
		comp_vert_y = m*comp_vert_x
		plt.plot(comp_vert_x, comp_vert_y, 'o', color='black', markersize = 20, markerfacecolor = 'g');
		rect = plt.Rectangle((x,y), comp_x, comp_y, angle, fc='blue', ec="red")
		plt.gca().add_patch(rect)
	if (q == 3):
		m = slope(x, y, q)
		comp_vert_x = comp_center_x(comp_y, x, y, q, m)
		comp_vert_y = m*comp_vert_x
		plt.plot(comp_vert_x, comp_vert_y, 'o', color='black', markersize = 20, markerfacecolor = 'g');
		rect = plt.Rectangle((x,y), comp_x, comp_y, angle, fc='blue', ec="red")
		plt.gca().add_patch(rect)
	if (q == 4):
		m = slope(x, y, q)
		comp_vert_x = comp_center_x(comp_y, x, y, q, m)
		comp_vert_y = m*comp_vert_x
		plt.plot(comp_vert_x, comp_vert_y, 'o', color='black', markersize = 20, markerfacecolor = 'g');
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
	vert_angle = 360/num_vert

	# creating iterable list of all internal angles
	for i in range(0, num_vert+1):
		internal_angles.insert(i, float(i*vert_angle))

	with open ("temp.txt", "w") as f_out:
		for i in internal_angles:
			# quadrant I
			if (i <= 90):
				x = radius * math.cos(np.deg2rad(i))
				y = radius * math.sin(np.deg2rad(i))
				angle = i - 90
				plot_component(1, x, y, angle)
			# quadrant II
			if (i <= 180 and i > 90):
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
			if (i > 270 and i <= 360):
				x = radius * math.cos(np.deg2rad(i))
				y = radius * math.sin(np.deg2rad(i))
				angle = i - 90	
				plot_component(4, x, y, angle)
	
			f_out.write(str("{:>5.2f}".format(round(x,2))) + " \t" + str("{:>5.2f}".format(round(y,2))) \
			+ "\t# vertex " + str(internal_angles.index(i)+1) + " @ " + str("{:>7.2f}".format(angle)) + str("\u00b0\n"))

	plot_graph()

num_vert = int(input("Enter number of vertices: "))
radius = float(input("Enter maximum size (diameter): "))/2
comp_x = float(input("Enter component width (x): "))
comp_y = float(input("Enter component heigh (y): "))
alpha = int_angle_comp()

main()
