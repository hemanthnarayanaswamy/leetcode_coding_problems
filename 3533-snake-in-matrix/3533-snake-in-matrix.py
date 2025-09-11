class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        
        i = j = 0

        for command in commands:
            if command == "RIGHT":
                j += 1
            elif command == "LEFT":
                j -= 1
            elif command == "DOWN":
                i += 1
            else:
                i -= 1
        
        return i * n + j