from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = Counter(stones)
        count = 0

        for jewel in jewels:
            count += stones.get(jewel, 0)
        
        return count