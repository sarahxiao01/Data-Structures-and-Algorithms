# 3
from DoublyLinkedList import Doubly_Linked_List


class CompactString():

    def __init__(self, orig_str=''):
        self._data = Doubly_Linked_List()
        for i in range(len(orig_str)):
            if i == 0:
                self._data.insert_last((orig_str[i], 1))
            if i > 0 and orig_str[i] != orig_str[i - 1]:
                self._data.insert_last((orig_str[i], 1))
            else:
                mylast = self._data.last()
                tup1 = mylast[1]
                self._data._trailer._prev._element = (orig_str[i], tup1 + 1)

    def __add__(self, other):
        result = CompactString()
        if self._data._trailer._prev._element[0] == other._data._header._next._element[0]:
            newcount = other._data._header._next._element[1] + self._data._trailer._prev._element[1]
            other._data._header._next._element = other._data._header._next._element[0], newcount
            self._data.delete_last()
        curr = self._data._header._next
        while curr._element != None:
            result._data.insert_last(curr._element)
            curr = curr._next
        mycurr = other._data._header._next
        while mycurr._element != None:
            result._data.insert_last(mycurr._element)
            mycurr = mycurr._next
        return result

    def __lt__(self, other):
        curr = self._data._header._next
        mycurr = other._data._header._next
        while curr != self._data._trailer and mycurr != other._data._trailer:
            if curr._element[0] == mycurr._element[0]:
                if curr._element[1] == mycurr._element[1]:
                    curr = curr._next
                    mycurr = mycurr._next
                elif curr._element[1] < mycurr._element[1]:
                    if curr._next is not self._data._trailer:
                        return curr._next._element[0] < mycurr._element[0]
                    else:
                        return True
                else:
                    if mycurr._next is not other._data._trailer:
                        return curr._element[0] < mycurr._next._element[0]
                    else:
                        return False
            elif curr._element[0] < mycurr._element[0]:
                return True
            else:
                return False

        if mycurr != other._data._trailer and curr == self._data._trailer:
            return True
        return False

    def __eq__(self, other):
        if not self < other:
            if not self > other:
                return True
        return False

    # curr = self._data._header._next
    # mycurr = other._data._header._next
    # while curr != self._data._trailer:
    # 	if mycurr != self._data._trailer and curr._element == mycurr._element:
    # 		curr = curr._next
    # 		mycurr = mycurr._next
    # if curr == self._data._trailer and mycurr == self._data._trailer:
    # 	return True
    # return False

    def __le__(self, other):
        if self < other:
            return True
        else:
            if self == other:
                return True
        return False

    def __gt__(self, other):
        curr = self._data._header._next
        mycurr = other._data._header._next
        while curr != self._data._trailer and mycurr != other._data._trailer:
            if curr._element[0] == mycurr._element[0]:
                if curr._element[1] == mycurr._element[1]:
                    curr = curr._next
                    mycurr = mycurr._next
                elif mycurr._element[1] < curr._element[1]:
                    if mycurr._next is not other._data._trailer:
                        return curr._element[0] > mycurr._next._element[0]
                    else:
                        return True
                else:
                    if curr._next is not self._data._trailer:
                        return curr._next._element[0] > mycurr._element[0]
                    else:
                        return False
            elif curr._element[0] > mycurr._element[0]:
                return True
            else:
                return False
        if mycurr == other._data._trailer and curr != self._data._trailer:
            return True
        return False

    def __ge__(self, other):
        if self > other:
            return True
        else:
            if self == other:
                return True
        return False

    def __repr__(self):
        repstr = ''
        currNode = self._data._header._next
        while currNode is not self._data._trailer:
            for i in range(currNode._element[1]):
                repstr += currNode._element[0]
            currNode = currNode._next
        return repstr

    s1 = CompactString('aaaaabbbaaac')
    s2 = CompactString('aaaaaaacccaaaa')
    print(s1)
    print(s2)
    s3 = s2 + s1
    print(s3)
    print(s1 > s2)