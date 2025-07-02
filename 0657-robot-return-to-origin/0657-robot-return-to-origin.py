class Solution:
    def judgeCircle(self, moves: str) -> bool:
        Horizontal, Vertical = 0, 0
        
        for m in moves:
            if m == 'U':
                Vertical += 1
            elif m == 'D':
                Vertical -= 1
            elif m == 'R':
                Horizontal += 1
            else:
                Horizontal -= 1
        
        return False if Horizontal or Vertical else True
        