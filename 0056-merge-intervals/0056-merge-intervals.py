class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]  ## Initiating result with first element of intervals for references 
        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1],intervals[i][1])
            else:
                result.append(intervals[i])
        return result
        