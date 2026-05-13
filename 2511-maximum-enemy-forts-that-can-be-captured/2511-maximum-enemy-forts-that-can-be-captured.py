class Solution:
    def captureForts(self, forts: List[int]) -> int:
        def attack(forts):
            m, c = 0, -1
            for f in forts:
                if f == 1: 
                    c = 0   
                elif f == 0: 
                    if c >= 0:
                        c += 1     
                else: 
                    c, m = -1, max(c,m)  
            return m
        
        return max(attack(forts), attack(forts[::-1]))