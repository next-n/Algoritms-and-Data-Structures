def max_tree(n):
	if not n:
		return -999999
	if not n.left and not n.right:
		return n.data

	left_value = max_tree(n.left)
	right_value = max_tree(n.right)

	return max(left_value, right_value, n.data)


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


print(max_tree(node1))


