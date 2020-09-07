from doubly_linked_base import _DoublyLinkedBase

# class Empty(Exception):
#   """Error attempting to access an element from an empty container."""
#   pass

#from exceptions import Empty

##INHERITANCE

import Empty

class LinkedDeque(_DoublyLinkedBase):         # note the use of inheritance
  """Double-ended queue implementation based on a doubly linked list."""

  def first(self):
    """Return (but do not remove) the element at the front of the deque.

    Raise Empty exception if the deque is empty.
    """
    if self.is_empty():
      raise Empty("Deque is empty")
    return self._header._next._element ##NEXT!!! ELEMENT!!!
    #to do         # return item just after header

  def last(self):
    """Return (but do not remove) the element at the back of the deque.

    Raise Empty exception if the deque is empty.
    """
    if self.is_empty():
      raise Empty("Deque is empty")
    return self._trailer._prev._element
    #to do        # return item just before trailer

  def insert_first(self, e):
    """Add an element to the front of the deque."""
    #to do       # insert e after header and use inherited method
    insert_between(self, e, self._header, self._header._next)

  def insert_last(self, e):
    """Add an element to the back of the deque."""
    #to do      # insert e before trailer and use inherited method
    insert_between(self, e, self._trailer._prev, self._trailer)

  def delete_first(self):
    """Remove and return the element from the front of the deque.

    Raise Empty exception if the deque is empty.
    """
    if self.is_empty():
      raise Empty("Deque is empty")
    #to do   # delete and return the element after header and use inherited method
    self._delete_node(self, self._header._next)

  def delete_last(self):
    """Remove and return the element from the back of the deque.

    Raise Empty exception if the deque is empty.
    """
    if self.is_empty():
      raise Empty("Deque is empty")
    #to do   # delete and return the element before trailer and use inherited method
    self._delete_node(self, self._trailer._prev)

  def __str__(self):
    result = []
    result.append("Dummy Header <--> ")
    curNode = self._header
    while (curNode._next != self._trailer):
      result.append(str(curNode._next._element) + " <--> ")
      curNode = curNode._next

    result.append(" Dummy Trailer")
    return "".join(result)


deque = LinkedDeque()
print(deque)    # Dummy Header <--> Dummy Trailer
for i in range(4):
  deque.insert_first(i)
for j in range(4):
  deque.insert_last(j + 4)

print(deque) # Dummy Header <--> 3 <--> 2 <--> 1 <--> 0 <--> 4 <--> 5 <--> 6 <--> 7 <--> Dummy Trailer
print("deleting first: ", deque.delete_first())   # 3
print("deleting last: ", deque.delete_last())     # 7
print(deque) # Dummy Header <--> 2 <--> 1 <--> 0 <--> 4 <--> 5 <--> 6 <--> Dummy Trailer 
