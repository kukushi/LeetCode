# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def dfs(self, node, count, target):
        if self.found:
            return
        count += node.val
        if count == target and node.left is None and node.right is None:
            self.found = True
            return
        if node.left is not None:
            self.dfs(node.left, count, target)
        if node.right is not None:
            self.dfs(node.right, count, target)

    def hasPathSum(self, root, sum):
        """
            :type root: TreeNode
            :type sum: int 
            :rtype: bool
        """
        self.found = False
        if root != None:
              self.dfs(root, 0, sum)
        return self.found