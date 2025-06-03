class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0

        for i, char in enumerate(s):
            result += (26-(ord(char) - 97)) * (i+1)
        
        return result
