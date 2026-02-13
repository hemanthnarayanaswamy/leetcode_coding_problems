class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n+2)
            
        for f, l, s in bookings:
            diff[f] += s
            diff[l+1] -= s
        
        for i in range(1, n+2):
            diff[i] += diff[i-1]
        
        return diff[1:n+1]
