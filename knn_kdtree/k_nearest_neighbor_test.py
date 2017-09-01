from kdtree import KDTree
import numpy as np

#### test for create tree and print tree
test_sample = np.array([[7,2], [5,4], [9,6], [2,3], [4,7], [8,1]])
kd_tree = KDTree()
kd_tree.build_tree(input_data=test_sample, sel_feature=0, tree_node = None)
kd_tree.print_tree()

#### test for search closest neighbor
point = np.array([[2.1, 3.1]])
min_dist_list, min_dist_pnt_list = kd_tree.search_neighbor(point, 2)
cnt = 1
for d, p in zip(min_dist_list, min_dist_pnt_list):
	print "%d distance: "%(cnt), d
	print "%d point: "%(cnt), p
	cnt = cnt + 1
point = np.array([[2, 4.5]])
min_dist_list, min_dist_pnt_list = kd_tree.search_neighbor(point, 2)
cnt = 1
for d, p in zip(min_dist_list, min_dist_pnt_list):
	print "%d distance: "%(cnt), d
	print "%d point: "%(cnt), p
	cnt = cnt + 1