def lengthOfLongestSubstring(s: str) -> int:

	j = 0
	maxvalue = 0
	arr = []
	for i in range(len(s)):

		a = s[i]

		while s[i] in arr:

			arr.remove(s[j])

			j += 1
		arr.append(a)
		maxvalue = max(maxvalue, i - j + 1)
	return maxvalue


st = 'abcabcbb'

print(lengthOfLongestSubstring(st))
