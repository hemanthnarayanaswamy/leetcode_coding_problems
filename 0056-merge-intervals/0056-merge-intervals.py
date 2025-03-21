class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort() # DON'T USE
        intervals.sort(key = lambda i: i[0])  #sort the intervals by the first values
        result = [intervals[0]]  ## Initiating result with first element of intervals for references 
        for i in range(1, len(intervals)):
            current_element = result[-1]
            next_element = intervals[i]
            if current_element[1] >= next_element[0]:
                current_element[1] = max(current_element[1],next_element[1])
            else:
                result.append(next_element)

        return result
        