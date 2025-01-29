class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {'N':(0,1), "E":(1, 0), "S":(0,-1), "W":(-1, 0)}
        history = {(0,0),}
        x, y = 0 ,0
        for direction in path:
            x += directions[direction][0]
            y += directions[direction][1]
            if (x,y) in history:
                return True
            history.add((x,y))
        return False