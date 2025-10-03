class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0] * m
        column = [0] * n

        for r,c in indices:  
            row[r] +=  1  
            column[c] += 1
        
        odd_count = 0
        for i in row:
            for j in column: 
                if (i + j) % 2:
                    odd_count += 1 

        return odd_count  

