class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        prevTime = longestTime = events[0][1]
        res = events[0][0]

        for i in range(1, len(events)):
            idx, time = events[i]
            tmpTime = (time - prevTime)

            if tmpTime > longestTime:
                longestTime = tmpTime
                res = idx
            elif tmpTime == longestTime:
                res = min(res, idx)
            
            prevTime = time
        
        return res

