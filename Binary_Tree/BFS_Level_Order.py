def bfs_level_order(n):
	q = [n]
	ans = []
	while q:
		a = q.pop(0)
		ans.append(a.data)
		if a.left:
			q.append(a.left)
		if a.right:
			q.append(a.right)

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

#
# print(bfs_level_order(node1))
