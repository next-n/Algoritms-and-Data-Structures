from search_binary_tree import searchbinarytree
from min_max_binarytree import *
from delete import *
from check_valid_binarysearchtree import *


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


n10 = Node(10)


def insert(root, n):

	if n.data == root.data:
		return None
	elif n.data < root.data:
		if not root.left:
			root.left = n
		else:
			insert(root.left, n)
	elif n.data > root.data:
		if not root.right:
			root.right = n
		else:
			insert(root.right, n)
		pass


n10 = Node(10)


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


def insertarray(arr):
	global n10
	for x in arr:
		temn = Node(x)
		insert(n10, temn)
	return bfs_level_order(n10)


arr1 = [23, 7, 5, 3, 89]
print(insertarray(arr1))
# print(searchbinarytree(n10, 90))
# print(min_binarytree(n10))
# print(max_binarytree(n10))
print(deletenode(n10, 10))
print(bfs_level_order(n10))

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
print(isvalid(node1))



