class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort()
        #sort the intervals by the first values
        intervals.sort(key = lambda i: i[0])
        result = [intervals[0]]  ## Initiating result with first element of intervals for references 
        for i in range(1, len(intervals)):
            current_element = result[-1][1]
            if current_element >= intervals[i][0]:
                result[-1][1] = max(current_element,intervals[i][1])
            else:
                result.append(intervals[i])

        return result
        