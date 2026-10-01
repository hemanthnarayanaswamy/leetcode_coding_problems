class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        matMap = defaultdict(list)
        n = len(mat)
        m = len(mat[0])
        rowCount = [0] * n
        colCount = [0] * m

        for i in range(n):
            for j in range(m):
                num = mat[i][j]
                matMap[num] = [i, j]
        
        for i, num in enumerate(arr):
            r, c = matMap[num]
            rowCount[r] += 1
            colCount[c] += 1

            if rowCount[r] == m or colCount[c] == n:
                return i
        