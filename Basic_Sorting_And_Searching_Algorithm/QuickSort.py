def quicksort(arr, low, high):
	if low < high:
		pivotposition = partition(arr, low, high)
		quicksort(arr, low, pivotposition)
		quicksort(arr, pivotposition + 1, high)
	return arr


def partition(arr, low, high):
	pivot = arr[low]
	pivotpoint = low
	leftwall = low

	for i in range(low + 1, high):
		if arr[i] < pivot:
			arr[i], arr[leftwall] = arr[leftwall], arr[i]
			pivotpoint = i
			leftwall += 1
		arr[pivotpoint], arr[leftwall] = arr[leftwall], arr[pivotpoint]

	return leftwall


arr1 = [2, 6, 5, 3, 8, 7, 1, 0]
print(quicksort(arr1, 0, len(arr1)))
