class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        widths = []
        heights = []
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    widths.append(j)
                    heights.append(i)

        return (max(heights) - min(heights) + 1) * (max(widths) - min(widths) + 1)