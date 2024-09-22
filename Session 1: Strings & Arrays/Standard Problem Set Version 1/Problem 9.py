def can_pair(item_quantities):
	for i in range(len(item_quantities)):
		if item_quantities[i]%2 != 0:
			print(False)
			break
	else:
		print(True)
item_quantities = [2, 4, 6, 8]
can_pair(item_quantities)

item_quantities = [1, 2, 3, 4]
can_pair(item_quantities)

item_quantities = []
can_pair(item_quantities)
