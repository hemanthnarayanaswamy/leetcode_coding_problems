class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonalMat = defaultdict(list)
        res = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonalMat[i+j].append(mat[i][j])
        
        for i in diagonalMat:
            if i % 2:
                res.extend(diagonalMat[i])
            else:
                res.extend(diagonalMat[i][::-1])

        return res