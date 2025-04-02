class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        my_coins = 0
        n = len(piles) // 3

        for i in range(1,len(piles), 2):
            my_coins += piles[i]
            n -= 1
            if n == 0:
                break 
        
        return my_coins