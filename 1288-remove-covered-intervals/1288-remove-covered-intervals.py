class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        
        prev = intervals[0]
        count = 1
        
        for i in range(1, len(intervals)):
            if prev[0] <= intervals[i][0] <= prev[1] and prev[0] <= intervals[i][1] <= prev[1]:
               continue
            
            count += 1
            prev = intervals[i]

        return count
