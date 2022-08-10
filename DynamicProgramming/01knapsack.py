def knapsack(wt, val=None, totalweight=0):
	arr = []
	for x in range(len(wt) + 1):
		insidearr = []
		for y in range(totalweight + 1):
			insidearr.append(0)
		arr.append(insidearr)
	for x in range(len(wt) + 1):
		for j in range(totalweight + 1):
			if x == 0 or j == 0:
				continue
			elif wt[x - 1] <= j:
				first = val[x - 1] + arr[x - 1][j - wt[x - 1]]
				sec = arr[x - 1][j]
				arr[x][j] = max(first, sec)
	return arr[len(wt)][totalweight]
	# return arr


val1 = [1, 4, 5, 7]
wt1 = [10, 30, 4, 5]
totalweight1 = 7
print(knapsack(wt1, val1, totalweight1))

# print(ord('g') - 97)
# dci = {[0, 1]: 1}
# print(dci.keys())
# x = set()
# x.add(2)
# x.add(1)
# s = sorted(x)
# print(s)

# print(x)
