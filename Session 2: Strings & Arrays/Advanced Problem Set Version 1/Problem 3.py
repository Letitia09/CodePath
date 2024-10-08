def remove_dupes(items):
    i = 0
    j = count = 1
    while (i < len(items) and j < len(items)):
        if items[i] == items[j]:
            j+=1
        else:
            count+=1
            i=j
            j+=1
    print(count)
        
            
items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
remove_dupes(items)

items = ["extract of malt", "haycorns", "honey", "thistle"]
remove_dupes(items)

items = [1,1,1,2,3]
remove_dupes(items)
