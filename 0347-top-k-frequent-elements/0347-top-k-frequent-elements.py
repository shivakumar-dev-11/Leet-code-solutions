class Solution(object):

    def topKFrequent(self, nums, k):

        freq = {}

       
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        answer = []

       
        for i in range(k):

            highest = 0
            highest_num = None

            for num in freq:

                if freq[num] > highest:
                    highest = freq[num]
                    highest_num = num

            answer.append(highest_num)

           
            del freq[highest_num]

        return answer