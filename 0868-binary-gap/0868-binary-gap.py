class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2::]
        l = len(b)
        maxDist = 0
        
        for i in range(l):
            if b[i] != '1':
                continue
            dist = 0
            for j in range(i+1, l):
                if b[j] == '1':
                    dist = j - i 
                    break
            maxDist = max(dist, maxDist)
        
        return maxDist

