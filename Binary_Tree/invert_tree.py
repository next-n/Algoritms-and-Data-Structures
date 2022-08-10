from BFS_Level_Order import bfs_level_order


def invert_tree(n):
	if not n:
		return None
	if not n.left and not n.right:
		# print(n.data)
		return n

	left = invert_tree(n.left)
	right = invert_tree(n.right)

	n.right, n.left = left, right
	return n


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
node7 = Node(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

invert_tree(node1)
print(bfs_level_order(node1))
