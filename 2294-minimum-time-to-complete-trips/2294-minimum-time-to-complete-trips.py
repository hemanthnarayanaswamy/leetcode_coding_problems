class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 1, min(time)*totalTrips

        while l < r:
            m = (l + r) // 2
            tmp = 0
            for t in time:
                tmp += (m // t)
            
            if tmp >= totalTrips:
                r = m
            else:
                l = m + 1
        
        return l