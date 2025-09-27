class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # Helper function to calculate the area of a triangle given three points (x, y)
        def area(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            # Shoelace formula for triangle area
            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        
        maxArea = 0.0
        n = len(points)

        # Iterate through all unique combinations of three points
        for i in range(n-2):
            for j in range(i + 1, n-1): # Start j from i + 1 to avoid duplicate pairs and self-pairing
                for k in range(j + 1, n): # Start k from j + 1 to avoid duplicate triplets and self-pairing
                    current_area = area(points[i], points[j], points[k])
                    if current_area > maxArea:
                        maxArea = current_area
    
        return maxArea