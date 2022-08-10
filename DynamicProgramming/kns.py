def kns(wt, val, towei):
	arr = []
	for x in range(len(wt)+1):
		temp = []
		for j in range(towei+1):
			if not x or not j:
				temp.append(0)
				continue
			if wt[x-1] > j:
				temp.append(0)
			else:
				first = val[x-1] + arr[x-1][j-wt[x-1]]
				sec = arr[x-1][j]
				temp.append(max(first, sec))
		arr.append(temp)
	return arr[len(wt)][towei]
	# return arr


val1 = [1, 4, 5, 7]
wt1 = [1, 3, 4, 5]
totalweight1 = 7
print(kns(wt1, val1, totalweight1))


