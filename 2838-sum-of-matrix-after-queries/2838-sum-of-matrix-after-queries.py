class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        col_visited = [False] * n
        col_visited_count = 0
        
        row_visited = [False] * n
        row_visited_count = 0
        
        res = 0

        for set_col, index, val in reversed(queries):
            if set_col:
                if col_visited[index]:
                    continue
                col_visited[index] = True
                col_visited_count += 1
                res += val * (n - row_visited_count)
            else:
                if row_visited[index]:
                    continue
                row_visited[index] = True
                row_visited_count += 1
                res += val * (n - col_visited_count)
        return res