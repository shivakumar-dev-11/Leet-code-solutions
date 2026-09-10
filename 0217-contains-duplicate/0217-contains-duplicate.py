class Solution(object):
    def containsDuplicate(self, nums):
        duplicate = set()
        for i in nums:
            if i in duplicate:
                return True
            duplicate.add(i)
        return False
         