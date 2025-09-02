class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        m = len(s)
        result = [0] * m

        for i in range(len(s)):
            x, y = startPos
            count = 0
            for dir in s[i:]:
                dx, dy = directions[dir]
                x += dx
                y += dy

                if not (0 <= x < n and 0 <= y < n):
                    break
                count += 1
            result[i] = count
        return result
