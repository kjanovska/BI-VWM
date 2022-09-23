from database import *

def brute_force(points, minmax):
	if str(minmax[0]) == 'min' and str(minmax[1]) == 'min':
		return brute_force_minmin(points)
	elif str(minmax[0]) == 'min' and str(minmax[1]) == 'max':
		return brute_force_minmax(points)
	elif str(minmax[0]) == 'max' and str(minmax[1]) == 'min':
		return brute_force_maxmin(points)
	return brute_force_maxmax(points)


def brute_force_maxmax(points):
	skyline_points = []
	for point in points:
		is_on_skyline = True
		for compare_point in points:
			if point.x < compare_point.x and point.y < compare_point.y:
				is_on_skyline = False
				break
		if is_on_skyline:
			skyline_points.append(point)
	return skyline_points


def brute_force_maxmin(points):
	skyline_points = []
	for point in points:
		is_on_skyline = True
		for compare_point in points:
			if point.x < compare_point.x and point.y > compare_point.y:
				is_on_skyline = False
				break
		if is_on_skyline:
			skyline_points.append(point)
	return skyline_points

def brute_force_minmax(points):
	skyline_points = []
	for point in points:
		is_on_skyline = True
		for compare_point in points:
			if point.x > compare_point.x and point.y < compare_point.y:
				is_on_skyline = False
				break
		if is_on_skyline:
			skyline_points.append(point)
	return skyline_points

def brute_force_minmin(points):
	skyline_points = []
	for point in points:
		is_on_skyline = True
		for compare_point in points:
			if point.x > compare_point.x and point.y > compare_point.y:
				is_on_skyline = False
				break
		if is_on_skyline:
			skyline_points.append(point)
	return skyline_points
