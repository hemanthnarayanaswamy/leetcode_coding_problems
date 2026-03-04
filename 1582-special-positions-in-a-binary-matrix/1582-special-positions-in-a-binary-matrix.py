class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    if rows[i] == 1 and cols[j] == 1:
                        ans += 1
        
        return ans
