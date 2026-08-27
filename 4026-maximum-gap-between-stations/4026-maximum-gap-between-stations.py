class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n1 = len(skill)
        n2 = len(station)

        if n1 <= 1:
            return 0

        earliest = [0] * n1
        latest = [0] * n1

        l1 = l2 = 0
        while l1 < n1 and l2 < n2:
            if skill[l1] == station[l2]:
                earliest[l1] = l2
                l1 += 1    
            l2 += 1
        
        r1, r2 = n1 -1, n2 - 1
        while r1 > -1 and r2 > -1:
            if skill[r1] == station[r2]:
                latest[r1] = r2
                r1 -= 1
            r2 -= 1
        
        maxGap = 0
        for i in range(1, n1):
            maxGap = max(maxGap, latest[i]-earliest[i-1])
        
        return maxGap

