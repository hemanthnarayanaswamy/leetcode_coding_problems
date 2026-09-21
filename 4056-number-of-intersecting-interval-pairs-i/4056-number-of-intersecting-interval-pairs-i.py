class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],x[1]))
        n = len(intervals)
        intersect = 0

        for i in range(n):
            si, ei = intervals[i]
            for j in range(i+1, n):
                sj, ej = intervals[j]

                if sj <= ei:
                    intersect += 1
        
        return intersect