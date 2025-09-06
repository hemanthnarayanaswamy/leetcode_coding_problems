class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanceCount = res = 0

        for c in s:
            if c == 'R':
                balanceCount += 1
            else:
                balanceCount -= 1
            
            if not balanceCount:
                res += 1
        
        return res