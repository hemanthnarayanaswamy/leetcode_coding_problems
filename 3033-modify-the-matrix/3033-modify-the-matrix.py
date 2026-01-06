class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        colMax = []

        for col in zip(*matrix):
            colMax.append(max(col))
        
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = colMax[j]
        
        return matrix
