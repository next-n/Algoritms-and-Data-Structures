def selectionSort(arr):
	for j in range(len(arr) - 1):
		imin = j
		for i in range(j + 1, len(arr)):
			if arr[i] < arr[imin]:
				imin = i
	return arr


arr1 = [5, 2, 8, 4]
print(selectionSort(arr1))
