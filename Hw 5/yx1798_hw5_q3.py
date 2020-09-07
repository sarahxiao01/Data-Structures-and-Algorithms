#3

from BinarySearchTree import *

#construct	an	empty	binary	search	tree
#make repeated calls to insert method
 
#a #CORRECT 
def create_chain_bst(n):
	curr = 1
	mytree = BinarySearchTree()
	while curr <= n:          #For q1, h = n
		mytree.insert(curr)  #insert runtine is O(h)
		curr += 1
	return mytree

#Draw trees
#b
#gets a positive integer n = 2^k-1 fior nonnegative k.
#returns bst with n nodes, containing keys 1, 2, 3, ...n as a complete binary tree.
	
def create_complete_bst(n):
	def add_items(bst, low, high):
		#recursive
		if low >= (high+1) // 2:                 ##insert n number of nodes, and each time you insert, it takes h = log(n)
			bst.insert(low)                        ##time because it is a complete bst
		else:
			bst = add_items(bst, low*2, high)
			now = low
			times = ((high+1) //2) // low
			for i in range(times):
				bst.insert(now)
				now += low*2
		return bst
	bst = BinarySearchTree()
	add_items(bst, 1, n)
	return bst

##seven = create_complete_bst(7)
##fifteen = create_complete_bst(15)
##lst1 = [i for i in iter(seven)]
##lst2 = [i for i in iter(fifteen)]
##print(lst1)
##print(lst2)


#c
# Insert function is of cost O(h), where h is the current height of the tree at the time of insert as
# we need to traverse down the tree to find the insert position.
# runtime of a: quadratic, because in this case (chain) height h = n (number of nodes), instead of h = log n.  
# Therefore,  the cost of creating the tree is 1 + 2 + 3 + 4 +... + n = n(n+1)/2 as the tree increases in height,
# which is O(n^2). 
# runtime of b: n(log(n)), because in this case (complete BST) height h = log(n) (number of nodes).  
# Therefore,  the cost of creating the tree is nlog(n) as we do n inserts of n nodes while each insertion costs log(n).
# which is O(n^2). 
