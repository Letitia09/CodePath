def get_item(items, x):
	if x<len(items):
		print(items[x])
	else:
		print(None)
items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)
