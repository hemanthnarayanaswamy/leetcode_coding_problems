
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        LHS = 0

        for x in cnt:
            if x + 1 in cnt:
                LHS = max(LHS, cnt[x] + cnt[x + 1])

        return LHS