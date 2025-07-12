class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_len = float('-inf')
        count = 0

        for l, w in rectangles:
            side_len = min(l, w)
            
            if side_len == max_len:
                count += 1
            elif side_len > max_len:
                max_len = side_len
                count = 1

        return count