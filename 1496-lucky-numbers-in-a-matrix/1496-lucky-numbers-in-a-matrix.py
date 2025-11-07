class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        row = [float('inf')] * m
        col = [0] * n

        for i in range(m):
            for j in range(n):
                num = matrix[i][j]
                if num < row[i]:
                    row[i] = num
                if num > col[j]:
                    col[j] = num
        
        return list(set(row) & set(col))

