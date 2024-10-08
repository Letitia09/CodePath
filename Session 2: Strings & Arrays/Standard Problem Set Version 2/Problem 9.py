def common_elements(lst1, lst2):
    com_elem = []
    for val in lst1:
        if val in lst2:
            com_elem.append(val)
    print(com_elem)     
            
lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["super speed", "time travel", "dimensional travel"]
common_elements(lst1, lst2)

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["martial arts", "stealth", "master detective"]
common_elements(lst1, lst2)
