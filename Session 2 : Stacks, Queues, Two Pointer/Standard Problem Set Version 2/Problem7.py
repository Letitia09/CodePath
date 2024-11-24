
#Problem 7: Check if a Signal Occurs as a Prefix in Any Transmission

def is_prefix_of_signal(transmission, searchSignal):
    str_list = transmission.split()
    count, flag = 0, 0
    n = len(searchSignal)-1
    for i in str_list:
        count+=1
        if searchSignal in i and searchSignal[n] == i[n] and searchSignal[0] == i[0]:
            flag = 1
            return count
    if flag == 0 :
        return -1
     
print(is_prefix_of_signal("hellohello hellohellohello", "ell")) 
print(is_prefix_of_signal("this problem is an easy problem", "pro")) 
print(is_prefix_of_signal("i am tired", "you")) 
