def count_group(lst):
	'''count different elements and their appearance times
	Input:
		list: value of element
	Output:
		list: frequency
	'''
	data_set = set(lst)
	count_list = []
	for one in data_set:
		count_list.append(lst.count(one))

	return count_list

def divide_group(lst, index):
	'''divide list according to feature[index]
	Input:
		list: [[], [], [], ...]
		int:  index
	Output:
		dic: {v1: [[], [], ...], v2: [[], [], ...], ... }
	'''

	#### dic: {v1: [[], [], ...], v2: [[], [], ...], ... }
	dic = {}
	for itm in lst:
		if itm[index] not in dic.keys():
			dic.setdefault(itm[index], [itm])
		else:
			dic[itm[index]].append(itm)

	return dic
