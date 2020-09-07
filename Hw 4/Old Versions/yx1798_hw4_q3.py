#3
from DoublyLinkedList import Doubly_Linked_List

class CompactString():

    def __init__(self, orig_str):
        self._data = Doubly_Linked_List()
    	for i in range(len(orig_str)):
    		if i > 0 and orig_str[i] !=  orig_str[i-1]:
    			self._data.insert_last((orig_str[i], 1))
    		else:
    			mylast = self._data.last()
    			tup1 = mylast[1]
    			self._data._trailer._prev._element = (orig_str[i], tup1+1)

    def __add__(self, other):
    	if self._trailer._prev._element[0] == other._header._next._element[0]:

    	else: 
    		self._trailer._prev._next = other._header._next
    		other._header._next._prev = self._trailer._prev


        for
    def __lt__(self, other):
    	if self._data._header._next == self._data._trailer and other._data._header._next == other._data._trailer: 
    		return False
    	elif other._data._header._next == self._data._trailer: 
    		return False
    	elif self._data._header._next == self._data._trailer: 

    def __eq__(self, other):
    	if self._data._header._next == self._data._trailer and other._data._header._next == other._data._trailer: 
    		return True

    def __le__(self, other):

    	if self == other: 
    		return True 
        
    def __gt__(self, other):
        
    def __ge__(self, other):

    	if self == other: 
    		return True 

    def __repr__(self):
