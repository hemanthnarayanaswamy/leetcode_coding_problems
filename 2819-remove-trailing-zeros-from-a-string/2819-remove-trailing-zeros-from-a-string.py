class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        if num[-1] == '0':
            return str(int(num[::-1]))[::-1]
        else:
            return num