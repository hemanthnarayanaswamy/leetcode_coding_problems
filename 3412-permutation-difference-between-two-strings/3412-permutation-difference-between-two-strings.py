class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0

        for i,char in enumerate(s):
            result += abs(t.index(char) - i)

        return result