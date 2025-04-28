class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        inc,dec = 0, n
        perm = [0]*(n+1)

        for i in range(n):
            if s[i] == 'I':
                perm[i] = inc
                inc += 1
            else:
                perm[i] = dec
                dec -= 1 
        
        perm[n] = inc

        return perm


        