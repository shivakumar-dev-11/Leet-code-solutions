class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = float('-inf')
        presum = 0       
        for i in range (0, len(nums)):
            presum += nums[i]
            if presum > maxsum:
                maxsum = presum
            if presum < 0:
                presum = 0 
        return maxsum
