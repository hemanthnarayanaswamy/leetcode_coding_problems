class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        new = set([num for num in nums if num % k == 0])
        max = 1000

        for i in range(1, max):
            n = i * k
            if n not in new:
                return n