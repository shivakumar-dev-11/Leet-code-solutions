
class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        freq = {}
        morethan = n // 3
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        output = []
        for key, value in freq.items():
            if value > morethan:
                output.append(key)
        return output
