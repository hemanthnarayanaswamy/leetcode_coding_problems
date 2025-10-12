class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        onesRow = [0] * m
        onesColumn = [0] * n

        for i in range(m):
            row = grid[i]
            for j in range(n):
                v = row[j]
                onesRow[i] +=  v
                onesColumn[j] += v
    
        diff = []

        for i in range(m):
            tmp = []
            rowScore = 2*onesRow[i] - n
            for j in range(n):
                totalScore = rowScore + (2*onesColumn[j] - m)
                tmp.append(totalScore)
            diff.append(tmp)

        return diff
