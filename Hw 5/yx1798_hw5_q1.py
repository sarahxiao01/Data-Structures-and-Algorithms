#1
from LinkedBinaryTree import *

class Empty(Exception):
	pass

#raise Exception if tree is empty
#linear time, traversal not allowed

#O(n) Runtime, raise Exception when called on Empty tree
def find_min_and_max(bin_tree):
	# if bin_tree.is_empty():
	# 	return Empty("Binary tree is empty!")
	def subtree_min_and_max(root):
		if root is None:
			return Empty("Binary tree is empty!")
		mymin = root._element
		mymax = root._element
		if root._left is not None:
			myleft = subtree_min_and_max(root._left)
			mymin = min(mymin, myleft[0])
			mymax = max(mymax, myleft[1])
		if root._right is not None:
			myright = subtree_min_and_max(root._right)
			mymin = min(mymin, myright[0])
			mymax = max(mymax, myright[1])
		return (mymin, mymax)
	return subtree_min_and_max(bin_tree._root)

# me = LinkedBinaryTree()
# me.add_root(30)
# me.add_right(me._root, 18)
# me.add_left(me._root, 24)
# me.add_right(me._root._left, -5)
# me.add_left(me._root._left, 37)
# me.add_right(me._root._right, 8)
# me.add_left(me._root._right, -10)
# print(find_min_and_max(me))
