def running_sum(superhero_stats):
	sum = 0
	for i in range(len(superhero_stats)):
		sum += superhero_stats[i]
		superhero_stats[i] = sum
	print(superhero_stats)
		
superhero_stats = [1, 2, 3, 4]
running_sum(superhero_stats)

superhero_stats = [1, 1, 1, 1, 1]
running_sum(superhero_stats)

superhero_stats = [3, 1, 2, 10, 1]
running_sum(superhero_stats)
