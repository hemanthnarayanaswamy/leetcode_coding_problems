class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        
        for i in range(len(colors)-1,-1,-1):
            if colors[i]!=colors[0]:
                diff = i
                ans = max(ans,diff)

        for i in range(len(colors)):
            if colors[i]!=colors[len(colors)-1]:
                diff = len(colors)-1-i
                ans = max(ans,diff)

        return ans