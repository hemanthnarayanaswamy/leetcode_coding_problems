class Solution:
    def removeZeros(self, n: int) -> int:
        res = []

        while n:
            quotient, remainder = divmod(n, 10)
            if remainder:
                res.append(str(remainder))
            n = quotient
        
        return int(''.join(res[::-1]))
