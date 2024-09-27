def delete_minimum_elements(hunny_jar_sizes):
	l=[]
	while True:
		if hunny_jar_sizes == []:
			break
		else:
			min_n = min(hunny_jar_sizes)
			l.append(min_n)
			hunny_jar_sizes.remove(min_n)
	print(l)	
			
hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)

hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)
