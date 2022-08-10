from min_max_binarytree import max_binarytree


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def deletenode(root, datavalue):
	# print(root.data)
	if datavalue == root.data:
		if not root.left and not root.right:

			return "None"

		elif root.left and root.right:
			tempdata = max_binarytree(root.left).data
			temp = max_binarytree(root.left)
			root.data = tempdata
			deletenode(temp, tempdata)

		else:
			root.data = root.left.data if root.left else root.right.data
			root.left = root.left.left if root.left else root.right.left
			root.right = root.left.right if root.left else root.right.right

	elif datavalue < root.data:
		if root.left:
			bo = deletenode(root.left, datavalue)
			if bo == "None":
				root.left = None
	elif datavalue > root.data:
		if root.right:
			bo = deletenode(root.right, datavalue)
			if bo == "None":
				root.right = None
	return root
