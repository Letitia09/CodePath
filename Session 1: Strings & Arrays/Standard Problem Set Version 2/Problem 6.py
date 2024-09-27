def squared(numbers):
	print(list(map(lambda x: x ** 2, numbers)))
	# or 
	#print([lambda x: x * x for x in numbers])
numbers = [1, 2, 3]
squared(numbers)
