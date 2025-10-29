class Solution:
    def smallestNumber(self, n: int) -> int:
        res = 0
        power = 1

        while res < n:
            res = (2**power)-1
            power += 1

        return res