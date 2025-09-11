class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        directions = {"RIGHT": [0, 1], "LEFT": [0, -1], "DOWN": [1, 0], "UP": [-1, 0]}
        i = j = 0

        for command in commands:
            i += directions[command][0]
            j += directions[command][1]
        
        return i * n + j