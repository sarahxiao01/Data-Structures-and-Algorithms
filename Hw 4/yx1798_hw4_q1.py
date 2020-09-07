#1

from DoublyLinkedList import Doubly_Linked_List

class LinkedQueue():
    def __init__(self, N = 10):
        self._data = Doubly_Linked_List()
        self._size = 0   

    def __len__(self):
        return self._size
       

    def is_empty(self):
        return self._size == 0 


    def first(self):#O(1)
        if self.is_empty():
            raise Empty("Queue is Empty") 
        return self._header._next._element

    def dequeue(self):#O(1)
        if self.is_empty():
            raise Empty("Queue is Empty") 
        self._size -= 1 
        return self._data.delete_first()  ##???

    def enqueue(self, e): #O(1)
        self._size += 1
        self._data.insert_last(e) ##???


    def __str__(self):
        ''' You can simply print self._data '''
        return str(self._data)   #print directly or as string

# myqueue = LinkedQueue()
# myqueue.enqueue(3)
# myqueue.enqueue(6)
# myqueue.enqueue(5)
# myqueue.enqueue(2)
# myqueue.enqueue(8)
# print(myqueue)
# myqueue.dequeue()
# myqueue.dequeue()
# print(myqueue)

# queue = LinkedQueue()

#         # Enqueue 0, 1, 2, 3, 4, 5, 6, 7
# for i in range(8):
#     queue.enqueue(i)
# print(queue)   # [0, 1, 2, 3, 4, 5, 6, 7, None, None] 

#         # Dequeue 5 times.
# for j in range(5):
#     queue.dequeue()
# print(queue)  # [None, None, None, None, None, 5, 6, 7, None, None]

#         # Enqueue 8, 9, 10, 11, 12
# for k in range(5):
#     queue.enqueue(k + 8)
# print(queue)  # [10, 11, 12, None, None, 5, 6, 7, 8, 9]

