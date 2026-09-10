class Solution(object):
    def removeDuplicates(self, nums):
        k = 0

        for j in range(1, len(nums), +1):
            if nums[k] != nums[j]:
                k += 1
                nums[k] = nums[j]
        return k+ 1