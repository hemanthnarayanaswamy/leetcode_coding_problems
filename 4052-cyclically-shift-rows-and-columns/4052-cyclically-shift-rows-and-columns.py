class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        n = len(rowShift)

        for i in range(n):
            k = rowShift[i]
            grid[i] = grid[i][k:]+grid[i][:k]
        
        for j in range(n):
            k = colShift[j]
            tmp = []
            if k:
                for i in range(n):
                    tmp.append(grid[i][j])
                tmp = tmp[k:] + tmp[:k]

                for i in range(n):
                    grid[i][j] = tmp[i]
        
        return grid