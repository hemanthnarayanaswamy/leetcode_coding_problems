class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s = s.split(':')
        c1, r1 = ord(s[0][0]), int(s[0][1])
        c2, r2 = ord(s[1][0]), int(s[1][1])
        res = []
        
        for c in range(c1, c2+1):
            c = chr(c)
            for r in range(r1, r2+1):
                res.append(c+str(r))
        
        return res
