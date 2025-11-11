class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        n = len(s)
        start = 0
        prev = s[0]

        if n < 3:
            return res

        for i in range(1, n):
            if s[i] != prev:
                if (i - start) >= 3:
                    res.append([start, i-1])
                start = i
                prev = s[i]
        
        if (n - start) >= 3:
            res.append([start, n-1])

        return res