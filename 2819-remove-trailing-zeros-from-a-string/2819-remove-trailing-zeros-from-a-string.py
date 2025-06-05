class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        numAns = str(int(num[::-1]))

        return numAns[::-1]