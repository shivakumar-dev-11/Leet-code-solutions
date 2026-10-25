class Solution(object):
    def findDuplicates(self, nums):
        hashmap = {}
        output = []
        for i in nums:
            hashmap[i] = hashmap.get(i, 0)+1
        for i in hashmap :
            if hashmap[i] > 1:
                output.append(i)
        return output

