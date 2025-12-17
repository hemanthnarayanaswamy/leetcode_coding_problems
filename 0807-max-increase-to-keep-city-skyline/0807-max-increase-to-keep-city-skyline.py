class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowMax = [max(row) for row in grid]
        colMax = [max(col) for col in zip(*grid)]
        
        totalSum = 0
        for i in range(n):
            for j in range(n):
                totalSum += min(rowMax[i], colMax[j]) - grid[i][j]
        
        return totalSum
