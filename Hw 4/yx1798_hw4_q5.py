#5

from SinglyLinkedList import SinglyLinkedList
from SinglyLinkedList import Node

def findLoop(linkedList):
	slow = linkedList._head
	fast = linkedList._head
	while slow is not None and slow._next is not None:
		slow = slow._next
		if fast is not None: 
			fast = fast._next
			fast = fast._next
		else: 
			return False 
		if slow == fast:
			return True
	return False


ll = SinglyLinkedList()
n5 = Node(5)
n4 = Node(4, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

n5._next = n3

# setting the head to the created linked list
ll._head = n1

# testing to see if the linked list loops
curr = ll._head
for i in range(8):
  print curr._element
  curr = curr._next

# lst = SinglyLinkedList()
# n4 = Node(4)
# n3 = Node(3, n4)
# n2 = Node(2, n3)
# n1 = Node(1, n2)
# lst._head = n1
print(findLoop(ll))
# print(findLoop(lst))