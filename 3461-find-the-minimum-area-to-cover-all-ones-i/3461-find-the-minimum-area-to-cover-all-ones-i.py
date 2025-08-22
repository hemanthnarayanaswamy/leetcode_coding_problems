class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_height, min_width = float('inf'), float('inf')
        max_height, max_width = 0, 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if i == 0:
                        min_height = 0
                    elif min_height != 0:
                        min_height = min(min_height, i)

                    if j == 0:
                        min_width = 0
                    elif min_width != 0:
                        min_width = min(min_width, j)

                    if i > max_height:
                        max_height = i

                    if j > max_width:
                        max_width = j

        return (max_height - min_height + 1) * (max_width - min_width + 1)