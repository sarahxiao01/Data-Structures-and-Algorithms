#4

from DoublyLinkedList import Doubly_Linked_List

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
	def merge_sublists(srt_lnk_lst1, srt_lnk_lst2, Node1, Node2):
		if Node1._element is None and Node2._element is None:
			new = Doubly_Linked_List()
			return new
		else:
			if Node1._element is not None and Node2._element is not None:
				if Node1._element < Node2._element:
						now = merge_sublists(srt_lnk_lst1, srt_lnk_lst2, Node1._next, Node2)
						now.insert_first(Node1._element)
				else:
						now = merge_sublists(srt_lnk_lst1, srt_lnk_lst2, Node1, Node2._next)
						now.insert_first(Node2._element)
				return now
		if Node1._element is not None and Node2._element is None:
			now = merge_sublists(srt_lnk_lst1, srt_lnk_lst2, Node1._next, Node2)
			now.insert_first(Node1._element)
			return now
		if Node1._element is None and Node2._element is not None:
			now = merge_sublists(srt_lnk_lst1, srt_lnk_lst2, Node1, Node2._next)
			now.insert_first(Node2._element)
			return now
	return merge_sublists(srt_lnk_lst1, srt_lnk_lst2, srt_lnk_lst1._header._next, srt_lnk_lst2._header._next)

# lst1 = Doubly_Linked_List()
# lst1.insert_last(1)
# lst1.insert_last(3)
# lst1.insert_last(5)
# lst1.insert_last(6)
# lst1.insert_last(8)
# print(lst1)

# lst2 = Doubly_Linked_List()
# lst2.insert_last(2)
# lst2.insert_last(3)
# lst2.insert_last(5)
# lst2.insert_last(10)
# lst2.insert_last(15)
# lst2.insert_last(18)
# print(lst2)

# lst3 = merge_linked_lists(lst1, lst2)
# print(lst3)