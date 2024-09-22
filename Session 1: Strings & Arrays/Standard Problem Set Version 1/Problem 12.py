def locate_thistles(items):
	lis=[]
	for i in range(len(items)):
		if items[i] == "thistle":
			lis.append(i)
	print(lis)
			
items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)
