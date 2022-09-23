from database import *

def divide_conquer(points, minmax):
	points.sort(key=lambda i: i.x, reverse=True)
	if str(minmax[0]) == 'min' and str(minmax[1]) == 'min':
		return divide_conquer_minmin(points)
	elif str(minmax[0]) == 'min' and str(minmax[1]) == 'max':
		return divide_conquer_minmax(points)
	elif str(minmax[0]) == 'max' and str(minmax[1]) == 'min':
		return divide_conquer_maxmin(points)
	return divide_conquer_maxmax(points)


def divide_conquer_maxmax(points):
	if len(points) <= 1:
		return points
	middle = len(points)//2
	a = divide_conquer_maxmax(points[:middle])
	b = divide_conquer_maxmax(points[middle:])
	return merge_skyline_maxmax(a, b)

def merge_skyline_maxmax(a, b):
	merged = a + b
	highesty = 0
	result = []
	for point in merged:
		if point.y > highesty:
			highesty = point.y
			result.append(point)
	return result

def divide_conquer_maxmin(points):
	if len(points) <= 1:
		return points
	middle = len(points)//2
	a = divide_conquer_maxmin(points[:middle])
	b = divide_conquer_maxmin(points[middle:])
	return merge_skyline_maxmin(a, b)

def merge_skyline_maxmin(a, b):
	merged = a + b
	highesty = float("inf")
	result = []
	for point in merged:
		if point.y < highesty:
			highesty = point.y
			result.append(point)
	return result

def divide_conquer_minmax(points):
	if len(points) <= 1:
		return points
	middle = len(points)//2
	a = divide_conquer_minmax(points[:middle])
	b = divide_conquer_minmax(points[middle:])
	return merge_skyline_minmax(a, b)

def merge_skyline_minmax(a, b):
	merged = a + b
	highesty = 0
	result = []
	for point in merged:
		if point.y > highesty:
			highesty = point.y
			result.append(point)
	return result

def divide_conquer_minmin(points):
	if len(points) <= 1:
		return points
	middle = len(points)//2
	a = divide_conquer_minmin(points[:middle])
	b = divide_conquer_minmin(points[middle:])
	return merge_skyline_minmin(a, b)

def merge_skyline_minmin(a, b):
	merged = a + b
	highesty = float("inf")
	result = []
	for point in merged:
		if point.y < highesty:
			highesty = point.y
			result.append(point)
	return result
