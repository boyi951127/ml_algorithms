import myutil
import numpy as np

class KDTree(object):
	def __init__():
		self.tree_root = TreeNode()

	def build_tree(self, input_data, sel_feature, tree_node = None):
	'''input: 
	   		array --> samples*features
	   		selected feature to split
	   		tree node
	   output: 
	   ---------
	'''
		#### tree root
		if tree_node == None:
			tree_node = self.tree_root

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
			if input_data_col[ir] == mid_val and tree_node.root == -1:
				tree_node.root = input_data[ir]
			elif input_data_col[ir] < mid_val:
				np.row_stack(tree_node.left_data, input_data[ir])
			elif input_data_col[ir] > mid_val:
				np.row_stack(tree_node.right_data, input_data[ir])

		#### deal with left and right nodes
		left_node = TreeNode()
		left_node.parent = tree_node
		right_node = TreeNode()
		right_node.parent = tree_node
		build_tree(left_data, sel_feature+1, left_node)
		build_tree(right_data, sel_feature+1, right_node)






	def print_tree(self, ):

	def search_tree(self, )：
