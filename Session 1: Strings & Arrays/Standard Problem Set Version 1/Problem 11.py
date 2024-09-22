def tiggerfy(s):
	char = ['t','i','g','e','r','T','I','G','E','R']
	stri=""
	for i in range(len(s)):
		if s[i] in char:
			stri += ""
		else:
			stri+= s[i]
	print(stri)
s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)
