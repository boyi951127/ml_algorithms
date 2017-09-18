import math

class DecisionTree:

	def __init__(self, dataset, labels, epsinon=0.0):
		'''
		Input:
			dataset = [[feature1, feature2, feature3..., output], ...]
			labels = ['feature name 1', 'feature name 2', ...]
		'''
		self.dataset = dataset
		self.cur_dataset = self.dataset[:]
		self.labels = labels
		self.count_label = len(labels)
		# self.cur_lables = self.labels[:]
		self.sample_number = len(dataset)
		if self.sample_number:
			self.feature_number = len(dataset[0]) - 1
		else:
			self.feature_number = 0
		self.epsinon = epsinon

	def cal_shannon_ent(self, subset):
		'''
		Input:
			subset = [[feature1, feature2, feature3..., output], ...]
		Output:
			float: value
		'''
		output_list = []
		for lst in subset:
			output_list.append(lst[self.feature_number])
		frequecy_list = count_group(output_list)
		#### frequency_list : [3, 4, 1, 2, ....]
		sum_of_frequecy = sum(frequecy_list)
		H_X = 0
		for item in frequecy_list:
			p = item/sum_of_frequecy
			H_X -= p * math.log(p, 2)

		return H_X


	def cal_info_gain(self, dataset):
		'''
		Input:
			dataset waited to be split: [[], [], ...]
		Output:
			optimum split gain
			optimum split gain index
		'''

		#### base empirical entropy
		H_D = cal_shannon_ent(dataset)
		
		sum_samples = len(dataset)
		max_info_gain = 0
		max_ind = 0

		#### max_info_gain_div: { v1: [[], []], v2: [[], []], ... }
		max_info_gain_div = {}

		for i in range(self.lables):

			#### this label has been used
			if self.lables[i] == -1:
				continue

			#### sub_set: { v1: [[], []], v2: [[], []], ... }
			sub_set = divide_group(dataset, i)
			
			H_DA = 0
			for itm in sub_set.values():
				H_DA -= (len(itm)/sum_samples) * cal_shannon_ent(itm)
			info_gain = H_D - H_DA
			if info_gain > max_info_gain:
				max_info_gain = info_gain
				max_info_gain_div = sub_set
				max_ind = i
		# del self.cur_lables[max_ind]
		self.labels[max_ind] = -1
		self.count_label -= 1

		return max_ind, max_info_gain_div


	def cal_info_gain_ratio(self, dataset):
		'''
		Input:
			dataset waited to be split: [[], [], ...]
		Output:
			optimum split gain
			optimum split gain index
		'''

		#### base empirical entropy
		H_D = cal_shannon_ent(dataset)
		
		sum_samples = len(dataset)
		max_info_gain_ratio = 0
		max_ind = 0

		#### max_info_gain_div: { v1: [[], []], v2: [[], []], ... }
		max_info_gain_ratio_div = {}

		for i in range(self.cur_lables):

			#### this label has been used
			if self.lables[i] == -1:
				continue

			#### sub_set: { v1: [[], []], v2: [[], []], ... }
			sub_set = divide_group(dataset, i)

			#### calculate info_gain(IG)
			H_DA = 0
			for itm in sub_set.values():
				H_DA -= (len(itm)/sum_samples) * cal_shannon_ent(itm)
			info_gain = H_D - H_DA

			#### calculate penalty denominator
			iv = 0
			for itm in sub_set.values():
				p = len(itm) / sum_samples
				iv -= p * math.log(p, 2)

			info_gain_ratio = info_gain / iv
			if info_gain_ratio > max_info_gain_ratio:
				max_info_gain_ratio = info_gain_ratio
				max_info_gain_ratio_div = sub_set
				max_ind = i
		# del self.cur_lables[max_ind]
		self.labels[max_ind] = -1
		self.count_label -= 1

		return max_ind, max_info_gain_ratio_div




	def ID3_create_tree(self, dataset):
		node = {}
		lst = [dataset[i][-1] for i in range(len(dataset))]
		st = (set)lst

		if len(st) == 1:
			#### all samples in dataset belong to the same class
			return dataset[0][-1]

		max_cnt = 0
		if len(self.count_label) == 0:
			#### no feature to split
			for one in st:
				cnt = lst.count(one)
				if cnt > max_cnt:
					max_cnt = cnt
					max_label = one
			return one

		#### can still be divided
		ind, divgrp = self.cal_info_gain(dataset)
		node.setdefault(self.labels[ind], {})
		for key in divgrp.keys():
			node[self.labels[ind]].setdefault(key, ID3_create_tree(divgrp[key]))
		return node


	def C45_create_tree:
		node = {}
		lst = [dataset[i][-1] for i in range(len(dataset))]
		st = (set)lst

		if len(st) == 1:
			#### all samples in dataset belong to the same class
			return [dataset[0][-1]]

		max_cnt = 0
		if len(self.count_label) == 0:
			#### no feature to split
			for one in st:
				cnt = lst.count(one)
				if cnt > max_cnt:
					max_cnt = cnt
					max_label = one
			return [one]

		#### can still be divided
		ind, divgrp = self.cal_info_gain_ratio(dataset)
		node.setdefault(self.labels[ind], {})
		for key in divgrp.keys():
			node[self.labels[ind]].setdefault(key, ID3_create_tree(divgrp[key]))
		return node


	def CART_create_tree:
		pass






	def get_num_of_leafs(tree):
		#### calculate the number of leaves of the tree
		number_of_leaves = 0
		root = tree.keys()[0]
		seclayer = tree[root]
		for key in seclayer.keys():
			if type(seclayer[key]).__name__ == 'dict':
				number_of_leaves += get_num_of_leafs(seclayer[key])
			else:
				number_of_leaves += 1
		return number_of_leaves

	def get_tree_depth(tree):
		#### calculate the depth of the tree
		max_depth = 0
		root = tree.keys()[0]
		seclayer = tree[root]
		for key in seclayer.keys():
			if type(seclayer[key]).__name__ == 'dict':
				depth_of_tree = 1 + get_tree_depth(seclayer[key])
			else:
				depth_of_tree = 1
			if depth_of_tree > max_depth:
				max_depth = depth_of_tree
		return max_depth

	# copy online
	def print_tree(tree):
		#### to print the tree out like a tree boooooo!
		fig = plt.figure(1, facecolor='white')  
	    fig.clf()  
		axprops = dict(xticks=[], yticks=[])  
		createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)    #no ticks  
		plotTree.totalW = float(get_num_of_leafs(tree))#c存储树的宽度  
		plotTree.totalD = float(get_tree_depth(tree))#存储树的深度。我们使用这两个变量计算树节点的摆放位置  
		plotTree.xOff = -0.5/plotTree.totalW
		plotTree.yOff = 1.0
		plotTree(inTree, (0.5,1.0), '')  
		plt.show()  