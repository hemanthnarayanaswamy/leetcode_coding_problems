class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        fr = fc = 0
        n, m = len(grid), len(grid[0])

        for r in grid:
            x = 0
            y = m - 1
            while x < y:
                if r[x] != r[y]:
                    fr += 1
                x += 1
                y -= 1
        
        for j in range(m):
            x = 0
            y = n - 1
            while x < y:
                if grid[x][j] != grid[y][j]:
                    fc += 1
                x += 1
                y -= 1
        
        return min(fc, fr)
 
        