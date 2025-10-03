class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = {}
        column = {}
        result = [[0]*n] * m
        count = 0

        for r,c in indices:
            row[r] = row.get(r, 0) + 1
            column[c] = column.get(c, 0) + 1
        
        for i in range(m):
            for j in range(n):
                result[i][j] = row.get(i, 0) + column.get(j, 0)
                
                if result[i][j] % 2:
                    count += 1 

        return count
        

