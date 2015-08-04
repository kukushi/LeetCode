class Solution:
    # @param {TreeNode} root
	# @return {TreeNode}
	def visitNode(self, node):
        if node is None:
		    return

		rightNode = node.right
		node.right = node.left
		node.left = rightNode

		self.visitNode(node.left)
		self.visitNode(node.right)

	def invertTree(self, root):
		self.visitNode(root)
			return root
