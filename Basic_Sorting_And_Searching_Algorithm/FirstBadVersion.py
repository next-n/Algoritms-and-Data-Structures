# https://leetcode.com/problems/first-bad-version/

bad = 7


def isBadVersion(n):
	global bad
	if n < bad:
		return False;
	else:
		return True


def firstBadVersion(total):
	low = 1
	high = total
	if isBadVersion(1):
		return 1

	while not low > high:
		mid = (low + high) // 2
		if isBadVersion(mid) and not isBadVersion(mid - 1):
			return mid
		if isBadVersion(mid):
			high = mid - 1
		else:
			low = mid + 1


print(firstBadVersion(8))
