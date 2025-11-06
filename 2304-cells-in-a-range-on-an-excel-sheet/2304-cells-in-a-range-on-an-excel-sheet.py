class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        lower, upper = s.split(':')
        c1, r1 = ord(lower[0]), int(lower[1])
        c2, r2 = ord(upper[0]), int(upper[1])
        res = []
        
        for cc in range(c1, c2+1):
            cc = chr(cc)
            for rr in range(r1, r2+1):
                res.append(cc+str(rr))
        
        return res
