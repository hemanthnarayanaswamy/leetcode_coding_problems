class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        intersect = 0

        for i in range(n):
            si, ei = intervals[i]
            for j in range(i+1, n):
                sj, ej = intervals[j]

                if max(si, sj) <= min(ei, ej):
                    intersect += 1
        
        return intersect