class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        if x not in s or y not in s:
            return s
        
        s1 = s2 = s3 = ''

        for c in s:
            if c in x:
                s1 += c
            elif c in y:
                s2 += c
            else:
                s3 += c
        
        return s2 + s1 + s3