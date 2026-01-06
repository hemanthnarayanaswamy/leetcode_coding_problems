class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        colMax = defaultdict(int)
        i = 0

        for col in zip(*matrix):
            colMax[i] = max(col)
            i += 1 
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = colMax[j]
        
        return matrix
