class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        n = len(mat)
        m = len(mat[0])

        arr_rows = defaultdict(int)
        arr_cols = defaultdict(int)

        for i in range(n):
            for j in range(m):
                num = mat[i][j]
                rows[num] = i
                cols[num]= j
        
        for i, num in enumerate(arr):
            r = rows[num]
            c = cols[num]
            arr_rows[r] += 1
            arr_cols[c] += 1

            if arr_rows[r] == m or arr_cols[c] == n:
                return i
        