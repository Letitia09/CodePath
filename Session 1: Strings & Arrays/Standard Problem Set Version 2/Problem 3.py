def trilogy(year):
	if year == 2005 : 
		print("Batman Begins")
	elif year == 2008:
		print("The Dark Knight")
	elif year == 2012:
		print("The Dark Knight Rises")
	else:
		print(f"Christopher Nolan did not release a Batman movie in {year}.")
year = 2008
trilogy(year)

year = 1998
trilogy(year)

# using dictionaries
# def trilogy(year):
# 	dict_1 = {2005: "Batman Begins",2008:"The Dark Knight",2012:"The Dark Knight Rises"}
# 	if year not in dict_1.keys():
# 		print(f"Christopher Nolan did not release a Batman movie in {year}.")
# 	else:
# 		print(dict_1[year])
		
# year = 2008
# trilogy(year)

# year = 1998
# trilogy(year)
