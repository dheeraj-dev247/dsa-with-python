def rev_sub_array_using_loop(left,right,nums):
    print(nums)
    while left < right:
        print('i am inside')
        nums[left],nums[right] = nums[right],nums[left]
        left +=1
        right -=1
    return nums

print(rev_sub_array_using_loop(2,4, [1, 2, 3, 4, 5, 6, 7])) 