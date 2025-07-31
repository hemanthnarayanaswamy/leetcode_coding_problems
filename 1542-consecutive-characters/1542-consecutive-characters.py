class Solution:
    def maxPower(self, s: str) -> int:
        res = 0
        cur = 0
        curr_c = None
        for c in s:
            if c != curr_c:
                curr_c = c
                cur = 1
            else:
                cur += 1
            if cur > res:
                res = cur
        return res