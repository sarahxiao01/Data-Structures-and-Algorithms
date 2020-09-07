class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass


class Node:#newNode = Node(e)
    
  def __init__(self, element, next = None):   # initialize node's fields
    self._element = element               # reference to user's element
    self._next = next                     # reference to next node


class SinglyLinkedList:
    
  
  #------------------------------- Single Linked List methods -------------------------------
  def __init__(self):
    """Create an empty Linked List."""
    self._head = None                       # reference to the head node
    self._size = 0                          # number of elements in the list

  def __len__(self):#O(1)
    """Return the number of elements in the Linked List."""
    return self._size

  def is_empty(self):#O(1)
    """Return True if the Linked List is empty."""
    return self._size == 0

  def insertAtFirst(self, e):#O(1)#push
    """Add element e to the start of the Linked List."""
    newNode = Node(e)
    newNode._next = self._head
    self._head = newNode
    self._size += 1


    
  def deleteFirst(self):#pop
    """Remove and return the first element from the Linked List.

    Raise Empty exception if the Linked List is empty.
    """
    
    if self.is_empty():
      raise Empty('Linked List is empty')
    temp = self._head._element
    self._head = self._head._next
    self._size -= 1
    return temp


  def unOrderedSearch(self,target):
    # Search for the target element in the Linked List
    currNode = self._head
    while currNode is not None and currNode._element != target:
        currNode = currNode._next
    
    return currNode is not None     


  def printAll(self):
      # print the contents of the Linked List
      result =""
      currNode = self._head
      while currNode is not None:
          result += str(currNode._element)+" "
          currNode = currNode._next
    
      return result[:-1]
