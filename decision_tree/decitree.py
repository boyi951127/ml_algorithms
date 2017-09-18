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
		self.cur_lables = self.labels[:]
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

		for i in range(self.cur_lables):

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
		del self.cur_lables[max_ind]

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
		del self.cur_lables[max_ind]

	return max_ind, max_info_gain_ratio_div




	def ID3_create_tree(self, dataset):
		node = {}
		lst = [dataset[i][-1] for i in range(len(dataset))]
		st = (set)lst

		if len(st) == 1:
			#### all samples in dataset belong to the same class
			return [dataset[0][-1]]

		max_cnt = 0
		if len(self.cur_lables) == 0:
			#### no feature to split
			for one in st:
				cnt = lst.count(one)
				if cnt > max_cnt:
					max_cnt = cnt
					max_label = one
			return [one]

		

		ind, divgrp = self.cal_info_gain(dataset)



	def C45_create_tree:

	def CART_create_tree:

	def print_tree: