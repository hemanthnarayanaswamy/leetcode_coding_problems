class Solution:
    def getSmallestString(self, s: str) -> str:
        for i in range(len(s)-1):
            cur = int(s[i])
            nxt = int(s[i+1])
            if cur > nxt and cur % 2 == nxt % 2:
                return s[:i] + s[i:i+2][::-1] + s[i+2:]
        
        return s