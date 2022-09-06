class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.height = 1
		self.size = 1


def height(node):
	if not node:
		return 0
	return node.height


def size(node):
	if not node:
		return 0
	return node.size


def get_balance(node):
	return height(node.left) - height(node.right)


def right_rotate(node):
	x = node
	y = x.left
	t2 = y.right
	y.right = x
	x.left = t2
	x.height = 1 + max(height(x.left), height(x.right))
	y.height = 1 + max(height(y.left), height(y.right))
	x.size = 1 + size(x.left) + size(x.right)
	y.size = 1 + size(y.left) + size(y.right)
	return y


def left_rotate(node):
	y = node
	x = y.right
	t2 = x.left
	x.left = y
	y.right = t2
	x.height = 1 + max(height(x.left), height(x.right))
	y.height = 1 + max(height(y.left), height(y.right))
	x.size = 1 + size(x.left) + size(x.right)
	y.size = 1 + size(y.left) + size(y.right)
	return x


def insert(root, x, count):
	if not root:
		return Node(x), 0
	if x < root.data:
		root.left, count = insert(root.left, x, count)
	elif x > root.data:
		root.right, count = insert(root.right, x, count)
	else:
		return root, count
	root.height = 1 + max(height(root.left), height(root.right))
	root.size = 1 + size(root.left) + size(root.right)
	balance = get_balance(root)
	if x > root.data:
		count += size(root.left) + 1
	if balance > 1:
		if x < root.left.data:
			return right_rotate(root), count
		elif x > root.left.data:
			root.left = left_rotate(root.left)
			return right_rotate(root), count
	if balance < -1:
		if x > root.right.data:
			return left_rotate(root), count
		elif x < root.right.data:
			root.right = right_rotate(root)
			return left_rotate(root), count
	return root, count


def get_count(arr):
	root = None
	ans = []
	for x in range(len(arr)-1, -1, -1):
		if not root:
			root = Node(arr[x])
			ans.append(0)
		else:
			root, count = insert(root, arr[x], 0)
			ans.append(count)
	ans.reverse()
	return ans


arr1 = [12, 8, 5, 9, 4, 3]
print(get_count(arr1))