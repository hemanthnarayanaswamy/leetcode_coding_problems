class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        result = []

        for s,t in tasks:
            result.append(s+t)
        
        return min(result)
        