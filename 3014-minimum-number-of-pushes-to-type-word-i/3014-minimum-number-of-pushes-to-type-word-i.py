class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        d, m = divmod(n, 8)
        print(d, m)

        if n <= 8:
            return n

        total = 0
        for i in range(1, d+1):
            print(total)
            total += (8*i)
        
        print(total)
        total += (m*(i+1))

        return total