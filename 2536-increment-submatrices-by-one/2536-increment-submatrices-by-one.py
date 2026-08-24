class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        #  apply all operations using 4-point updates
        for row1, col1, row2, col2 in queries: 
            diff[row1][col1] += 1
            diff[row2 + 1][col1] -= 1
            diff[row1][col2 + 1] -= 1
            diff[row2 + 1][col2 + 1] += 1
        
        # apply row wise prefix
        for i in range(n+1):
            for j in range(1, n+1):
                diff[i][j] += diff[i][j-1]
        
        # apply column wise prefix
        for j in range(n+1):
            for i in range(1, n+1):
                diff[i][j] += diff[i-1][j]
        
        # apply the diff to the original array
        arr = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                arr[i][j] = diff[i][j]
        
        return arr