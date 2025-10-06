class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        result = float('inf')

        for s,t in tasks:
            tmp = s+t
            if tmp < result:
                result = tmp
        
        return result
        