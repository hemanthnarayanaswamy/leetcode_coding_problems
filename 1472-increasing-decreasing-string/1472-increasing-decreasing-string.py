class Solution:
    def sortString(self, s: str) -> str:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        sFreq = Counter(s)

        result = []

        while len(result) != len(s):
            for c1 in alphabets:
                if sFreq.get(c1,0) > 0:
                    result.append(c1)
                    sFreq[c1] -= 1
            
            if len(result) == len(s):
                break
            
            for c2 in alphabets[::-1]:
                if sFreq.get(c2,0) > 0:
                    result.append(c2)
                    sFreq[c2] -= 1       
        
        return ''.join(result)