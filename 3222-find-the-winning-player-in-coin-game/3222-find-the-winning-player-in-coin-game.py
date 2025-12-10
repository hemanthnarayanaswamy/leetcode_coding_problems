class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        count = 0
        while x > 0 and y > 0:
            x -= 1
            y -= 4

            if x >= 0 and y >= 0:
                count += 1
        
        count %= 2
        
        return 'Alice' if count else 'Bob'