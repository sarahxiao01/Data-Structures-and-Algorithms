import ctypes


class UserDefinedDynamicArray:
    def __init__(self,I=None):
        self._n=0
        self._capacity=1
        self._A=self._make_array(self._capacity)# storage box, low level array from ctypes
        if I:
            self.extend(I)

    def __len__(self):
        return self._n

    def append(self,x):
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n]=x
        self._n+=1

    def _resize(self,newsize):
        A=self._make_array(newsize)
        self._capacity=newsize
        for i in range(self._n):
            A[i]=self._A[i]
        self._A=A

    def _make_array(self,size):
        return (size*ctypes.py_object)()

    def __getitem__(self,i): 
        if isinstance(i,slice):#list2=list1[:-1]
            A=UserDefinedDynamicArray()
            for j in range(*i.indices(self._n)): # * operator was used to unpack the slice tuple
                A.append(self._A[j])
            return A
        if i<0:
            i=self._n+i
        return self._A[i]

    def __delitem__(self,i):
        if isinstance(i,slice):
            #A=UserDefinedDynamicArray()
            for j in reversed(range(*i.indices(self._n))):
                 del self[j]
        else:
            if i<0:
                i=self._n+i
            for j in range(i,self._n-1):
                self._A[j]=self._A[j+1]
            self[-1]=None   #__setitem__     
            self._n-=1


    def __str__(self):
        return "[" \
               +"".join( str(i)+"," for i in self[:-1]) \
               +(str(self[-1]) if not self.is_empty() else "") \
               +"]"

    def is_empty(self):
        # we will do in class
        # return true if array is empty otherwise false
        # Your Code
        
        return self._n==0
        #pass

    def __iter__(self):
        # we will do in class, iterate through the list using yield
        # Your Code
        for i in range(self._n):
            yield self[i]
        #pass

    def __setitem__(self,i,x):
        #we will do in class, think about how to handle negative index
        # Your code
        if i<0:
            i = i+self._n
        self._A[i]=x
        #pass

    def extend(self,I):
        # append all elements of I to the self
        for each in I:
            self.append(each)
        #pass

    def reverse(self):
        #we will do in class
        # reverse the list
        # your code
        for i in range(len(self)//2):
            j = len(self)-1-i
            self._A[i],self._A[j]=self._A[j],self._A[i]
        #pass


    def __contains__(self,x):
        #we will do in class
        # If element x is present in the list return true otherwise false
        # your code
        for each in self:
            if x == each:
                return True
        return False
        #pass

    def index(self,x):
        #we will do in class
        # Return the index of first occurrence of element x, if not found in the list return None.
        # Your code
        for i in range(len(self)):
            if x == self[i]:
                return i
        return None
        #pass

    def count(self,x):
        #we will do in class
        # return how many times element x is present in the list
        # Your code
        count = 0
        for each in self:
            if x == each:
                count += 1
        return count
        #pass



    def __add__(self,other):
        # we will do in class
        # '+' Operator Overloading for UserDefinedDyamicArray Class like myList1+myList2 will return a list containing all the elements of myList1 and then myList2
        # Your code
        
        pass
    def __iadd__(self,other):
        pass
    def __sub__(self,other):
        pass

    def __mul__(self,times):
        # we will do in class
        # '*' Operator Overloading for UserDefinedDyamicArray Class like myList1*3 will return a list having myList1 elements three times.
        # Your code
        pass

    __rmul__=__mul__



    def pop(self,i=-1):
        # We will do in class
        # delete element at position i using del keyword, by default we delete the last element from UserDefinedDyamicArray and return the element to the calling method
        # Your Code
        pass
        
    def remove(self,x):
        #we will do in class
        # remove element x from the list, we will delete the first occurrence of element x from the list
        # at first find out the index of element x, then delete it
        # Your code
        pass




def main():
## Task1: Print the lists
##  create two empty list myList1 and myList2, append some elements and print it. You need to implement __len__ and __iter__ methods in the UserDefinedDyanmicArray class.
    myList1 = UserDefinedDynamicArray()
    print(myList1)
    myList1.append(3)
    print(myList1)

    myList2=UserDefinedDynamicArray()
    for i in range(10):
        myList2.append((i+1)*20)
    
    print(myList2)
    
    print("myList3")
    myList3= myList2[4]
    print(myList3)

##  Task2: Delete elements from the myList2 using "del" keyword. __delitem__ method is already given but you need to write __setitem__ method to make it run.
##  suppose we want to delete 2nd, third, and four elements from myList2 by as follows. This will give you an error as __setitem__ method needs to be complete

   
    

    
##  Task3: extending the list using extend function and creating a list from an existing list
##  suppose we want to use extend myList1 by adding all the elements in myList2 by calling the extend(self, I) function in the UserDefinedDynamicArray Class

    myList1.extend(myList2)
    print(myList1)

##  Task4: Reverse a list by calling myList2.reverse(), it will reverse the list.
    print(myList2)
    myList2.reverse()
    print(myList2)

##  Task5: Implement __contains__(self,x), count(x), and index(x) as described in the UserDefinedDynamicArray class.
##  __contains__ will check whether element x is present in the list. If yes return true, otherwise false
##  index(x) will return the index of element x in the list. If x is present multiple times, it will return the first index of x, otherwise it will return None
##  count(x) will return how many times element x is present in the list. If the element x is not present, it will return 0.
    x=140
    print("Whether x is present in the MyList1: ",x in myList1) #contains function check
    print("x current position in the myList1 is ",myList1.index(x))
    print("Number of times x appears in the myList1 is ",myList1.count(x))



##  Task6: Implement __add__(self,other) and __mul__(self,times) as described in the UserDefinedDynamicArray class.
##  __add__ will implement '+' Operator Overloading for UserDefinedDyamicArray Class
##  like myList1+myList2 will return a list containing all the elements of myList1 and then myList2
##  --mul__ qill implement '*' Operator Overloading for UserDefinedDyamicArray Class like myList1*3 will return a list having myList1 elements three times.
    myList3=myList1+myList2
    print(myList3)
    myList4 = 2*myList1
    print(myList4)
    


##   Task7: Implement pop(i) function for UserDefinedDynamicArray Class. Implement remove method for UserDefinedDynamicArray Class.
##   By default pop will return the last element from the list and delete that element from the list using del keyword.
##   if i value is specified then we will delete the element at position i and return it to the calling method.
##   remove(x) will delete the element x from the list. If x is present multiple time, it will delete the first occurrence of x.

    p=myList2.pop(1)
    print("Popped element at position 1 from myList2 ",p)

    myList1.remove(140)
    print(myList1)

   

    
if __name__ == '__main__':
    main()
