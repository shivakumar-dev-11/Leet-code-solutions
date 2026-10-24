class Solution(object):
    def thirdMax(self, nums):
        set_nums=list(set(nums))
        set_nums.sort(reverse = True) 
        if len(set_nums) >= 3:
            return set_nums[2]
        return set_nums[0]
      
