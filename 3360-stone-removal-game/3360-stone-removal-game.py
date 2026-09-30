class Solution:
    def canAliceWin(self, n: int) -> bool:
        for i in range(10, 0, -1):
            if n >= i:
                n -= i
            else:
                break
        
        return True if i % 2 else False
            