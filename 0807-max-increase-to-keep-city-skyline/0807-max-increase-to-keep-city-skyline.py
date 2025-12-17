class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = defaultdict(int)
        colMax = defaultdict(int)
        totalSum = 0
        n = len(grid)

        for i in range(n):
            rowMax[i] = max(grid[i])
            for j in range(n):
                h = grid[i][j]
                if colMax[j] < h:
                    colMax[j] = h
        
        for i in range(n):
            for j in range(n):
                totalSum += abs(grid[i][j] - min(rowMax[i], colMax[j]))
        
        return totalSum

