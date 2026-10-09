class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        sum = nums[0]       
        for i in range (1 , len(nums)):
            if sum < 0:
                sum = 0 
            sum += nums[i]
            if sum > maxsum :
                maxsum = sum  
        return maxsum
