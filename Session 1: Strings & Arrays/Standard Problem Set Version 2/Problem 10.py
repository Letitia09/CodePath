def up_and_down(lst):
	count_odd=count_even=0
	for num in lst:
		if num%2 == 0:
			count_even += 1
		else:
			count_odd += 1
	print(count_odd - count_even) 
lst = [1, 2, 3]
up_and_down(lst)

lst = [1, 3, 5]
up_and_down(lst)

lst = [2, 4, 10, 2]
up_and_down(lst)
