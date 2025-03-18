class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats=sorted(seats)
        students=sorted(students)
        cnt=0
        for i in range(len(seats)) :
            cnt=cnt+abs(seats[i] - students[i])
        return cnt