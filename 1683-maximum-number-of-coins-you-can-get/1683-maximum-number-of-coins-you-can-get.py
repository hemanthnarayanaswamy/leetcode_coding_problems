class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        coinCount = 0
        n = len(piles)
        
        for _ in range(n//3):
            n -=2
            coinCount += piles[n]

        return coinCount