<h2><a href="https://leetcode.com/problems/sum-of-matrix-after-queries">2838. Sum of Matrix After Queries</a></h2><h3>Medium</h3><hr><p>You are given an integer <code>n</code> and a <strong>0-indexed</strong>&nbsp;<strong>2D array</strong> <code>queries</code> where <code>queries[i] = [type<sub>i</sub>, index<sub>i</sub>, val<sub>i</sub>]</code>.</p>

<p>Initially, there is a <strong>0-indexed</strong> <code>n x n</code> matrix filled with <code>0</code>&#39;s. For each query, you must apply one of the following changes:</p>

<ul>
	<li>if <code>type<sub>i</sub> == 0</code>, set the values in the row with <code>index<sub>i</sub></code> to <code>val<sub>i</sub></code>, overwriting any previous values.</li>
	<li>if <code>type<sub>i</sub> == 1</code>, set the values in the column with <code>index<sub>i</sub></code> to <code>val<sub>i</sub></code>, overwriting any previous values.</li>
</ul>

<p>Return <em>the sum of integers in the matrix after all queries are applied</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/05/11/exm1.png" style="width: 681px; height: 161px;" />
<pre>
<strong>Input:</strong> n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
<strong>Output:</strong> 23
<strong>Explanation:</strong> The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 23. 
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/05/11/exm2.png" style="width: 681px; height: 331px;" />
<pre>
<strong>Input:</strong> n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
<strong>Output:</strong> 17
<strong>Explanation:</strong> The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 17.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>queries[i].length == 3</code></li>
	<li><code>0 &lt;= type<sub>i</sub> &lt;= 1</code></li>
	<li><code>0 &lt;= index<sub>i</sub>&nbsp;&lt; n</code></li>
	<li><code>0 &lt;= val<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>

# Approach
1. Process queries in reversed order, as the latest queries represent the most recent changes in the matrix.
2. Once you encounter an operation on some row/column, no further operations will affect the values in this row/column. Keep track of seen rows and columns with a set. 
3. When operating on an unseen row/column, the number of affected cells is the number of columns/rows you haven't previously seen. 

**If it's a `row assignment (t == 0)` and the row is not seen, it sets that row’s cells for every column that is not already fixed by a seen column. `Contribution = val * (n - len(colSeen))`. Then mark the row seen.**
**If it's a `column assignment (t == 1)` and the column is not seen, it sets that column’s cells for every row not already fixed by a seen row. `Contribution = val * (n - len(rowSeen))`. Then mark the column seen.**


```ini
Quick trace for n=3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]] (processed reversed):

(1,0,4) col 0 val 4 -> add 4*(3-0)=12, colSeen={0}
(0,2,3) row 2 val 3 -> add 3*(3-1)=6, rowSeen={2} # the idea sum of that row is (3 * 3) but we already by coloumn 0 as value assigned so we set value in only column 1 & 2, (3 * 3 - 3 * 1) = 3*(3 - 1) = 6
(1,2,2) col 2 val 2 -> add 2*(3-1)=4, colSeen={0,2} 
(0,0,1) row 0 val 1 -> add 1*(3-2)=1, rowSeen={2,0}
Total = 12+6+4+1 = 23
```

# Solution 
```python
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rowSeen = set()
        colSeen = set()
        totalSum = 0

        for query in queries[::-1]:
            t, idx, val = query
            if not t:
                if idx not in rowSeen:
                    totalSum += val * (n - len(colSeen))
                    rowSeen.add(idx)
            else:
                if idx not in colSeen:
                    totalSum += val * (n - len(rowSeen))
                    colSeen.add(idx)
        return totalSum
```
---
# Optimal Solution 
```python
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
```
