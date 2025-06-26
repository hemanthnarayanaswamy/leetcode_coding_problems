class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        # Pair each score with its original index
        indexed_scores = list(enumerate(score))
        # Sort descending by score
        indexed_scores.sort(key=lambda x: x[1], reverse=True)

        # Prepare the result array
        ans = [''] * n
        
        # Assign medals/ranks in one pass
        for rank, (idx, _) in enumerate(indexed_scores, start=1):
            if rank == 1:
                ans[idx] = "Gold Medal"
            elif rank == 2:
                ans[idx] = "Silver Medal"
            elif rank == 3:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(rank)
        
        return ans
