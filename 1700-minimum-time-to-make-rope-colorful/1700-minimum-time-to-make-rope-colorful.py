class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        prev_color = ''
        prev_max = 0
        for c, t in zip(colors, neededTime):
            if c == prev_color:
                total += min(prev_max, t)
                prev_max = max(prev_max, t)
            else:
                prev_color = c
                prev_max = t
        return total