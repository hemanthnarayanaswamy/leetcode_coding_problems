class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        
        stack = []
        for slot in intervals:
            print(stack, slot)
            if stack:
                if slot[0] not in range(stack[-1][0], stack[-1][1]+1) or slot[1] not in range(stack[-1][0], stack[-1][1]+1):
                    stack.append(slot)
            else:
                stack.append(slot)
        
        return len(stack)
