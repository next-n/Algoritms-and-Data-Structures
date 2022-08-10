class Node:
	def __init__(self, data):
		self.val = data
		self.next = None


def isPalindrome(head) -> bool:
	rev = None
	slow = fast = head
	while fast and fast.next:
		fast = fast.next.next
		# if fast:
		# 	print("fast", fast.val)
		temp = rev
		# print('temp', temp)
		rev = slow
		# print('rev', rev.val)
		slow = slow.next
		# print('slow', slow.val)
		rev.next = temp
	if fast:
		slow = slow.next
		print('if fast', slow.val)
	while rev and rev.val == slow.val:
		print('hayhay')
		slow = slow.next
		rev = rev.next
	return not rev


n1 = Node(1)
n2 = Node(2)
n3 = Node(2)
n4 = Node(1)

n1.next = n2
n2.next = n3
n3.next = n4

# print(isPalindrome(n1))
a1 = [0, 2]
a2 = [1, 4]
