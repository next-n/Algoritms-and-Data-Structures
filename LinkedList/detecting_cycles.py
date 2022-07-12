def detect(node):
	slow, fast = node, node
	while fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			return True
	return False


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
node5.next = node2

print(detect(head))
