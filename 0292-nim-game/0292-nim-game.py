class Solution:
    def canWinNim(self, n: int) -> bool:
        if n <= 2:
            return True
        
        return True if n % 4 else False