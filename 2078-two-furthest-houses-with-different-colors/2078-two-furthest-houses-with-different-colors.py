class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        n = len(colors)

        for i in range(n-1,-1,-1):
            if colors[i] != colors[0]:
                ans = i
                break

        for i in range(n):
            if colors[i] != colors[n-1]:
                diff = len(colors)-1-i
                ans = max(ans,diff)
                break

        return ans