def move_zeroes(lst):
    ind = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[ind],lst[i] = lst[i],lst[ind]
            ind += 1
    print(lst)
            
lst = [1, 0, 2, 0, 3, 0]
move_zeroes(lst)
"""
Input: [1, 0, 2, 0, 3, 0]
Output: [1, 2, 3, 0, 0, 0]
"""
