class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        x, y = points[0]
        for i in range(1, len(points)):
            x1, y1 = points[i]
            
            time += max(abs(x1 - x), abs(y1 - y))
            x, y = points[i]

        return time
        