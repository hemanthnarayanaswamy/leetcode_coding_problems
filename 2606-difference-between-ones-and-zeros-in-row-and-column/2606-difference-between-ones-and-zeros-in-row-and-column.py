class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        onesRow = [0] * m
        onesColumn = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    onesRow[i] +=  1
                    onesColumn[j] += 1
    
        diff = []

        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(onesRow[i] + onesColumn[j] - (m - onesRow[i]) - (n - onesColumn[j]))
            diff.append(tmp)

        return diff
