class Solution:
    def findValidPair(self, s: str) -> str:
        sMap = Counter(s)

        for i in range(len(s)-1):
            a, b = s[i], s[i+1]

            if a == b:
                continue
            
            if sMap[a] == int(a):
                if sMap[b] == int(b):
                    return a + b
        
        return ''