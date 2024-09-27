def make_divisible_by_3(nums):
    count_op = 0
    for i in nums:
        if (i+1) % 3 == 0 or (i-1) % 3 ==0:
            count_op += 1
    print(count_op)
nums = [1, 2, 3, 4]
make_divisible_by_3(nums)

nums = [3, 6, 9]
make_divisible_by_3(nums)
