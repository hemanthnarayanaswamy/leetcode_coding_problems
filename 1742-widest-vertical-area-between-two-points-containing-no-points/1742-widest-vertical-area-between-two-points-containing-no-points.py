class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xpoints = sorted(x for x,y in points)

        maxWidth = 0

        for i in range(len(xpoints)-1):
            tempDiff = xpoints[i+1] - xpoints[i]
            if tempDiff > maxWidth:
                maxWidth = tempDiff
        
        return maxWidth
