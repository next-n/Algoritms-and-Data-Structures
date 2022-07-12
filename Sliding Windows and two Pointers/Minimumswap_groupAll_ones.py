from typing import List


def minswap(nums: List[int]):
	totalones = nums.count(1)
	nums = nums + nums
	curzero = 0
	for i in range(totalones):
		if nums[i] == 0:
			curzero += 1
	ans = curzero
	a = (len(nums) // 2) + totalones - 1
	for i in range(totalones, a):
		if nums[i] == 0:
			curzero += 1
		if nums[i - totalones] == 0:
			curzero -= 1
		ans = min(ans, curzero)
		if ans == 0:
			break
	return ans


nums1 = [1, 0, 0, 1, 1, 1]
print(minswap(nums1))
# print(nums1[0:2])
