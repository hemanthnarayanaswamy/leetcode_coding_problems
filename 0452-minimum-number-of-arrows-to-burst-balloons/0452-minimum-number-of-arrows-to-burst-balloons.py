class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda x: x[0])
        arrows = 1
        p = points[0][1]
        
        for balloon in points[1:]:
            if balloon[0] > p: 
                arrows += 1  
                p = balloon[1] 
            else:
                p = min(p, balloon[1])
        
        return arrows