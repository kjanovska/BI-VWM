from database import *

def plane_sweep(points, minmax):
	if str(minmax[0]) == 'min' and str(minmax[1]) == 'min':
		return plane_sweep_minmin(points)
	elif str(minmax[0]) == 'min' and str(minmax[1]) == 'max':
		return plane_sweep_minmax(points)
	elif str(minmax[0]) == 'max' and str(minmax[1]) == 'min':
		return plane_sweep_maxmin(points)
	return plane_sweep_maxmax(points)


def plane_sweep_maxmax(points): # points are of class SkylineParam
	# 1. sort points by x
	points.sort(key=lambda a: a.x, reverse=False)
	# 2. stack s - list, using .pop()
	stack = []
	for point in points:
		while not len(stack) == 0 and stack[-1].y <= point.y:
			stack.pop()
		stack.append(point)
	return stack # returns points laying on a skyline

def plane_sweep_maxmin(points):
	points.sort(key=lambda a: a.x, reverse=False)
	stack = []
	for point in points:
		while not len(stack) == 0 and stack[-1].y >= point.y:
			stack.pop()
		stack.append(point)
	return stack

def plane_sweep_minmax(points):
	points.sort(key=lambda a: a.x, reverse=True)
	stack = []
	for point in points:
		while not len(stack) == 0 and stack[-1].y <= point.y:
			stack.pop()
		stack.append(point)
	return stack

def plane_sweep_minmin(points):
	points.sort(key=lambda a: a.x, reverse=True)
	stack = []
	for point in points:
		while not len(stack) == 0 and stack[-1].y >= point.y:
			stack.pop()
		stack.append(point)
	return stack