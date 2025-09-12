class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = sum(1 for c in s if c in 'aeiou')

        if count == 0:
            return False
        else:
            return True
            
