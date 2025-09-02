class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        result = []

        for i in range(len(s)):
            x, y = startPos[0], startPos[1]
            count = 0
            while i < len(s):
                x1, y1 = directions[s[i]]
                x += x1
                y += y1
                if (x > n - 1 or y > n - 1) or (x < 0 or y < 0 ):
                    break
                else:
                    count += 1
                    i += 1
            result.append(count)
        
        return result
            