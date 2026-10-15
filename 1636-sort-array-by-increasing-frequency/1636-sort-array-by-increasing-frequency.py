
class Solution(object):
    def frequencySort(self, nums):
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if (freq[nums[i]] > freq[nums[j]] or
                    (freq[nums[i]] == freq[nums[j]] and
                     nums[i] < nums[j])):
                    nums[i], nums[j] = nums[j], nums[i]

        return nums

        