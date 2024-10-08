def reverse_list(lst):
    #print(lst[::-1])
    print([lst.pop() for i in range(len(lst))])
lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
reverse_list(lst)
