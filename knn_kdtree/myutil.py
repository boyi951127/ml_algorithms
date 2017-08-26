def get_median(data):
	"""input: 
	   		list : one-dimension feature
	   output: 
	   		int : middle value
	   ---------
	"""
	data.sort()
	half = len(data) // 2
	return data[half]

def eucli_distance(point_1, point_2):
	"""input: 
	   		list : point_1, point_2
	   output: 
	   		int : middle value
	   ---------
	"""
	
	