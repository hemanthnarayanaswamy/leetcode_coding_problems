class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        if moves.count('R') > moves.count('L'):
            travelDirection = 'R' 
        else:
            travelDirection = 'L'

        directionsVal = {'R': 1, 'L': -1}
        
        dist = 0

        for d in moves:
            if d == '_':
                dist += directionsVal[travelDirection]
            else:
                dist += directionsVal[d]
        
        return abs(dist)


