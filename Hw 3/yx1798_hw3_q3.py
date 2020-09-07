from array_Stack import ArrayStack

# runtime remain as in original implementation for all implementations
## tuple as elements to store additional information 
class MaxStack:
    def __init__(self):
        self._data = ArrayStack()

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def push(self, e):
        if len(self._data) == 0:
            elem = (e,e)
            self._data.push(elem)
        else:
            last = self._data.top()
            mymax = last[1]
            currmax = mymax 
            if e > mymax:
                currmax = e
            tup1 = (e, currmax)
            self._data.push(tup1)

    def top(self):
        if self.is_empty():
            raise Empty("MaxStack is empty")
        ##return a reference without removing it
        temp = self._data.top()
        return temp[0]
    
    def pop(self):
        if self.is_empty():
            raise Empty("MaxStack is empty")
        temp = self._data.top()
        self._data.pop() ##Can I directly operate on the LL array??
        return temp[0]
        
    def max(self):
        ## theta 1 worst-case time
        if self.is_empty():
            raise Empty("MaxStack is empty")
        temp = self._data.top()
        return temp[1]
    
    ## Can I directly operate on the lower level array?? 

'''
data members:
A Stack of type ArrayStack
Additional Theta 1 space
'''

# maxS = MaxStack()
# maxS.push(3)
# maxS.push(1)
# maxS.push(6)
# maxS.push(4)
# print(maxS.max())
# print(maxS.pop())
# print(maxS.pop())
# print(maxS.max())
