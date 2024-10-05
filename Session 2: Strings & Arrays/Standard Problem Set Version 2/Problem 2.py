def count_evens(lst):
    count_evenstr = 0
    for string in lst:
        if len(string)%2 == 0:
            count_evenstr += 1
    print(count_evenstr)
lst = ["na", "nana", "nanana", "batman", "!"]
count_evens(lst)

lst = ["the", "joker", "robin"]
count_evens(lst)

lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
count_evens(lst)
