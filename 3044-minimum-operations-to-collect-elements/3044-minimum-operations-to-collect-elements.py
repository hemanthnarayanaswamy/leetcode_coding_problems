class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s1 = set()
        s2 = set()
        for i in range(1, k+1):
            s1.add(i)
        n = len(nums)-1
        r = 0
        while (s1 != s2 and n>-1):
            if nums[n] in s1:
                s2.add(nums[n])
            r += 1
            n -= 1
        return r