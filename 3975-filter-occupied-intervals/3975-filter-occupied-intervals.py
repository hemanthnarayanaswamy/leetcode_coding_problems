class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        occupiedIntervals.sort(key= lambda x: x[0])

        merged = [occupiedIntervals[0]]

        for s, e in occupiedIntervals[1:]:
            prev_end = merged[-1][1]

            if s > prev_end + 1:
                merged.append([s, e])
            else:
                merged[-1][1] = max(e, prev_end)

        if freeEnd < merged[0][0] or freeStart > merged[-1][1]:
            return merged
        
        result = []

        for s, e in merged:
            if e < freeStart or s > freeEnd:
                result.append([s, e])
            else:
                if freeStart > s:
                    result.append([s, freeStart - 1])
                if e > freeEnd:
                    result.append([freeEnd + 1, e])

        return result