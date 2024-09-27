def sum_of_digits(num):
    r = 0
    while num>0:
        r += num%10
        num //= 10
    print(r)
        
num = 423
sum_of_digits(num)

num = 4
sum_of_digits(num)
