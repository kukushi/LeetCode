# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
        # @param {ListNode} node
	    # @return {void} Do not return anything, modify node in-place instead.
	        def deleteNode(self, node):
		            pre = None
			        while node.next != None:
					    node.val = node.next.val
						pre = node
						node = node.next
					pre.next = None
										            
