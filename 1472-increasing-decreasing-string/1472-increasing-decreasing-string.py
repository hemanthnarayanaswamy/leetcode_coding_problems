class Solution:
    def sortString(self, s: str) -> str:
        sFreq = Counter(s)

        result = []

        while len(result) != len(s):
            for i in range(ord('a'), ord('z')+1):
                c1 = chr(i)
                if sFreq.get(c1,0) > 0:
                    result.append(c1)
                    sFreq[c1] -= 1
            
            if len(result) == len(s):
                break
            
            for j in range(ord('z'), ord('a')-1, -1):
                c2 = chr(j)
                if sFreq.get(c2,0) > 0:
                    result.append(c2)
                    sFreq[c2] -= 1
            
            print(result)
        
        return ''.join(result)