class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        scoreRank = {s: str(i+1) for i, s in enumerate(sorted(score, reverse=True))}

        rank = []

        for s in score:
            if scoreRank[s] == '1':
                rank.append("Gold Medal")
            elif scoreRank[s] == '2':
                rank.append("Silver Medal")
            elif scoreRank[s] == '3':
                rank.append("Bronze Medal")
            else:
                rank.append(scoreRank[s])
        
        return rank


        