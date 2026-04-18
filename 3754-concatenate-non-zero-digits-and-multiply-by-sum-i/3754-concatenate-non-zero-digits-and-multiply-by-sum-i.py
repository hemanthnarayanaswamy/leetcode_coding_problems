class Solution:
    def sumAndMultiply(self, n: int) -> int:   
        total = power = num = 0

        while n:
            n, m = divmod(n, 10)
            if m:
                total += m
                num += m * (10 ** power)
                power += 1
        
        return total * num