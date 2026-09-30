class Solution:
    def binaryGap(self, n: int) -> int:
        prev = dist = 0

        for i, b in enumerate(bin(n)[2::]):
            if b == '1':
                dist = max(dist, i - prev)
                prev = i
        
        return dist

        