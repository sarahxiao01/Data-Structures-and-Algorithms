from BinarySearchTree import *
from LinkedBinaryTree import *

#1

def bt_even_sum(binTree):
    def helper(root):
        if root.left is None and root.right is None:
            if root.element % 2 == 0:
                mysum = root.element
                return mysum
            return 0
        elif root.left and root.right:
            mysum = helper(root.left) + helper(root.right)
            if root.element % 2 = 0:
                mysum += root.element
            return mysum
        elif root.left:
            mysum = helper(root.left)
            if root.element % 2 = 0:
                mysum += root.element
            return mysum
        else:
            mysum = helper(root.right)
            if root.element % 2 = 0:
                mysum += root.element
            return mysum
    return helper(binTree.root)

#2
def bt_contains(root, val):
    if root.element == val:  ##very basic base case, outside of cases
        return True
    if root.left is None and root.right is None:
        return root.element == val #return True False statement
    else:
        mybool = False #Define first
        # if root.element != val:
        #     mybool = False
        if root.left:
            mybool = mybool or bt_contains(root.left, val)
        if root.right:
            mybool = mybool or bt_contains(root.right, val)
        return mybool

#3
def is_BST(root):  ##Check None
    if root is None: #Empty tree is still BST
        return True 
    return is_BST_helper(root)[2]

def is_BST_helper(root):
    if root.left is None and root.right is None:
        return (root.element, root.element, True)
    leftbool = True 
    newmin = root.element #Define first, return directly
    if root.left is not None:
        left = is_BST_helper(root.left) #function call ref for easy tuple reference
        #check separately whether min max, inner, and whether left itself; separate; left bool
        leftbool = (left[0] < left[1] < root.element) and (root.left.element < root.element) and (left[2])
        newmin = left[0]
    rightbool = True 
    newmax = root.element
    if root.right is not None:
        right = is_BST_helper(root.right) 
        rightbool = (right[1] > right[0] > root.element) and (root.right.element > root.element) and (right[2])
        newmax = right[1]
    return (newmin, newmax, leftbool and rightbool) #Doesn't return true min and max for non-BST?
    #return at the end, after all conditions
    #see whether both or either should be updated 