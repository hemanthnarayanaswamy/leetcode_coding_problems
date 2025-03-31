from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_freq = Counter(stones)
        count = 0

        for jewel in jewels:
            count += stones_freq.get(jewel, 0)
        
        return count