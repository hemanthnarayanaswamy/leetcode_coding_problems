class Solution:
    def largestEven(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)-1, -1, -1):
            if s[i] == '2':
                break
            else:
                s.pop(i)
        
        return ''.join(s)