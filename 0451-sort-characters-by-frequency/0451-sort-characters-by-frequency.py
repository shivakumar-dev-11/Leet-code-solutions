class Solution(object):
    def frequencySort(self, s):
        frequency = {}
        for char in s:
            frequency[char] = frequency.get(char , 0) +1
        n = len(s)
        buckets = [[] for _ in range(n+1)]
        for char , count in frequency.items():
            buckets[count].append(char)              
        result = []
        for i in range (n,0, -1):
            for char in buckets[i]:
                result.append(char*i)
        return "".join(result)
