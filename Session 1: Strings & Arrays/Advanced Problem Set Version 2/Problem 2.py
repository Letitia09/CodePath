def hulk_smash(n):
    res_list=[]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            res_list.append("HulkSmash")
        elif i%3==0:
            res_list.append("Hulk")
        elif i%5==0:
            res_list.append("Smash")
        else:
            res_list.append(str(i))
    print(res_list)
n = 3
hulk_smash(n)

n = 5
hulk_smash(n)

n = 15
hulk_smash(n)
