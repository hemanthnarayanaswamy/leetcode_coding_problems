class Solution:
    def sumAndMultiply(self, n: int) -> int:
        new_n = power = total = 0

        while n > 0:
            n, m = divmod(n,10)
            if m:
                new_n += m * (10**power)
                total += m
                power += 1

        return new_n * total
        