class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        result = []

        for start in range(len(s)):
            x, y = startPos[0], startPos[1]
            count = 0
            for i in range(start, len(s)):
                dx, dy = directions[s[i]]
                x += dx
                y += dy

                if not (0 <= x < n and 0 <= y < n):
                    break
                count += 1
            result.append(count)
        
        return result
