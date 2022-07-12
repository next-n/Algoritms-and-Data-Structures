def selectionSort(arr):
	for j in range(len(arr) - 1):
		imin = j
		for i in range(j + 1, len(arr)):
			if arr[imin] > arr[i]:
				imin = i
		arr[imin], arr[j] = arr[j], arr[imin]

	return arr


arr1 = [5, 2, 8, 4]
print(selectionSort(arr1))
