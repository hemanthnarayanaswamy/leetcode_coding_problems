class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        onesRow = [0] * m
        onesColumn = [0] * n

        for i in range(m):
            for j in range(n):
                x = grid[i][j] 
                onesRow[i] +=  x
                onesColumn[j] += x
    
        diff = []

        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append((2*onesRow[i] - n) + (2*onesColumn[j] - m))
            diff.append(tmp)

        return diff
