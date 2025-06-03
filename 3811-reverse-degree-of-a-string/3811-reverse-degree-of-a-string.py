class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0

        for i, char in enumerate(s):
            result += ((i+1) * abs(ord(char) - 123))
        
        return result
