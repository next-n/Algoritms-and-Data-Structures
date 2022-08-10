def counting_sort(nums):
	def numberToBase(n, b):
		if n == 0:
			return [0]
		digits = []
		while n:
			digits.append(int(n % b))
			n //= b

		return digits[::-1]
	s = []
	for x in nums:
		t = numberToBase(x, len(nums))
		s.append(t)
	c = True
	i = 0
	j = 0
	# print(s)
	count = 0
	while c:
		count += 1
		# if count == 3:
		# 	break
		# print('c')
		temp = []
		for _ in range(len(nums)):
			# print('asd')
			temp.append([])

		while i < len(s):
			# print(i, len(s))
			check = len(s[i]) - 1 - j
			if check < 0:
				c = False
				temp[0].append(s[i])
				i += 1
				continue
			c = True
			# print(s[i][check])
			temp[s[i][check]].append(s[i])
			# print("temp", temp)
			# print('a')
			i += 1
		s = []
		# print('b')
		for ap in temp:
			# print(ap)
			while ap:
				# print('asdf')
				s.append(ap.pop(0))
		# print(s)
		j += 1
		i = 0
		# count += 1

	ans = []
	# print(s)
	for t in s:
		ti = [str(i) for i in t]
		tempstr = ''.join(ti)
		tint = int(tempstr, len(nums))
		ans.append(tint)
	return ans


print(counting_sort([3, -1]))




