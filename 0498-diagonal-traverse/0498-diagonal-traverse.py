class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonalMat = defaultdict(list)
        res = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonalMat[i+j].append(mat[i][j])
        
        for i, val in diagonalMat.items():
            if i % 2:
                res.extend(val)
            else:
                res.extend(val[::-1])

        return res