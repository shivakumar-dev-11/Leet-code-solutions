class Solution(object):
    def maxArea(self, height):
        left = 0 
        right = len(height)-1
        max = 0 
        while left < right :
            length = min(height[left], height[right])
            breath =  right - left 
            area = length * breath
            if area > max :
                max = area 
            if height[right] > height[left]:
                left+=1
            else:
                right-=1
        return max



       
        