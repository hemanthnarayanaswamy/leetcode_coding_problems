class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        d, m = divmod(n, 8)

        if n <= 8:
            return n

        total = 0
        for i in range(1, d+1):
            total += (8*i)
        
        total += (m*(i+1))

        return total