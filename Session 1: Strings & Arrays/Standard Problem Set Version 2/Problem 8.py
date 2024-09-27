def find_villain(crowd, villain):
	l=[]
	for i in range(len(crowd)):
		if crowd[i] == villain:
			l.append(i)
	print(l)
			
crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
find_villain(crowd, villain)
