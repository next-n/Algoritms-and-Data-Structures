def min_binarytree(n):
	while n.left:
		n = n.left
	return n.data


def max_binarytree(n):
	while n.right:
		n = n.right
	return n
