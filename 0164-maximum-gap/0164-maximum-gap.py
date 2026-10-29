class Solution(object):
    def maximumGap(self, nums):
       nums.sort()
       maxdiffer = 0 
       n = len(nums)
       for i in range (0 , n-1):
            sub =  nums[i+1] - nums[i]
            if sub > maxdiffer:
                maxdiffer = sub 
       return maxdiffer
               