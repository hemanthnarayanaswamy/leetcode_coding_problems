class Solution:
    def maxPower(self, s: str) -> int:
        pre = s[0]
        res = 1
        count = 1

        for ch in s[1:]:
            if ch == pre:
                count += 1
            else:
                res = max(res, count)
                count = 1
                pre = ch
        
        return max(res, count)
