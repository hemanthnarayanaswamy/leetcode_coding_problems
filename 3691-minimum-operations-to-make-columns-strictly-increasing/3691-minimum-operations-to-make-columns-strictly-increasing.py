class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        operations = 0

        for j in range(len(grid[0])):
            for i in range(1, len(grid)):
                p = grid[i-1][j] 
                c = grid[i][j]
                if p > c:
                    tmp = p - c + 1
                    grid[i][j] += tmp
                    operations += tmp
                elif p == c:
                    grid[i][j] += 1
                    operations += 1

        return operations
