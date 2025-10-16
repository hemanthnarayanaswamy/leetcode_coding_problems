class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def ComputeTrips(minTime):
            trips = 0
            for t in time:
                trips += (minTime // t)
                if trips >= totalTrips: # Early Termination to avoid large sums
                    return trips
            return trips
        
        l, r = 1, min(time)*totalTrips

        while l < r:
            m = (l + r) // 2
            trips = ComputeTrips(m)

            if trips < totalTrips:
                l = m + 1
            else:
                r = m

        return l