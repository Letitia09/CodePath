def smaller_than_current(nums):
    res_list = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if j != i and nums[j] < nums[i]:
                count += 1
        res_list.append(count)
    print(res_list)
nums = [8, 1, 2, 2, 3]
smaller_than_current(nums)

nums = [6, 5, 4, 8]
smaller_than_current(nums)

nums = [7, 7, 7, 7]
smaller_than_current(nums)
