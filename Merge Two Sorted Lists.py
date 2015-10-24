# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
        """
        merged_list = None

        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val < l2.val:
            merged_list = l1
            l1 = l1.next
        else:
            merged_list = l2
            l2 = l2.next

        start = merged_list

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                merged_list.next = l1
                merged_list = merged_list.next
                l1 = l1.next
            else:
                merged_list.next = l2
                merged_list = merged_list.next
                l2 = l2.next
        if l1 is None:
            merged_list.next = l2
        elif l2 is None:
            merged_list.next = l1

        return start