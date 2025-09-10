class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index = -1
        minDistance = float('inf')

        for i, cor in enumerate(points):
            x1, y1 = cor 
            
            if x1 == x:
                tmpDistance = abs(y - y1)
                if tmpDistance < minDistance:
                    minDistance = tmpDistance
                    index = i
            elif y1 == y:
                tmpDistance = abs(x - x1)
                if tmpDistance < minDistance:
                    minDistance = tmpDistance
                    index = i
        
        return index
