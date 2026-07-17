class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        occupiedIntervals = sorted(occupiedIntervals, key=lambda x: (x[0], -x[1]))

        mergedIntervals = [occupiedIntervals[0]]

        for i in range(1, len(occupiedIntervals)):
            s1, e1 = mergedIntervals[-1]
            s2, e2 = occupiedIntervals[i]

            if e1 + 1 < s2:
                mergedIntervals.append([s2, e2])
            elif s2 <= e1 + 1 <= e2:
                mergedIntervals.pop()
                mergedIntervals.append([s1, e2])
        
        res = []

        for s, e in mergedIntervals:
            if e < freeStart or s > freeEnd:
                res.append([s, e])
            else:
                if s < freeStart:
                    res.append([s, freeStart - 1])
                
                if e > freeEnd:
                    res.append([freeEnd + 1, e])
        
        return res
