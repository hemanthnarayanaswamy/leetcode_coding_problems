class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = {}
        column = {}
        count = 0

        for r,c in indices:
            row[r] = row.get(r, 0) + 1
            column[c] = column.get(c, 0) + 1
        
        for i in range(m):
            for j in range(n): 
                
                if (row.get(i, 0) + column.get(j, 0)) % 2:
                    count += 1 

        return count  

