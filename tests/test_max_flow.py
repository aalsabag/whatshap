from phasingutils import string_to_readset
from whatshap.maxflow import Leaf_node,one_d_range_tree

def test_tree_struct():
	reads = string_to_readset("""
	  11
	  000
	    11
	      00
	    11
	""")
	first_tree_attemp=one_d_range_tree(reads)
	#complete tree is the root node and from there on it gets down to the leafs
	complete_tree=first_tree_attemp.get_complete_tree()
	root_coverage=complete_tree.get_coverage()
	assert root_coverage==(1,3)
	left_child=complete_tree.get_left_child()
	right_child=complete_tree.get_right_child()
	assert left_child.get_coverage()==(2,3)
	assert right_child.get_coverage()==(1,2)
	assert left_child.get_balance()==0
	assert right_child.get_balance()==0
	assert left_child.get_min_coverage()==2
	assert right_child.get_max_coverage()==2

	#assert 0==1


def test_algo_by_mini_readset():
	reads = string_to_readset("""
	  11
	  00
	    11
	""")
	first_tree_attemp=one_d_range_tree(reads)
	#complete tree is the root node and from there on it gets down to the leafs
	complete_tree=first_tree_attemp.get_complete_tree()
	root_coverage=complete_tree.get_coverage()
	assert root_coverage==(1,2)

	#assert 0==1

#def test_struct_of_tree():
#	reads = string_to_readset("""
#	  11
#	  00
#	    11
#	""")
#	first_tree_attemp=one_d_range_tree(reads)
#	root_node=first_tree_attemp.get_complete_tree()
#	new_root_node=root_node.return_node()
#	print('Find out if we get the leaf nodes of the root node')
	#Method_list=new_root_node.get_all_leaf_nodes_of_subtree()



#	first_cov=root_node.get_coverage()
#	print(first_cov)
#	leaf_list=first_tree_attemp.get_leaf_list_of_tree()
#	print('Leaf List ')
#	print(len(leaf_list))
#	print(leaf_list)
#	assert  (len(leaf_list)==4)
#	for i,r in enumerate(reads):
#		print('I of enumerate %d '%i)
#		print(leaf_list[i].get_parent().get_coverage())
#		one_leaf=leaf_list[i].get_sibling()
#		print('one_leaf')
#		print(one_leaf)
#		firs_pos=r[0]
#		print('First position of the read')
#		print(firs_pos.position)
		#Leaf_node_of_first_position=leaf_list.index(int(firs_pos.position))
		#last_pos=read[len(read)-1]


#	for i,leaf in enumerate(leaf_list):
#		l_parent=leaf.get_parent()
#		r_child=l_parent.get_right_child()

#	assert 0==1



#def test_split_node():
#	reads = string_to_readset("""
#	  11
#	  000
#	   11
#	    000
#	     111
#	""")
#	tree=one_d_range_tree(reads)
#	root_node=tree.get_complete_tree()
#	leaf_list_of_tree=tree.get_leaf_list_of_tree()
#	for i,l_node in enumerate(leaf_list_of_tree):
#		print('Index of leaf_list %d'%i)
#		print(l_node.get_coverage())
#		print('Value of node %d'%l_node.get_value())
#		print(l_node.get_parent().get_coverage())
#
#	assert 0==1

#def test_algo_dev():
#	reads=string_to_readset("""
#	 111
#	 00
#	 11
#	  111
#	   00
#	    11
#	    0000
#	      111
#	      00
#	       11
#	""")
#	tree=one_d_range_tree(reads)
#	root_node=tree.get_complete_tree()
#	leaf_list_of_tree=tree.get_leaf_list_of_tree()
#	#go over leafs =reads
#	for i,l_node in enumerate(leaf_list_of_tree):
#		#print('Index of leaf_list %d'%i)
#		#print(l_node.get_coverage())
#		#print('Value of leaf node %d' %l_node.get_value())
#		leaf_value=l_node.get_value()
#		siblings=l_node.get_sibling()
#		print('L_node . so read node coverage %d' %l_node.get_coverage())
#		print('L_node . value %d' %leaf_value)
#		#print('Siblings:')
#		#print(siblings)
#		new_sibling=sorted(siblings)
#		#print(new_sibling)
#		#look only at the start points
#		only_end_points=[sib for sib in new_sibling if sib>leaf_value]
#		for end_part_of_read in only_end_points:
#			print('Leaf node%d'% end_part_of_read)
#			value_of_sibling=end_part_of_read
#			(split_node_of_read,List_to_change)=tree.get_split_node(l_node,value_of_sibling)
#			print('Split node')
#			print(split_node_of_read)
##			if split_node_of_read !=None:
#				print('Split node coverage')
#				print(split_node_of_read.get_coverage())
#				print('len of List to change by removal%d' %len(List_to_change))
#				for i in List_to_change:
#					print('List to change')
#					print(i.get_coverage())
#					print(i.get_balance())
#		#print(only_end_points)
#		#print('Only start points')
#		#print(l_node.get_parent().get_coverage())


