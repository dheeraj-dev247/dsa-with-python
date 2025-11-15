def rev_sub_array_using_loop(left,right,nums):
    left -= 1
    right -=1
    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left +=1
        right -=1
    return nums

print(rev_sub_array_using_loop(2,4, [1, 2, 3, 4, 5, 6, 7])) 


## Solution on the GFG
class Solution:
	def reverseSubArray(self,arr,l,r):
		self.helper_func(arr,l-1,r-1)
		return arr
		
	def helper_func(self,arr,l,r):
	    if l >= r:
	        return 
	    arr[l],arr[r] = arr[r],arr[l]
	    self.helper_func(arr,l+1,r-1)