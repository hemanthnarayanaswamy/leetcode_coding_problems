class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        count = 0

        for i in range(n):
            for j in range(1,m):
                if strs[j-1][i] > strs[j][i]:
                    count += 1
                    break
                
        return count