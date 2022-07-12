def countNodes(linlis):
	if linlis is None:
		return 0
	count = 1
	while linlis.next is not None:
		linlis = linlis.next
		count += 1
	return count


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


head = Node(4)
node2 = Node(2)
node3 = Node(3)
node4 = Node(10)
node5 = Node(2)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


print(countNodes(head))

