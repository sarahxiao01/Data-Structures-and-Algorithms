
from array_Stack import ArrayStack

from queue import Empty
from queue import Full


#1 
def is_balanced(input_str):
	mys = ArrayStack()
	lst = input_str.split()
	fore = "([{"
	back = ")]}"
	for i in range(len(lst)):
		if lst[i] in fore:
			myStack.push(lst[i])
		else:
			if lst[i] not in back:
				raise Exception("invalid input!")
			else: 
				lst[i] = mine
				if mys.is_empty() == False:
					curr = myStack.pop()
				else: 
					return False
				if curr == '(' and mine != ')': #mind == syntax!!!
					return False 
				elif curr == '[' and mine != ']':
					return False 
				elif curr == '{' and mine != '}':
					return False 
	if mys.is_empty() == False: 
		return False 
	return True

input1 = "{{([])}}([])" #return True
input2 = "{{[(])}}" #return False
input3 = "([]{{[]}())}" #return False
input4 = "(([]{{[]}})" #return False
input5 = "([]{{[]}()})" #return True

# is_balanced(input1)
# is_balanced(input2)
# is_balanced(input3)
# is_balanced(input4)
# is_balanced(input5)


#2 

class ArrayDeque:
    def __init__(self,N=10):
        self._data = [None] * N
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == len(self._data)
    

    def first(self):
       ''' Return the value stored at the front of the queue '''
        if self.is_empty():
            raise Empty("Queue is Empty")
        return self._data[self._front]
        

    def last(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        end = (self.front + self.size -1)% len(self._data)
        return self._data[end]

        
    def delete_first(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        temp = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1) % len(self._data)  ## index +1 !!! VERY IMPORTANT 
        self._size -= 1
        return temp

    def add_last(self, e):
        if self._size == len(self._data):
            raise Full("Full Queue Exception")
        ''' Insert e at the end of the queue '''
        avail = (self._front+self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def add_first(self, e):
        if self._size == len(self._data):
            raise Full("Full Queue Exception")
        #avail = self._front - 1
        self._front = (self._front-1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

## ANY CHANGES IN THE FRONT leads to change in Front index!!!


    def delete_last(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        last = (self._front+self._size -1) % len(self._data)
        temp = self._data[last]
        self._data[last] = None
        self._size -= 1
        return temp

# -1 before or after? 
## Directly call self._last ?? Why hasn't Circular Queue called self._first? 

    def __str__(self):
        return str(self._data)

def main():
    # Empty Queue, size 10.
    deque = ArrayDeque()

    # Add 0, 1, 2, 3 following FIFO.
    for i in range(4):
        deque.add_first(i)
    print(deque)  # [None, None, None, None, None, None, 3, 2, 1, 0]

    # Add 4, 5, 6, 7 following LIFO.
    for j in range(4):
        deque.add_last(j + 4)
    print(deque)  # [4, 5, 6, 7, None, None, 3, 2, 1, 0]

    # Remove first one
    print(deque.delete_first()) # 3

    # Remove last one
    print(deque.delete_last()) # 7


if __name__ == '__main__':
    main()

#3 
def eval_prefix(exp_str):
	str_lst = exp_str.split(" ")
	operators = "+-*/"
	mystack = ArrayStack()
	count1 = 0
	count2 = 0
	count3 = 0
	for i in range(len(str_lst)):  # for i in range
		if count2 != 0 and count1 != 0:
			arg2 = mystack.pop()
			arg1 = mystack.pop()
			item = mystack.pop()
			if item == '+':
				res = arg1 + arg2
			elif item == '-':
				res = arg1 - arg2
			elif item == '*':
				res = arg1 * arg2
			else: 
				res = arg1 / arg2
			mystack.push(res)
			count1 = 0
			count3 = 1
		if (count1 != 0) and (str_lst[i] not in operators) and (count2 == 0):
			continue
		if (count3 != 0):
			count3 = 0
			continue
		if str_lst[i] in operators: 
			mystack.push(str_lst[i])
			count1 = 0
		else: 
			arg1 = int(str_lst[i]) ##CONVERT to int!!
			if count2 == 0 and count1 == 0:
				arg2 = int(str_lst[i+1])
				count1 += 1
				item = mystack.pop()
				if item == '+':
					res = arg1 + arg2
				elif item == '-':
					res = arg1 - arg2
				elif item == '*':
					res = arg1 * arg2
				else: 
					res = arg1 / arg2
				mystack.push(res)
				if (i+2 <= len(str_lst)-1):
					if str_lst[i+2] not in operators:
						count2 += 1
			else: 
				arg2 = arg1
				arg1 = int(mystack.pop())
				item = mystack.pop()
				if item == '+':
					res = arg1 + arg2
				elif item == '-':
					res = arg1 - arg2
				elif item == '*':
					res = arg1 * arg2
				else: 
					res = arg1 / arg2
				mystack.push(res)
	return res

def eval_postfix(exp_str):
	str_lst = exp_str.split(" ")
	operators = "+-*/"
	mystack = ArrayStack()
	for item in str_lst: 
		if item not in operators: 
			mystack.push(int(item)) #KEY is to convert to int!!!
		else: 
			arg2 = mystack.pop()
			arg1 = mystack.pop() #ARG2 popped first!!!
			if item == '+':
				res = arg1 + arg2
			elif item == '-':
				res = arg1 - arg2
			elif item == '*':
				res = arg1 * arg2
			else: 
				res = arg1 / arg2
			mystack.push(res)
	return mystack.pop()


pre_str = "- + * 16 5 * 8 4 20"
# mid_str = "16*5 + 8*4 - 20"
post_str =  "16 5 * 8 4 * + 20 -"
# print(eval_postfix(post_str))
# print(eval_prefix(pre_str))