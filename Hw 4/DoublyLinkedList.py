class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass


class Doubly_Linked_List():
  """A class providing a Doubly Linked List representation"""
  class _Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    
    def __init__(self, element, prev = None, next = None):            # initialize node's fields
      self._element = element                           # user's element
      self._prev = prev                                 # previous node reference
      self._next = next                                 # next node reference

  #-------------------------- list constructor --------------------------

  def __init__(self):
    """Create an empty list."""
    self._header = self._Node(None, None, None)
    self._trailer = self._Node(None, None, None)
    self._header._next = self._trailer                  # trailer is after header
    self._trailer._prev = self._header                  # header is before trailer
    self._size = 0            

  #-------------------------- nonpublic utilities --------------------------

  def _insert_between(self, e, predecessor, successor):
    """Add element e between two existing nodes and return new node."""
    newest = self._Node(e, predecessor, successor)      # linked to neighbors
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest

  def _delete_node(self, node):
    """Delete nonsentinel node from the list and return its element."""
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    element = node._element                             # record deleted element
    node._prev = node._next = node._element = None      # deprecate node
    return element                                      # return deleted element

#-----------------------public accessors & modifiers --------------------------

  def __len__(self):
    """Return the number of elements in the list."""
    return self._size

  def is_empty(self):
    """Return True if list is empty."""
    return self._size == 0


  def first(self):
    """Return (but do not remove) the element at the front of the DLL.

    Raise Empty exception if the DLL is empty.
    """
    if self.is_empty():
      raise Empty("DLL is empty")
    return self._header._next._element

  def last(self):
    """Return (but do not remove) the element at the back of the DLL.

    Raise Empty exception if the DLL is empty.
    """
    if self.is_empty():
      raise Empty("DLL is empty")
    return self._trailer._prev._element

  def insert_first(self, e):
    """Add an element to the front of the DLL."""
    self._insert_between(e,self._header,self._header._next)

  def insert_last(self, e):
    """Add an element to the back of the DLL."""
    self._insert_between(e,self._trailer._prev,self._trailer)

  def delete_first(self):
    """Remove and return the element from the front of the DLL.

    Raise Empty exception if the DLL is empty.
    """
    if self.is_empty():
      raise Empty("DLL is empty")
    return self._delete_node(self._header._next)

  def delete_last(self):
    """Remove and return the element from the back of the DLL.

    Raise Empty exception if the DLL is empty.
    """
    if self.is_empty():
      raise Empty("DLL is empty")
    return self._delete_node(self._trailer._prev)

  def __str__(self):
    result = []
    result.append("Dummy Header <--> ")
    curNode = self._header
    while (curNode._next != self._trailer):
      result.append(str(curNode._next._element) + " <--> ")
      curNode = curNode._next

    result.append(" Dummy Trailer")
    return "".join(result)