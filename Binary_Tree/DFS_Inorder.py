def dfs_inorder(n):
	ans = ""

	def helper(node):
		nonlocal ans
		if not node:
			return
		else:
			if node.left:
				helper(node.left)

			ans += str(node.data) + " "

			if node.right:
				helper(node.right)
	helper(n)
	return ans


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

print(dfs_inorder(node1))


