class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rowSeen = set()
        colSeen = set()
        totalSum = 0

        for query in queries[::-1]:
            t, idx, val = query
            if t == 0:
                if idx not in rowSeen:
                    totalSum += val * (n - len(colSeen))
                    rowSeen.add(idx)
            else:
                if idx not in colSeen:
                    totalSum += val * (n - len(rowSeen))
                    colSeen.add(idx)
        return totalSum