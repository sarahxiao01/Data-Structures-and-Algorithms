from queue import Empty
from queue import Full

class ArrayQueue():

    #DEFAULT_CAPACITY = 10
    
    def __init__(self, N = 10):
        self._data = [None] * N
        self._size = 0   
        self._front = 0
    ## FIXED size queue, 0
    ## Front starts with 0

    def __len__(self):
        return self._size
        #pass

        #return Size, Size  not len!!!

    def is_empty(self):
        return self._size == 0 #len(self)==0
        #pass

        #Size = 0

    def first(self):#O(1)
        ''' Return the value stored at the front of the queue '''
        if self.is_empty():
            raise Empty("Queue is Empty") #ERROR
        return self._data[self._front]
        #pass

        #FRONT is first
        #raise ERROR if queue empty

    def dequeue(self):#O(1)
        ''' Remove and return the value stored at the front of the queue '''
        if self.is_empty():
            raise Empty("Queue is Empty")    #ERROR
        temp = self._data[self._front]  
        self._data[self._front] = None
        self._front =  (self._front+1)%len(self._data) #!!!!!!      REMAINDER over len(self._data)
        self._size -= 1
        return temp
        #pass

        #from FRONT!!! 
        #Raise exception if queue empty
        #Make reference, set as None, set Front as new mod, decrease Size, return reference
        #CHANGE index every time enqueue/ dequeue

    def enqueue(self, e): #O(1)
        if self._size == len(self._data):
            raise Full("Full Queue Exception")    #ERROR
        ''' Insert e at the end of the queue '''
        avail = (self._front+self._size)%len(self._data)#N      #!!!!!!
        self._data[avail] = e
        self._size += 1
        #pass

        #from Back!!! (Front + self.size)
        #Raise exception if queue full
        #Make avail, set as New, increase Size
        #CHANGE index every time enqueue/ dequeue

    def __str__(self):
        ''' You can simply print self._data '''
        return str(self._data)   #print directly or as string

def main():
    # Empty Queue, size 10.
    queue = ArrayQueue()

    # Enqueue 0, 1, 2, 3, 4, 5, 6, 7
    for i in range(8):
        queue.enqueue(i)
    print(queue)   # [0, 1, 2, 3, 4, 5, 6, 7, None, None] 

    # Dequeue 5 times.
    for j in range(5):
        queue.dequeue()
    print(queue)  # [None, None, None, None, None, 5, 6, 7, None, None]

    # Enqueue 8, 9, 10, 11, 12
    for k in range(5):
        queue.enqueue(k + 8)
    print(queue)  # [10, 11, 12, None, None, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    main()

