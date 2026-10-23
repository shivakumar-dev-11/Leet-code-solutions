class Solution(object):
    def runningSum(self, nums):
       num = []
       prefixsum =0
       for i in range (0 , len (nums)):
            prefixsum +=nums[i]
            num.append(prefixsum)
       return num