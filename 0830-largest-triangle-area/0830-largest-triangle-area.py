class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxArea = 0
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j]
                for k in range(n):
                    if k == j or k == i:
                        continue 
                    x3, y3 = points[k]
                    
                    area = 0.5 * abs((x1 * (y2 - y3))+(x2 * (y3 - y1))+(x3 * (y1 - y2)))
                    if area > maxArea:
                        maxArea = area
        
        return maxArea