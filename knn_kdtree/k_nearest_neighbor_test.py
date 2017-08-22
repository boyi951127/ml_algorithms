from kdtree import KDTree
import numpy as np

#### test for create tree and print tree
test_sample = np.array([[7,2], [5,4], [9,6], [2,3], [4,7], [8,1]])
kd_tree = KDTree()
kd_tree.build_tree(input_data=test_sample, sel_feature=0, tree_node = None)
kd_tree.print_tree()