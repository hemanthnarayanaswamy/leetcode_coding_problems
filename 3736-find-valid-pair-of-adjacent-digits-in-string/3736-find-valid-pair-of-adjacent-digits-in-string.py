class Solution:
    def findValidPair(self, s: str) -> str:
        sMap = Counter(s)

        for i in range(1, len(s)):
            a, b = s[i-1], s[i]

            if a == b:
                continue
            
            if sMap[a] == int(a):
                if sMap[b] == int(b):
                    return a + b
        
        return ''