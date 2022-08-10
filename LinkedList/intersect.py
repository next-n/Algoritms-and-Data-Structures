# https://leetcode.com/problems/intersection-of-two-linked-lists/
def intersect(heada, headb):
	a, b = heada, headb
	while a != b:
		a = headb if a is None else a.next
		b = heada if b is None else b.next
	return a

