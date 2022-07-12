def bubbleSort(arr):
	for i in range(1, len(arr)):
		for j in range(len(arr) - 1):
			if arr[j] > arr[j + 1]:
				arr[j + 1], arr[j] = arr[j], arr[j + 1]
	return arr


arr1 = [90, 6, 7, 9, 3]
print(bubbleSort(arr1))

