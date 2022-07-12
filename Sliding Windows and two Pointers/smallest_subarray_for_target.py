def smallest(arr, target):
	minwindowsize = float('inf')
	windowstart = 0
	currentsum = 0
	for windowend in range(len(arr)):
		currentsum += arr[windowend]
		while currentsum >= target:
			minwindowsize = min(minwindowsize, windowend - windowstart + 1)
			currentsum -= arr[windowstart]
			windowstart += 1
	return minwindowsize


arr1 = [4, 2, 2, 7, 8, 1, 2, 8, 10]
print(smallest(arr1, 8))
