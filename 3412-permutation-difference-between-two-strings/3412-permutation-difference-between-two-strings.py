class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0

        for char in s:
            result += abs(t.index(char) - s.index(char))

        return result