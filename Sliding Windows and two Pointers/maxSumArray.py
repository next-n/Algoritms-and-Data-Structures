def maxSum(arr, k):
	currentsum = 0
	maxsum = float('-inf')
	for i in range(len(arr)):
		currentsum += arr[i]
		if i >= k - 1:
			maxsum = max(maxsum, currentsum)
			currentsum -= arr[i - (k - 1)]
	return maxsum


arr1 = [2, 4, 5, 3, 81, 5, 2]
print(maxSum(arr1, 3))

