def get_last(items):
	if items == []:
		print(None)
	else:
		print(items[len(items)-1])
items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
get_last(items)

items = []
get_last(items)
