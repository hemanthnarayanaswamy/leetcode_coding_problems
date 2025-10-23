class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        lc = colors[0]
        lm = neededTime[0]
        tt = 0
        for i in range(1, n):
            if lc == colors[i]:
                if lm > neededTime[i]:
                    tt += neededTime[i]
                else:
                    tt += lm
                    lm = neededTime[i]
            else:
                lc = colors[i]
                lm = neededTime[i]
        return tt
        