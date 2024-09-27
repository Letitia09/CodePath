def harvest(vegetable_patch):
	count = 0
	for i in range(len(vegetable_patch)):
		for j in range(len(vegetable_patch[i])):
			if vegetable_patch[i][j] == 'c':
				count += 1
	print(count)
vegetable_patch = [
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]
harvest(vegetable_patch)
