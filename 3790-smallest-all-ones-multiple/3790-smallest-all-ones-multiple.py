class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        rem = 0
        seen = set()

        for cnt in range(k):
            rem = (rem * 10 + 1) % k

            if rem == 0: 
                return cnt+1

            if rem in seen:
                return -1

        return -1