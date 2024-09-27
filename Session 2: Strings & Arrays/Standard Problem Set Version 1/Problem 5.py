def final_value_after_operations(operations):
	trigger = 1
	for i in operations:
		if i == "flouncy" or i == "bouncy":
			trigger += 1
		elif i == "trouncy" or i == "pouncy":
			trigger -= 1
	print(trigger)
			
operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)
