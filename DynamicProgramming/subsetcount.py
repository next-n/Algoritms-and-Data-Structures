def countsubset(nums, target):
	arr = []
	for x in range(len(nums)):
		temp = []
		for t in range(target + 1):
			if not t:
				temp.append(1)
				continue
			if not x:
				if nums[x] == t:
					temp.append(1)
				else:
					temp.append(0)
			else:
				if nums[x] > t:
					temp.append(arr[x - 1][t])
				else:
					temp.append(arr[x - 1][t - nums[x]] + arr[x - 1][t])
		arr.append(temp)
	return arr[len(nums) - 1][target]


# return arr


def countsubset_recursive(nums, target):
	def rec(numsi, targeti, i):
		# print(targeti, i)
		if not targeti:
			# print("inside target 0", targeti, i)
			return 1
		elif i < 0:
			return 0
		elif targeti < 0:
			return 1
		elif targeti < nums[i]:
			return rec(numsi, targeti, i - 1)
		else:
			return rec(numsi, targeti - nums[i], i - 1) + rec(numsi, targeti, i - 1)

	return rec(nums, target, len(nums) - 1)


nums1 = [1, 1, 1, 1]
target1 = 1
nums2 = [2, 4, 6, 10]
# nums2.sort()
target2 = 16
# print(countsubset_recursive(nums2, target2))

s = None

print(s)
