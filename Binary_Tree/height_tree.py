def getheight(n):
	if not n:
		return 0
	leftheight = getheight(n.left)
	rightheight = getheight(n.right)

	if leftheight > rightheight:
		return leftheight + 1
	else:
		return rightheight + 1


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


print(getheight(node1))
