import myutil
import numpy as np

class KDTree(object):
	def __init__(self, ):
		self.root = -1
		self.parent = null
		self.leftChild = null
		self.rightChile = null

	
	def build_tree(self, input_data, sel_feature):
	'''input: 
	   		array --> samples*features
	   output: 
	   ---------
	'''
		#### get number of data samples, features, selected column
		sample_size = input_data.shape[0]
		feature_size = input_data.shape[1]
		input_data_col = input_data[:][sel_feature%feature_size]

		#### get middle number of selected feature
		mid_val = get_median(input_data_col.tolist())

		#### divide the input_data into two array
		left_data = np.array([])
		right_data = np.array([])
		for ir in range(sample_size):
			if input_data_col[ir] == mid_val && self.root == -1:
				self.root = input_data[ir]
			elif input_data_col[ir] < mid_val:
				np.row_stack(self.left_data, input_data[ir])
			elif input_data_col[ir] > mid_val:
				np.row_stack(self.right_data, input_data[ir])

		return self





	def print_tree(self, ):

	def search_tree(self, )：
