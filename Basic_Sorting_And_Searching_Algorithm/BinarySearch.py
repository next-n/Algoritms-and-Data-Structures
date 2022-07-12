def binarySearch(arr, target):
	low = 0
	high = len(arr) - 1
	while not low > high:
		mid = (low + high) // 2
		if target > arr[mid]:
			low = mid + 1
		elif target < arr[mid]:
			high = mid - 1
		else:
			return mid
	return -1


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binarySearch(arr1, 4))
