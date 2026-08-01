class Solution:
    def countValidPrefixes(self, s: str) -> int:
        pre = z = o = 0

        for c in s:
            if c == '0':
                z += 1
            else:
                o += 1
            
            if abs(z - o) <= 1:
                pre += 1
        
        return pre