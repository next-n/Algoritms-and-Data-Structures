class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.height = 1
		self.size = 1


def size(node):
	if not node:
		return 0
	return node.size


def get_height(node):
	if not node:
		return 0
	return node.height


def get_balance(node):
	return get_height(node.left) - get_height(node.right)


def right_rotata(node):
	x = node
	y = x.left
	t2 = y.right
	y.right = x
	x.left = t2
	x.height = 1 + max(get_height(x.left), get_height(x.right))
	y.height = 1 + max(get_height(y.left), get_height(y.right))
	x.size = 1 + size(x.left) + size(x.right)
	y.size = 1 + size(y.left) + size(y.right)
	return y


def left_rotate(node):
	y = node
	x = y.right
	t2 = x.left
	x.left = y
	y.right = t2
	x.height = 1 + max(get_height(x.left), get_height(x.right))
	y.height = 1 + max(get_height(y.left), get_height(y.right))
	x.size = 1 + size(x.left) + size(x.right)
	y.size = 1 + size(y.left) + size(y.right)
	return x


def insert(root, x, count, indx):
	# print(x)
	if not root:
		return Node(x)
	elif x < root.data:
		root.left = insert(root.left, x, count, indx)
	elif x > root.data:
		root.right = insert(root.right, x, count, indx)
		count[indx] += 1 + size(root.left)

	else:
		return root
	root.height = 1 + max(get_height(root.left), get_height(root.right))
	root.size = 1 + size(root.left) + size(root.right)
	balance = get_balance(root)
	if balance > 1 and x < root.left.data:
		return right_rotata(root)
	if balance < -1 and x > root.right.data:
		return left_rotate(root)
	if balance > 1 and x > root.left.data:
		root.left = left_rotate(root.left)
		return right_rotata(root)
	if balance < -1 and x < root.right.data:
		root.right = right_rotata(root.right)
		return left_rotate(root)
	return root


def preorder(root, arr):
	if root:
		arr.append(root.data)
		preorder(root.left, arr)
		preorder(root.right, arr)
	return arr


def find_count(arr):
	root = None
	ans = []
	for x in arr:
		ans.append(0)
	for x in range(len(arr)-1, -1, -1):
		# print(arr[x], "xxra")
		if not root:
			root = Node(arr[x])
		else:
			root = insert(root, arr[x], ans, x)
			# print(ans)

	return ans


arr1 = [12, 8, 5, 9, 4, 3]
print(find_count(arr1))

# n1 = Node(3)
# n1 = insert(n1, 4)
# n1 = insert(n1, 9)
# n1 = insert(n1, 5)
# n1 = insert(n1, 8)
# n1 = insert(n1, 12)
# preorder(n1)