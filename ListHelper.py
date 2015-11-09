# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        it = self
        while (it and other):
            if it.val != other.val:
                return False
            else:
                it = it.next
                other = other.next
        return it is None and other is None

    def __ne__(self, other):
        return not self.__eq__(other)

class ListHelper(object):
    """docstring for ListHelper"""
    @classmethod
    def listNodeFromList(self, array):
        list_head = None
        list = None
        for item in array:
            if list is None:
                list = ListNode(item)
                list_head = list
            else:
                node = ListNode(item)
                list.next = node
                list = list.next
        return list_head
