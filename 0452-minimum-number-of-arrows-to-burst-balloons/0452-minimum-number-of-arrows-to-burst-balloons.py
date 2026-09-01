class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1]))
        arrows = 0
        a1, a2 = points[0]

        for i in range(1, len(points)):
            b1, b2 = points[i]
            if a2 < b1:
                arrows += 1
                a1, a2 = b1, b2
            else:
                a1 = max(a1, b1)
                a2 = min(a2, b2)
        
        return arrows + 1
