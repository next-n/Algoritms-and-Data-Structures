def insertionSort(arr):
	for i in range(1, len(arr)):
		j = i
		while j > 0 and arr[j - 1] > arr[j]:
			arr[j - 1], arr[j] = arr[j], arr[j - 1]
			j -= 1
	return arr


arr1 = [6, 3, 8, 1]
print(insertionSort(arr1))

