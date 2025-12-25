class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        maxHappy = 0
        
        for i in range(k):
            maxHappy += max(happiness[i] - i, 0)

        return maxHappy
