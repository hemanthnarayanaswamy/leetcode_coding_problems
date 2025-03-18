class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        moves = [abs(seat-student) for student, seat in zip(sorted(students), sorted(seats))]
        return sum(moves)