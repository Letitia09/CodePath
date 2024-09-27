#unordered result
def exclusive_elemts(lst1, lst2):
	set_lst1 = set(lst1)
	set_lst2 = set(lst2)
	print(list(set_lst1 ^ set_lst2))
lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
exclusive_elemts(lst1, lst2)

#ordered result
def exclusive_elemts(lst1, lst2):
	uni_lst1 = [i for i in lst1 if i not in lst2]
	uni_lst2 = [i for i in lst2 if i not in lst1]
	print(uni_lst1+uni_lst2)

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
exclusive_elemts(lst1, lst2)
