def fabo(n):
	arr = []
	index = 0
	while index < n:
		if index < 2:
			arr.append(1)
		else:
			arr.append(arr[index - 1] + arr[index - 2])
		index += 1
	return arr[n-1]


print(fabo(50))

