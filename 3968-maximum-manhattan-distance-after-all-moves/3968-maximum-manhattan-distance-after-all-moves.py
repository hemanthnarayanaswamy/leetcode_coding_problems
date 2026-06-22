class Solution:
    def maxDistance(self, moves: str) -> int:
        dir = {'L': (-1, 0), 'D': (0, -1), 'U': (0, 1), 'R': (1, 0)}
        count_ = x = y = 0

        for d in moves:
            if d == '_':
                count_ += 1
            else:
                x += dir[d][0]
                y += dir[d][1]
        
        dist = count_ + abs(0 - x) + abs(0-y)

        return dist
