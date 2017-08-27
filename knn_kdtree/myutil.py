import numpy as np

def get_median(data):
	"""input: 
	   		list : one-dimension feature
	   output: 
	   		int/float : middle value
	   ---------
	"""
	data.sort()
	half = len(data) // 2
	return data[half]

def eucli_distance(point_1, point_2):
	"""input: 
	   		list : point_1, point_2
	   output: 
	   		float : distance between two points
	   ---------
	"""
	# print "point_1=",point_1
	# print "point_1=",point_2
	sum_of_dist = 0
	for i1, i2 in zip(point_1, point_2):
		sum_of_dist += (i1 - i2)**2
	return np.sqrt(sum_of_dist)
	
	