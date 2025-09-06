class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanceCount = 0
        Lcount = Rcount = 0

        for c in s:
            if c == 'R':
                Rcount += 1
            else:
                Lcount += 1
            
            if Rcount == Lcount:
                balanceCount += 1
        
        return balanceCount