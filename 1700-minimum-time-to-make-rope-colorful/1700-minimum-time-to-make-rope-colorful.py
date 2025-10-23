class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l, r = 0, 1
        time = 0
        n = len(colors)

        while r < n:
            if colors[l] == colors[r]:
                if neededTime[l] > neededTime[r]:
                    time += neededTime[r]
                    r += 1
                else:
                    time += neededTime[l]
                    l = r
                    r += 1
            else:
                l = r
                r += 1

        return time