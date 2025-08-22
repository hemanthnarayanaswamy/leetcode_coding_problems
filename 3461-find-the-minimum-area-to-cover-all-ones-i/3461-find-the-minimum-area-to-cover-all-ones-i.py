class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_height, min_width = float('inf'), float('inf')
        max_height, max_width = 0, 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if min_height == 0:
                        max_height = max(max_height, i)
                    else: 
                        min_height = min(min_height, i)
                        max_height = max(max_height, i)
                    
                    if min_width == 0:
                        max_width = max(max_width, j)
                    else:
                        min_width = min(min_width, j)
                        max_width = max(max_width, j)
        
        return (max_height - min_height + 1) * (max_width - min_width + 1)