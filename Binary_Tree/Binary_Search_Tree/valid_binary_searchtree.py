def valid(bnode):
	def helper(root, minval, maxval):
		if not root: return True
		if root.val <= minval or root.val >= maxval: return False
		return helper(root.left, minval, root.val) and helper(root.right, root.val, maxval)
	return helper(bnode, float("-inf"), float("inf"))


class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


n1 = Node(7)
n2 = Node(5)
n3 = Node(10)
n4 = Node(3)
n5 = Node(6)
n6 = Node(8)
n7 = Node(11)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7


print(valid(n1))

