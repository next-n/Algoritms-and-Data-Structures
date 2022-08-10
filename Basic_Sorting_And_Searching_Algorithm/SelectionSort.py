def selectionSort(arr):
	for j in range(len(arr) - 1):
		imin = j
		for i in range(j + 1, len(arr)):
			if arr[imin] > arr[i]:
				imin = i
		arr[imin], arr[j] = arr[j], arr[imin]

	return arr


def selectionSort_selectlargest(arr):
	def helper(a, indx):
		if not indx:
			return 0
		j = helper(a, indx - 1)
		if arr[j] > arr[indx]:
			return j
		return indx

	for i in range(len(arr) - 1, 0, -1):
		imax = helper(arr, i)
		arr[i], arr[imax] = arr[imax], arr[i]
	return arr


arr1 = [5, 2, 8, 4]
print(selectionSort_selectlargest(arr1))





