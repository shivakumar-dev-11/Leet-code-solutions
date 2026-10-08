class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums) 
        longestStreak = 0

        for num in num_set :
            if (num - 1) not in num_set:
                current_streak = 1

                while (num + current_streak ) in num_set:
                    current_streak += 1
                longestStreak = max(longestStreak,current_streak)
        return longestStreak

   