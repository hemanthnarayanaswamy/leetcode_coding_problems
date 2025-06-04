class Solution:
    def maximum69Number (self, num: int) -> int:
        numList = list(str(num))

        for i in range(len(numList)):
            if numList[i] == '6':
                numList[i] = '9'
                break

        return int(''.join(numList))