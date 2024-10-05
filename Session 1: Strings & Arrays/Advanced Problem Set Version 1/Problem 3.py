def tiggerfy(word):
	word = word.lower()
	word = word.replace('t','')
	word = word.replace('i','')
	word = word.replace('gg','')
	word = word.replace('er','')
	print(word)
word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)
