class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.height = 1


def getbalance(node):
	left = node.left.height if node.left else 0
	right = node.right.height if node.right else 0
	return left - right


def get_height(node):
	if not node:
		return 0
	else:
		return node.height


def right_rotate(node):
	y = node
	x = y.left
	t2  = x.right
	x.right = y
	y.left = t2
	y.height = 1 + max(get_height(y.left), get_height(y.right))
	x.height = 1 + max(get_height(x.left), get_height(x.right))
	return x


def left_rotate(node):
	x = node
	y = x.right
	t2 = y.left
	y.left = x
	x.right = t2
	x.height = 1 + max(get_height(x.left), get_height(x.right))
	y.height = 1 + max(get_height(y.left), get_height(y.right))
	return y


def insert(root, cur):
	if not root:
		return Node(cur)
	elif cur < root.data:
		root.left = insert(root.left, cur)
	elif cur > root.data:
		root.right = insert(root.right, cur)
	else:
		return root
	root.height = 1 + max(get_height(root.left), get_height(root.right))
	balance = getbalance(root)
	if balance > 1 and cur < root.left.data:
		return right_rotate(root)
	if balance < -1 and cur > root.right.data:
		return left_rotate(root)
	if balance > 1 and cur > root.left.data:
		root.left = left_rotate(root.left)
		return right_rotate(root)
	if balance < -1 and cur < root.right.data:
		root.right = right_rotate(root.right)
		return left_rotate(root)
	return root


def preorder(root):
	if root:
		print(root.data)
		preorder(root.left)
		preorder(root.right)


n1 = Node(3)
n1 = insert(n1, 4)
n1 = insert(n1, 9)
n1 = insert(n1, 5)
n1 = insert(n1, 8)
n1 = insert(n1, 12)
preorder(n1)
