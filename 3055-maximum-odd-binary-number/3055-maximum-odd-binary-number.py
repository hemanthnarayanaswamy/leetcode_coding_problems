class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        onesCount = s.count('1') 
        zerosCount = len(s) - onesCount

        return '1'*(onesCount-1) + '0'*zerosCount + '1'