class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n+1)
            
        for f, l, s in bookings:
            diff[f] += s
            if l + 1 <= n:
                diff[l+1] -= s
        
        for i in range(1, n+1):
            diff[i] += diff[i-1]
        
        return diff[1:]
