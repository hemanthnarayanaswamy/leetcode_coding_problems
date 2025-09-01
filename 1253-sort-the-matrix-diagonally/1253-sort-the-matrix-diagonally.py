class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonalMap = defaultdict(list)
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                diagonalMap[i-j].append(mat[i][j])
        
        for id in diagonalMap:
            diagonalMap[id].sort(reverse=True)

        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonalMap[i-j].pop()
        
        return mat
                
        
