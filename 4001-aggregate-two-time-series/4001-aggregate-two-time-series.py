class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        n1 = len(series1)
        n2 = len(series2)

        ans = []
        uniqueTime = set()
        p1 = p2 = 0

        for t1, v1 in series1:
            while p2 < n2-1 and t1 > series2[p2][0]:
                p2 += 1
            
            if t1 <= series2[p2][0]:
                v2 = series2[p2][1]
            else:
                v2 = 0
            ans.append([t1, v1+v2])
            uniqueTime.add(t1)
        
        for t2, v2 in series2:
            while p1 < n1-1 and t2 > series1[p1][0]:
                p1 += 1
            
            if t2 <= series1[p1][0]:
                v1 = series1[p1][1]
            else:
                v1 = 0

            if t2 not in uniqueTime:
                ans.append([t2, v1+v2])
                uniqueTime.add(t2)

        return sorted(ans)
