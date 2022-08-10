def searchbinarytree(root, datavalue):
	# print(root.data)
	bo = False
	if root.data == datavalue:
		return True
	elif datavalue < root.data:
		if root.left:
			bo = searchbinarytree(root.left, datavalue)
	elif datavalue > root.data:
		if root.right:
			bo = searchbinarytree(root.right, datavalue)
	return bo
