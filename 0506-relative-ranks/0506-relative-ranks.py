
class Solution(object):
    def findRelativeRanks(self, score):
        reversed_score = sorted(score, reverse=True)
        rank = {}

        for i in range(len(reversed_score)):
            if i == 0:
                rank[reversed_score[i]] = "Gold Medal"
            elif i == 1:
                rank[reversed_score[i]] = "Silver Medal"
            elif i == 2:
                rank[reversed_score[i]] = "Bronze Medal"
            else:
                rank[reversed_score[i]] = str(i + 1)

        result = []

        for s in score:
            result.append(rank[s])

        return result
