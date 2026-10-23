class Solution(object):
    def pivotIndex(self, nums):
        totalsum = sum(nums)
        leftsum = 0 
       
        for i in range (0 , len(nums)):
            rightsum = totalsum - leftsum - nums[i]
            if rightsum == leftsum :
                return i
            leftsum +=nums[i]
        return -1