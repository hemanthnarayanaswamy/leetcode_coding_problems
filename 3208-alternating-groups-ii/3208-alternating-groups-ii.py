class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors +=colors[:k-1]
        n=len(colors)
        subLen=1
        ans=0

        for i in range(1,n):
            if colors[i] != colors[i-1]:
                subLen += 1
            else:
                subLen = 1

            if subLen >= k:
                ans+=1
                
        return ans
