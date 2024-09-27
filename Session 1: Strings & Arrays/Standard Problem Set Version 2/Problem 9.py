def get_odds(nums):
	l = []
	for n in nums:
		if n%2 != 0:
			l.append(n)
	print(l)
nums = [1, 2, 3, 4]
get_odds(nums)

nums = [2, 4, 6, 8]
get_odds(nums)
