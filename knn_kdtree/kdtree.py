from myutil import get_median
from treenode import TreeNode
import numpy as np
import Queue

class KDTree(object):
	def __init__(self):
		self.tree_root = TreeNode()
		self.level = 0

	def build_tree(self, input_data, sel_feature, tree_node = None):
		"""
		input: 
			array 
				--> samples*features
			selected feature to split
			tree node
		
		output:
		-------- 
		"""

		#### end recursion
		if not input_data.size:
			return

		#### tree root
		if tree_node == None:
			tree_node = self.tree_root

		#### get number of data samples, features, selected column
		sample_size = input_data.shape[0]
		feature_size = input_data.shape[1]
		input_data_col = input_data[:, sel_feature%feature_size]

		#### get middle number of selected feature
		mid_val = get_median(input_data_col.tolist())

		#### divide the input_data into two array
		left_data = np.array([])
		right_data = np.array([])
		for ir in range(sample_size):
			if input_data_col[ir] == mid_val and tree_node.root == None:
				tree_node.root = input_data[ir]
			elif input_data_col[ir] <= mid_val:
				if left_data.size == 0:
					left_data = np.reshape(input_data[ir], (1, input_data[ir].shape[0]))
				else:
					left_data = np.row_stack((left_data, input_data[ir]))
			elif input_data_col[ir] > mid_val:
				if right_data.size == 0:
					right_data = np.reshape(input_data[ir], (1, input_data[ir].shape[0]))
				else:
					right_data = np.row_stack((right_data, input_data[ir]))

		#### deal with left and right nodes
		self.level = self.level + 1
		tree_node.leftChild = TreeNode()
		tree_node.leftChild.parent = tree_node
		tree_node.rightChild = TreeNode()
		tree_node.rightChild.parent = tree_node
		self.build_tree(left_data, sel_feature+1, tree_node.leftChild)
		self.build_tree(right_data, sel_feature+1, tree_node.rightChild)




	def print_tree(self):
		"""input: 
		   ---------
		   output: 
		   ---------
		"""

		#### if the tree is empty, print empty tree
		if self.tree_root == None:
			print "empty tree!"
			return

		print "\n"
		level = self.level
		q_tn = Queue.Queue()
		q_tn.put(self.tree_root)
		while not q_tn.empty():
			t_len = q_tn.qsize()
			print "LEVEL %d:" % (self.level-level+1)
			for i in range(t_len):
				T = q_tn.get()
				o_arr = [str(c) for c in T.root]
				if i == t_len-1:
					print "(", ", " . join(o_arr), ")"
				else:
					print "(", ", " . join(o_arr), ")",
				if T.leftChild.root is not None:
					q_tn.put(T.leftChild)
				if T.rightChild.root is not None:
					q_tn.put(T.rightChild)
			level = level - 1

		print "\ndone!"




	def search_tree(self, ):
		pass
