def good_pairs(pile1, pile2, k):
    count_pair=0
    for i in pile1:
        for j in pile2:
            if i%(j*k)==0:
                count_pair+=1
    print(count_pair)
pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
good_pairs(pile1, pile2, k)

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
good_pairs(pile1, pile2, k)