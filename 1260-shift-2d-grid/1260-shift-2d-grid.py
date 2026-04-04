class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        grid1D = []
        res = []
        m = len(grid[0])

        for row in grid:
            grid1D.extend(row)
        
        k = (k % len(grid1D))

        if k == 0:
            return grid
        
        grid1D[:k], grid1D[k:] = grid1D[-k:], grid1D[:-k]
        
        for i in range(0, len(grid1D), m):
            res.append(grid1D[i:i+m])

        return res