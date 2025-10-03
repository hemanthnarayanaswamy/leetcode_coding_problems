class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0] * m
        column = [0] * n

        for r,c in indices: # cumulative values 
            row[r] +=  1  
            column[c] += 1
        
        odd_count = 0
        for i in range(m):
            for j in range(n): 
                if (row[i] + column[j]) % 2:
                    odd_count += 1 

        return odd_count  

