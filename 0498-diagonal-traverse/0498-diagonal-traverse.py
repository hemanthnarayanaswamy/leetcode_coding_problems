class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        result = []

        for d in range(m+n-1):
            diagonal = []
            for i in range(m):
                j = d - i
                if 0 <= j < n:
                    diagonal.append(mat[i][j])

            if d % 2:
                result.extend(diagonal)
            else:
                result.extend(diagonal[::-1])

        return result 

