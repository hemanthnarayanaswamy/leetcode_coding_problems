class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        if (x1 >= x4 or x2 <= x3):
            return False
        
        if (y1 >= y4 or y2 <= y3):
            return False
        
        return True