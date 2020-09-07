from DoublyLinkedList import *
##Import both Node and DLL Classes

 class _Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    
    def __init__(self, element, prev = None, next = None):            # initialize node's fields
      self._element = element                           # user's element
      self._prev = prev                                 # previous node reference
      self._next = next   

#1

class LinkedStack:
	def __init__(self):
		self._data = Doubly_Linked_List()      

	def __len__(self):
		return len(self._data)

	def is_empty(self):
		return len(self) == 0

	def push(self, e):
		# newNode = self._Node(e, self._trailer._prev, self._trailer) #Make a new node!!!
		# self._trailer._prev._next = newNode
		# self._trailer._prev = newNode
		# self._size += 1 ## increase the size
		self._data._insert_last(e)

	def pop(self):
		if self.is_empty():
			raise Exception("LinkedStack is empty!")
		# popNode = self.trailer._prev
		# # popNode._prev._next = popNode._next
		# # popNode._next._prev = popNode._prev
		# # popNode._prev = None 
		# # popNode._next = None 
		# predecessor = popNode._prev
		# successor = popNode._next
		# predecessor._next = successor
		# successor._prev = predecessor
		# element = popNode._element
		# self._size -= 1 #decrease size!!!
		# popNode._prev = popNode._next = None 
		# popNode._element = None
		# return element
		return self._data.delete_last()
	def top(self):
		if self.is_empty():
			raise Exception("LinkedStack is empty!")
		return self._data.last()
		# return self._data._trailer._prev._element

(n+1) // 2 
#2
class MidStack:
	def __init__(self):
		self._data = Doubly_Linked_List()
		self._first = self._data._header._next
		self._last = self._data._trailer._prev
		self._mid = self._first

	def __len__(self):
		return len(self._data)

	def is_empty(self):
		return len(self) == 0

	def push(self, e):
		# newNode = self._Node(e, self._last, self._data._trailer)
		# self._last._next = newNode
		# self._data._trailer._prev = newNode
		# self._data._size += 1
		self._data.insert_last(e)
		if (self._data._size % 2) == 1:
			self._mid = self._mid._next ##mid is a DLL reference, not a number!!!

	def top(self):
		if self.is_empty():
			raise Exception("Midstack is empty!")
		return self._last._element

	def pop(self):
		if self.is_empty():
			raise Exception("Midstack is empty!")
		element = self._data.delete_last()
		if self.is_empty():
			self._mid = None
			# self._first = None 
			# self._last = None
		if (self._data._size) % 2  == 0:
			self._mid = self._mid._prev ##mid is a DLL reference, not a number!!!
		return element
		# element = self._last._element
		# predecessor = self._last._prev 
		# successor = self._data._trailer
		# predecessor._next = successor 
		# successor._prev = predecessor 
		# self._last._prev = self._last._next = self._last._element = None
		# self._data._size -= 1

	def mid_push(self, e):
		# newNode = self._Node(e, self._mid, self._mid._next)
		# predecessor = self._mid
		# successor = self._mid._next
		# predecessor._next = newNode
		# successor._prev = newNode
		self._data._insert_between(self, e, self._mid, self._mid._next)
		#insert and delete directly take size 
		if (self._data._size) % 2  == 1:
			self._mid = self._mid._next

	def get_mid(self):
		return self._mid._element ##mid directly refers to element
		#element not data in DLL
		#Make all mid changes after or before element change

# 1
# 1, 2
# 1, 2, 3
# 1, 2, 3, 4
# 1, 2, 3, 4, 5
# 1, 2, 3, 4, 5, 6

#3
#a 
def reverse_dll_by_data(dll):
	myfirst = dll.header #start from trailer and header; increment sequences!!!
	mylast = dll.trailer
	while myfirst.next != mylast:
		myfirst = myfirst.next
		if mylast.prev != myfirst:
			mylast = mylast.prev 
			myfirst.element, mylast.element = mylast.element, myfirst.element 

#b
def reverse_dll_by_node(dll):
	myfirst = dll.header
	mylast = dll.trailer
	while myfirst.next != mylast:
		myfirst = myfirst.next
		firstpred = myfirst.prev
		firstnext = myfirst.next
		if mylast.prev != myfirst:
			mylast = mylast.prev 
			lastpred = mylast.prev
			lastnext = mylast.next
			myfirst.prev = lastpred
			myfirst.next = lastnext
			mylast.prev = firstpred
			mylast.next = firstnext
			firstpred.next = mylast
			firstnext.prev = mylast
			lastpred.next = myfirst
			lastnext.prev = myfirst

	#using class methods 
	myfirst = dll.header
	mylast = dll.trailer
	while myfirst.next != mylast:
		myfirst = myfirst.next
		if mylast.prev != myfirst:
			mylast = mylast.prev 
			dll._insert_between(mylast._element, myfirst, myfirst._next)
			dll._insert_between(myfirst._element, mylast._prev, mylast)
			mylast = mylast._prev
			myfirst = myfirst._next
			dll._delete_node(mylast._next)
			dll._delete_node(myfirst._prev)
			
	#alternative solution
	curr = dll.header
	for i in range(len(dll)-1): #for length???
		mylast = dll.delete_last()
		dll.insert_between(mylast, curr, curr._next) #remember inserting an element!
		curr = curr._next
	#No runtime concerns for DLL!!!
	##Which methods would we be allowed to use??? esp. for this kind of methods 
	##When implementing a class, allowed to modify underlying array or just use methods? 
	##How to call _insert_between? Can we call these here???
			



