import copy 
import math
from array_Stack import ArrayStack
from Circular_Queue import ArrayQueue


def permutations(lst):
    ## non-recursive
    ## alloed a Stack, a Queue, Theta 1 additional space
    # use stack to generate permutations, use queue to store partial collection of pers generated so far
    # queue set up to hold
    mystack = ArrayStack()
    length = math.factorial(len(lst))
    result = ArrayQueue(length)
    for i in range(len(lst)):
        mystack.push(lst[i])
    lst1 = [mystack.pop()]
    result.enqueue(lst1)
    while mystack.is_empty() == False:
        elem = mystack.pop()
        times = math.factorial(len(result.first()))
        for i in range(times):
            lst1 = result.dequeue()
            for i in range(len(lst1)+1):
                newlst = copy.deepcopy(lst1)
                newlst.insert(i, elem)
                result.enqueue(newlst)
    return result

mylst = [1,2,3,4,5]
print(permutations(mylst))
        
