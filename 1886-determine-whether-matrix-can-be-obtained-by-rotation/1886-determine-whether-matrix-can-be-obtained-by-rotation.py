class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
        if mat == target:
            return True 

        def rotateMatrix(mat):
            tmp = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    tmp[i][j] = mat[j][n - i - 1] #out[i][j] = in[n - 1 - j][i]
            return tmp
        
        rotations = 0

        while rotations < 3:
            tmp = rotateMatrix(mat)
            if tmp == target:
                return True 
            mat = tmp
            rotations += 1
        
        return False