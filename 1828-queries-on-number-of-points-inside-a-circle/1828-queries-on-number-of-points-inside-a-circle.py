class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []

        for x1,y1,r in queries:
            count = 0
            for x2, y2 in points:
                if (x2 - x1)**2 + (y2 - y1)**2 <= r**2:
                    count += 1
            ans.append(count)
        
        return ans
            