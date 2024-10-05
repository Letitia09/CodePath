def remove_name(people, secret_identity):
	for ind,val in enumerate(people):
	    if val == secret_identity:
	        people.pop(ind)
	print(people)
people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
secret_identity = 'Bruce Wayne'
remove_name(people, secret_identity)
