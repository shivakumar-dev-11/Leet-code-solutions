class Solution(object):
    def plusOne(self, digits):
        nums = 0
        output = []
        for i in range (0, len(digits)):
            nums = nums*10+digits[i]
        nums+=1
        while nums >0:
           digit = nums%10
           output.append(digit)
           nums//=10
        output.reverse()
        return output


        