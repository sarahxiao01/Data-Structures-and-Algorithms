#2
from DoublyLinkedList import Doubly_Linked_List

class Integer():
    def __init__(self, num_str = ''):
    	self._data = Doubly_Linked_List()
    	for i in range(len(num_str)):
    		self._data.insert_last(num_str[i])
        
    def __add__(self, other):
    	carrier = 0
    	newInt = 0
    	result = Integer()
    	currNode = self._data._trailer
    	myNode = other._data._trailer
        if self._data.is_empty() or other._data.is_empty():
            raise Exception("invalid input")
    	while currNode._prev is not self._data._header:
    		currNode = currNode._prev
    		if myNode._prev is not self._data._header:
    			myNode = myNode._prev
    			newInt = int(currNode._element) + int(myNode._element)
                if carrier != 0:
    				newInt += 1
    				carrier -= 1
                if newInt >= 10:
    				newInt -= 10
    				carrier += 1
                result._data.insert_first(str(newInt))

        if currNode._prev == self._data._header:
            mybool = False
            while myNode._prev is not other._data._header:
                myNode = myNode._prev
                result._data.insert_first(myNode._element)
    	if myNode._prev == other._data._header:
            obool = False
            while currNode._prev is not self._data._header:
                currNode = currNode._prev
                result._data.insert_first(currNode._element)
    	return result

    def __repr__(self):
    	repstr = ''
    	currNode = self._data._header._next
    	while currNode is not self._data._trailer:
    		repstr += currNode._element
    		currNode = currNode._next
        return repstr

# n1 = Integer('375')
# n2 = Integer('4029')
# print(n1)
# print(n2)
# n3 = n1 + n2
# print(n3)