def test_algo_on_small_example():
	reads=string_to_readset("""
	 111
	 000
	   11
	    00
	    11
	""")
	tree=one_d_range_tree(reads)
	root_node=tree.get_complete_tree()
	leaf_list_of_tree=tree.get_leaf_list_of_tree()
	#go over leafs =reads

	leaf_value=leaf_list_of_tree[0].get_value()
	siblings=leaf_list_of_tree[0].get_sibling()
	only_end_points=[sib for sib in siblings if sib>leaf_value]
	assert only_end_points[0]==30
	assert only_end_points[1]==30
	(split_node_of_read,List_to_change)=tree.get_split_node(leaf_list_of_tree[0],only_end_points[0])
	assert split_node_of_read.get_coverage()==(2,3)
	assert split_node_of_read.get_right_child().get_value()==30
	(split_node_of_read,List_to_change)=tree.get_split_node(leaf_list_of_tree[0],only_end_points[1])
	assert split_node_of_read.get_coverage()==(2,3)
	assert split_node_of_read.get_right_child().get_value()==30

	leaf_value=leaf_list_of_tree[1].get_value()
	siblings=leaf_list_of_tree[1].get_sibling()
	only_end_points=[sib for sib in siblings if sib>leaf_value]
	assert only_end_points[0]==40
	(split_node_of_read,List_to_change)=tree.get_split_node(leaf_list_of_tree[1],only_end_points[0])
	assert split_node_of_read.get_coverage()==(2,3)
	assert split_node_of_read==root_node




def test_get_Leaf_nodes_of_subtree():
	reads=string_to_readset("""
	 111
	 00
	 11
	  111
	   00
	    11
	    0000
	      111
	      00
	       11
	""")
	tree=one_d_range_tree(reads)
	root_node=tree.get_complete_tree()
	empyt_list=[]
	List_ofLeafs=root_node.get_Leaf_nodes_of_subtree(empyt_list)
	assert List_ofLeafs.pop().get_value()==10
	assert List_ofLeafs.pop().get_value()==20
	assert List_ofLeafs.pop().get_value()==30
	assert List_ofLeafs.pop().get_value()==40
	assert List_ofLeafs.pop().get_value()==50
	assert List_ofLeafs.pop().get_value()==60
	assert List_ofLeafs.pop().get_value()==70
	assert List_ofLeafs.pop().get_value()==80
	assert len(List_ofLeafs)==0
	l_child_of_root=root_node.get_left_child()
	List_ofLeafs= l_child_of_root.get_Leaf_nodes_of_subtree(List_ofLeafs)
	assert len(List_ofLeafs)==4
	assert List_ofLeafs.pop().get_value()==10
	assert List_ofLeafs.pop().get_value()==20
	assert List_ofLeafs.pop().get_value()==30
	assert List_ofLeafs.pop().get_value()==40
	assert len(List_ofLeafs)==0
	r_child_of_l_child=l_child_of_root.get_right_child()
	List_ofLeafs= r_child_of_l_child.get_Leaf_nodes_of_subtree(List_ofLeafs)
	assert len(List_ofLeafs)==2
	assert List_ofLeafs.pop().get_value()==30
	assert List_ofLeafs.pop().get_value()==40

def test_get_Leaf_nodes_of_subtree_2():
	reads=string_to_readset("""
	 111
	 00
	 11
	  11
	      111
	      00
	       11
	""")
	tree=one_d_range_tree(reads)
	root_node=tree.get_complete_tree()
	empyt_list=[]
	List_ofLeafs=root_node.get_Leaf_nodes_of_subtree(empyt_list)
	assert List_ofLeafs.pop().get_value()==10
	assert List_ofLeafs.pop().get_value()==20
	assert List_ofLeafs.pop().get_value()==30
	assert List_ofLeafs.pop().get_value()==60
	assert List_ofLeafs.pop().get_value()==70
	assert List_ofLeafs.pop().get_value()==80
	assert len(List_ofLeafs)==0
	l_child_of_root=root_node.get_left_child()
	List_ofLeafs= l_child_of_root.get_Leaf_nodes_of_subtree(List_ofLeafs)
	print('Length of List_of_leafs')
	print(len(List_ofLeafs))
	for i in List_ofLeafs:
		print(i.get_value())
	assert len(List_ofLeafs)==3
	assert List_ofLeafs.pop().get_value()==10
	assert List_ofLeafs.pop().get_value()==20
	assert List_ofLeafs.pop().get_value()==30
	assert len(List_ofLeafs)==0
	l_child_of_l_child=l_child_of_root.get_left_child()
	List_ofLeafs= l_child_of_l_child.get_Leaf_nodes_of_subtree(List_ofLeafs)
	assert len(List_ofLeafs)==2
	assert List_ofLeafs.pop().get_value()==10
	assert List_ofLeafs.pop().get_value()==20

