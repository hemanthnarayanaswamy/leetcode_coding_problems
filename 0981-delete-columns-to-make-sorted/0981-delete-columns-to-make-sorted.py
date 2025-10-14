class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        count = 0

        for i in range(n):
            for j in range(m-1):
                if strs[j][i] > strs[j+1][i]:
                    count += 1
                    break
                
        return count