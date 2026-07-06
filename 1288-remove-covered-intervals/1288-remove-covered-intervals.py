class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0], -x[1]))
        prev = intervals[0]

        count = len(intervals)

        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev[0] and intervals[i][1] <= prev[1]:
                count -= 1
            else:
                prev = intervals[i]
        
        return count

        