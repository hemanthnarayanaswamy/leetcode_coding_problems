class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        bookings = defaultdict(set)
        left = {2, 3, 4, 5}
        middle = {4, 5, 6, 7}
        right = {6, 7, 8, 9}
        
        for r, s in reservedSeats:
            if s != 1 and s != 10:
                bookings[r].add(s)

        ans = (n - len(bookings)) * 2

        for r, seats in bookings.items():
            left_available = seats.isdisjoint(left)
            right_available = seats.isdisjoint(right)
            middle_available = seats.isdisjoint(middle)
            
            if left_available and right_available:
                ans += 2
            elif left_available or middle_available or right_available:
                ans += 1

        return ans
