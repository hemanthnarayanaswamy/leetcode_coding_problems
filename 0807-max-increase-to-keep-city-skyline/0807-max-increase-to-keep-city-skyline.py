class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = [max(row) for row in grid]
        colMax = [max(col) for col in zip(*grid)]
        totalSum = 0
        n = len(grid)
        
        for i in range(n):
            for j in range(n):
                totalSum += abs(min(rowMax[i], colMax[j])) - grid[i][j]
        
        return totalSum

