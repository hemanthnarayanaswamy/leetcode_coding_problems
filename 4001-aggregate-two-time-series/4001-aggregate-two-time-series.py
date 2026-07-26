class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        ans = []
        uniqueTime = set()

        def aggregatedSeries(s1, s2):
            p = 0
            n1 = len(s1)
            n2 = len(s2)

            for t1, v1 in s1:
                if t1 in uniqueTime:
                    continue

                while p < n2-1 and t1 > s2[p][0]:
                    p += 1
                
                if t1 <= s2[p][0]:
                    v2 = s2[p][1]
                else:
                    v2 = 0
                
                ans.append([t1, v1+v2])
                uniqueTime.add(t1)
            return

        aggregatedSeries(series1, series2)
        aggregatedSeries(series2, series1)
        return sorted(ans)
