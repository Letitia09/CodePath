def left_right_difference(nums):
    diff_l = []
    diff = 0
    for i in range(len(nums)):
        left = nums[ :i]
        right = nums[i+1 : ]
        if left == []:
            diff = - sum(right)
        if right == []:
            diff = sum(left)
        else:
            diff = sum(left) - sum(right)
        diff_l.append(diff)
    print(diff_l)   
            
nums = [10, 4, 8, 3]
left_right_difference(nums)

nums = [1]
left_right_difference(nums)
