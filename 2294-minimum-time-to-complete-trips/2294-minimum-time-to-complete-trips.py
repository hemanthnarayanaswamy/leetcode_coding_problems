class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def isFesible(minTime):
            trips = 0
            for t in time:
                trips += (minTime // t) # Number of tips a bus can take for new time
                if trips >= totalTrips: # Early Termination to avoid large sums
                    return True
            return False
        
        l, r = 1, min(time)*totalTrips

        while l < r:
            m = (l + r) // 2

            if isFesible(m):
                r = m
            else:
                l = m + 1

        return l 
# Complexity note: O(len(time) * log(min(time)*totalTrips)). Include this in comments.