class Solution(object):
    def intersection(self, nums1, nums2):
        set_num1 = set(nums1)
        set_num2 = set (nums2)
     
        output = []
        for i in set_num1:
            if i in set_num2:
                output.append(i)
        return output
        