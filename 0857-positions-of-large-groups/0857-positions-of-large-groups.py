class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        n = len(s)
        start = 0
        largeGroup = []

        for i in range(1, n + 1):
            if i == n or s[i] != s[i - 1]:
                if i - start >= 3:
                    largeGroup.append([start, i - 1])
                start = i

        return largeGroup