class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        n = len(s)
        start = 0
        prev = s[0]

        for i in range(1, n):
            if s[i] != prev:
                if (i - start) >= 3:
                    res.append([start, i-1])
                start = i
                prev = s[i]
        
        print(i)
        if (n - start) >= 3:
            res.append([start, i])

        return res