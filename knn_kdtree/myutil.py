def get_median(data):
	data.sort()
	half = len(data) // 2
	return data[half]