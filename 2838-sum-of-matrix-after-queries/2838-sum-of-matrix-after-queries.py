class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        row_seen = set()    # 0/1 flags faster than set lookups
        col_seen = set()
        rem_rows = n
        rem_cols = n
        total = 0

        for t, idx, val in reversed(queries):
            if rem_rows == 0 and rem_cols == 0:
                break

            if t:
                if idx not in col_seen:
                    total += val * rem_rows
                    col_seen.add(idx)
                    rem_cols -= 1
            else:
                if idx not in row_seen:
                    total += val * rem_cols
                    row_seen.add(idx)
                    rem_rows -= 1
            
        return total