def count_digits(n):
    if n == 0:
        print(1)
    else:
        count_digit = 0
        while n>0:
            n = n // 10
            count_digit += 1
        print(count_digit)
n = 964
count_digits(n)

n = 0
count_digits(n)
