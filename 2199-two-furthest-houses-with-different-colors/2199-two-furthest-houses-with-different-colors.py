class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        h1, h2 = 0, len(colors)-1

        res = []

        while h1 < h2:
            if colors[h1] != colors[h2]:
                res.append(h2 - h1)
                break
            else:
                h2 -= 1

        h2 = len(colors)-1

        while h1 < h2:
            if colors[h1] != colors[h2]:
                res.append(h2 - h1)
                break
            else:
                h1 += 1
        
        return max(res)