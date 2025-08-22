class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_height, min_width = float('inf'), float('inf')
        max_height, max_width = 0, 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    min_height = min(min_height, i)
                    min_width = min(min_width, j)
                    max_height = max(max_height, i)
                    max_width = max(max_width, j)
        
        area = (max_height - min_height + 1) * (max_width - min_width + 1)

        return area
