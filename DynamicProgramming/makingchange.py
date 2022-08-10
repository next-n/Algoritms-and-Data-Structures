def coinChange(coins, amount):
	coins.sort()
	arr = []
	for x in range(len(coins)):
		temp = []
		for t in range(amount+1):
			if not t:
				temp.append(0)
				continue
			if not x:
				if coins[x] > t:
					temp.append(-1)
				elif temp[t-coins[x]] == -1:
					temp.append(-1)
				else:
					temp.append(1+temp[t-coins[x]])
			elif coins[x] > t or temp[t-coins[x]] == -1:
				temp.append(arr[x-1][t])
			else:
				tem = min(1+temp[t-coins[x]], arr[x-1][t])if arr[x-1][t] != -1 else 1+temp[t-coins[x]]
				temp.append(tem)
		arr.append(temp)
	return arr[len(coins)-1][amount]

	# return arr


coins1 = [186, 419, 83, 408]
amount1 = 6249
coins2 = [5, 6]
amount2 = 16

print(coinChange(coins1, amount1))
