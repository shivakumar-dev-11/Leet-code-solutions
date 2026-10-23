class Solution(object):
    def firstMissingPositive(self, nums):
       positive_set = set (nums)
       positive = 1 
       while positive in positive_set:
            positive +=1
       return positive 
    
            
               