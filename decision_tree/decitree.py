import math

class DecisionTree:

	def __init__(self, dataset, labels):
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
			optimum split
		'''

		#### base empirical entropy
		H_D = cal_shannon_ent(dataset)
		
		sum_samples = len(dataset)
		max_info_gain = 0

		#### max_info_gain_div: { v1: [[], []], v2: [[], []], ... }
		max_info_gain_div = {}

		for i in range(self.labels):

			#### sub_set: { v1: [[], []], v2: [[], []], ... }
			sub_set = divide_group(dataset, i)
			
			info_gain = 0
			for itm in sub_set.values():
				info_gain -= (len(itm)/sum_samples) * cal_shannon_ent(itm)
			if info_gain > max_info_gain:
				max_info_gain = info_gain
				max_info_gain_div = sub_set

		return max_info_gain, max_info_gain_div






	def cal_info_gain_ratio:

	def ID3_create_tree:

	def C45_create_tree:

	def CART_create_tree:

	def print_tree: