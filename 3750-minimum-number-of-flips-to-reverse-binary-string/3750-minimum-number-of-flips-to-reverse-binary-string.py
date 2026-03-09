class Solution:
    def minimumFlips(self, n: int) -> int:
        b = bin(n)[2:]
        rb = b[::-1]
        res = 0

        for i in range(len(b)):
            if b[i] != rb[i]:
                res += 1
        
        return res