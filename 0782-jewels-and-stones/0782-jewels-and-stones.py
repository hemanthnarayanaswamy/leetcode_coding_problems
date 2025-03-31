from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_freq = Counter(stones)
        count = 0

        for jewel in jewels:
            if jewel in stones_freq:
                count += stones_freq[jewel]
        
        return count