class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        operations = 0

        for j in range(len(grid[0])):
            for i in range(1, len(grid)):
                if grid[i-1][j] >= grid[i][j]:
                    tmp = abs(grid[i-1][j] - grid[i][j]) + 1
                    grid[i][j] += tmp
                    print(grid[i][j], (abs(grid[i-1][j] - grid[i][j]) + 1))
                    operations += tmp
                    print(operations)
        print(grid)
        return operations
