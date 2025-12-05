class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for row in matrix:
            if len(set(row)) != n:
                return False
        
        matrix_transpose = list(map(list, zip(*matrix)))

        for row in matrix_transpose:
            if len(set(row)) != n:
                return False 
        
        return True