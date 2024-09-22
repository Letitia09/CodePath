def split_haycorns(quantity):
	l=[]
	for i in range(1,quantity//2+1):
		if quantity%i == 0:
			l.append(i)
	l.append(quantity)
	print(l)
		
quantity = 360
split_haycorns(quantity)

quantity = 12345
split_haycorns(quantity)

quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)
