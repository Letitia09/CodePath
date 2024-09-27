def goldilocks_approved(nums):
    l_max = max(nums)
    l_min = min(nums)
    nums.remove(l_max)
    nums.remove(l_min)
    if nums == []:
        print(-1)
    else:
        print(nums[0])
nums = [3, 2, 1, 4]
goldilocks_approved(nums)

nums = [1, 2]
goldilocks_approved(nums)

nums = [2, 1, 3]
goldilocks_approved(nums)
