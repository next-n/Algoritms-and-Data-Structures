def detect(node):
	slow, fast = node, node
	count = 0
	while fast.next:
		count += 1
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			# countlinkedlistwithloop = 1
			ptr1, ptr2 = fast, fast
			k = 1
			while ptr1.next != ptr2:
				ptr1 = ptr1.next
				k += 1
			ptr1, ptr2 = node, node
			for i in range(k):
				ptr2 = ptr2.next
			while ptr1 != ptr2:
				ptr1 = ptr1.next
				ptr2 = ptr2.next
				k += 1
			# print(k)

			return str(k) + " " + "have loop"
	while slow:
		count += 1
		slow = slow.next
	# print(count)
	return str(count) + "no loop"


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


head = Node(4)
node2 = Node(2)
node3 = Node(3)
node4 = Node(10)
node5 = Node(40)
node6 = Node(6)
node7 = Node(7)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = head
# node5.next = node2

print(detect(head))

# iii = 3
# for i in range(iii):
# 	iii+=1
# 	print(i)