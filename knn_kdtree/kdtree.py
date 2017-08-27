from myutil import get_median
from myutil import eucli_distance
from treenode import TreeNode
import numpy as np
import math
import Queue

class KDTree(object):
	def __init__(self):
		self.tree_root = TreeNode()
		self.level = 0
		self.count = 0
		self.search_path = []
		# self.flag = False

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
		tree_node.dimension = sel_feature%feature_size

		#### get middle number of selected feature
		mid_val = get_median(input_data_col.tolist())

		#### divide the input_data into two array
		left_data = np.array([])
		right_data = np.array([])
		for ir in range(sample_size):
			if input_data_col[ir] == mid_val and tree_node.isempty == True:
				tree_node.root = input_data[ir]
				tree_node.isempty = False
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
		self.count = self.count + 1
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

		self.level = (int)(math.log(self.count, 2)) + 1
		level = self.level
		q_tn = Queue.Queue()
		q_tn.put(self.tree_root)
		while not q_tn.empty():
			t_len = q_tn.qsize()
			print "LEVEL %d:" % (self.level-level+1)
			# cnt = 2**(self.level-level)-1
			for i in range(t_len):
				T = q_tn.get()

				#### we have to print null or we cannot distinct binary tree
				if T.isempty == True:
					if i == t_len -1:
						print "null"
					else:
						print "null",
				else:
					o_arr = [str(c) for c in T.root]
					if i == t_len-1:
						print "(", ", " . join(o_arr), ")"
					else:
						print "(", ", " . join(o_arr), ")",
					if T.leftChild.root is not None or (T.leftChild.root is None and level != 1):
						q_tn.put(T.leftChild)
					if T.rightChild.root is not None or (T.rightChild.root is None and level != 1):
						q_tn.put(T.rightChild)
			# print level
			level = level - 1

		print "done!"




	def find_position(self, search_point, tree_node):
		"""input: 
		   		array(1*d) : search point
		   output: 
		   		array(1*d) : closest point
		   ---------
		"""
		if tree_node.isempty == True:
			return

		cur_dim = tree_node.dimension
		if tree_node.leftChild.isempty == True and tree_node.rightChild.isempty == True:
			# self.flag = True
			self.search_path.append(tree_node)
		elif search_point[0, cur_dim] >= tree_node.root[cur_dim]:
			self.search_path.append(tree_node)
			self.find_position(search_point, tree_node.rightChild)
		elif search_point[0, cur_dim] < tree_node.root[cur_dim]:
			self.search_path.append(tree_node)
			self.find_position(search_point, tree_node.leftChild)



	def search_neighbor(self, search_point):
		"""input: 
		  		array(1*d) : search point
		   output: 
		   		minimum distance & minimum
		"""

		#### generate the precede points first
		self.find_position(search_point, self.tree_root)
		print "traceback path:"
		for i in self.search_path:
			print i.root
		# print self.search_path

		t_n = self.search_path.pop()
		min_dist = eucli_distance(search_point[0].tolist(), t_n.root.tolist())
		min_dist_pnt = t_n.root
		while(len(self.search_path) != 0):
			t_n = self.search_path.pop()
			if t_n.isempty == True:
				continue
			cur_dist = eucli_distance(search_point[0].tolist(), t_n.root.tolist())
			if cur_dist < min_dist:
				min_dist = cur_dist
				min_dist_pnt = t_n.root
				if search_point[0, t_n.dimension] >= t_n.root[t_n.dimension]:
					self.search_path.append(t_n.leftChild)
				elif search_point[0, t_n.dimension] < t_n.root[t_n.dimension]:
					self.search_path.append(t_n.rightChild)
			# elif eucli_distance(search_point.tolist(), t_n.root.tolist()) >= min_dist:
			# 	continue
		# print np.array([min_dist_pnt])
		# print search_point
		return min_dist, np.array([min_dist_pnt])




			







