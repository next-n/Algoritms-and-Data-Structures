# def checkthat(r):
# 	if (not r.left or r.data > r.left.data) and (not r.right or r.data < r.right.data):
# 		# print('hi')
# 		return True
# 	return False
#
#
# def isvalid(root):
# 	# print(root.data)
# 	while root.left or root.right:
# 		if root.left:
# 			if not checkthat(root.left):
# 				return False
# 			root = root.left
# 		if root.right:
# 			if not checkthat(root.right):
# 				return False
# 			root = root.right
#
# 	return True
#
#
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.left = None
# 		self.right = None
#
#
# n1 = Node(7)
# n2 = Node(5)
# n3 = Node(10)
# n4 = Node(3)
# n5 = Node(6)
# n6 = Node(4)
# n7 = Node(11)
# n1.left = n2
# n1.right = n3
# n2.left = n4
# n2.right = n5
# n3.left = n6
# n3.right = n7
#
#
# print(isvalid(n1))
