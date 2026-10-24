class Solution(object):
    def findTheDifference(self, s, t):       
        freq ={} 
        for i in s :
            freq[i] = freq.get(i,0)+1      
        for i in t :
            freq[i] = freq.get(i,0)-1
            if freq[i] <0:
                return i