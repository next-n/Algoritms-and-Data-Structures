def sisum(arri, target):
	# arri.sort()
	ans = []
	for x in range(len(arri)):
		temp = []
		for j in range(target + 1):
			if not j:
				temp.append(True)
				continue
			if not x:
				if arri[x] == j:
					temp.append(True)
				else:
					temp.append(False)
				continue
			if arri[x] > j:
				temp.append(ans[x - 1][j])
			else:
				# print(x, j, arri[x])
				temp.append(ans[x - 1][j - arri[x]] or ans[x-1][j])
		ans.append(temp)
	return ans[len(arri) - 1][target]
	# return ans

# return ans


arr1 = [2, 3, 7, 11]
target1 = 5
arr2 = [1, 5, 11, 5]
target2 = 11
arr3 = [23, 13, 11, 7, 6, 5, 5]
target3 = 35
arr4 = [3, 2, 7, 4, 2, 5, 3, 7, 5, 4]
target4 = 21
print(sisum(arr3, target3))
# print(sum(arr4))


