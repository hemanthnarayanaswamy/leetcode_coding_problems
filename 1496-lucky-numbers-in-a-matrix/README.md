<h2><a href="https://leetcode.com/problems/lucky-numbers-in-a-matrix">1496. Lucky Numbers in a Matrix</a></h2><h3>Easy</h3><hr><p>Given an <code>m x n</code> matrix of <strong>distinct </strong>numbers, return <em>all <strong>lucky numbers</strong> in the matrix in <strong>any </strong>order</em>.</p>

<p>A <strong>lucky number</strong> is an element of the matrix such that it is the minimum element in its row and maximum in its column.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[3,7,8],[9,11,13],[15,16,17]]
<strong>Output:</strong> [15]
<strong>Explanation:</strong> 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
<strong>Output:</strong> [12]
<strong>Explanation:</strong> 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[7,8],[1,2]]
<strong>Output:</strong> [7]
<strong>Explanation:</strong> 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= n, m &lt;= 50</code></li>
	<li><code>1 &lt;= matrix[i][j] &lt;= 10<sup>5</sup></code>.</li>
	<li>All elements in the matrix are distinct.</li>
</ul>

# Approach 
* `Find out and save the minimum of each row and maximum of each column in two lists.`
* **A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.**

Note: **Given Matrix has distinct Numbers**

**If Number is present in the the `minimum Tracker elements in Row` and `Maxium Tracker Elements in Column`, Then those are our Lucky Numbers**
![](https://leetcode.com/problems/lucky-numbers-in-a-matrix/Figures/1380/1380A.png)
* Use `set()` to get the intersection of the elements. 

```python
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        row = [float('inf')] * m
        col = [0] * n

        for i in range(m):
            for j in range(n):
                num = matrix[i][j]
                if num < row[i]:
                    row[i] = num
                if num > col[j]:
                    col[j] = num
        
        return list(set(row) & set(col))
```
<p>Hence, we can conclude that there can be at most one lucky number. If it exists, it can be found as follows: the lucky number is the minimum element in its row and the maximum element in its column. Therefore, we first find the minimum element of each row and then determine the maximum of these minimums as rowMinMax. Similarly, we find the maximum of each column and then determine the minimum of these maximums as colMaxMin. If rowMinMax equals colMaxMin, then this value is the lucky number; otherwise, we return an empty list. </p>

---
# Optimal Solution 
1. Iterate over each row and find the minimum as `rMin`, then find the maximum of these minimum elements in each row as `rMinMax`.
2. Iterate over each column and find the maximum as `cMax`, then find the minimum of these maximum elements in each column as `cMaxMin`.
3. **If the values `rMinMax and cMaxMin` are `equal` then return `rMinMax or cMaxMin`. Otherwise, return an empty list.**

```python
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        N, M = len(matrix), len(matrix[0])

        r_min_max = float('-inf')
        for i in range(N):
            r_min = min(matrix[i])  
            r_min_max = max(r_min_max, r_min)

        c_max_min = float('inf')
        for i in range(M):
            c_max = max(matrix[j][i] for j in range(N))
            c_max_min = min(c_max_min, c_max)

        if r_min_max == c_max_min:
            return [r_min_max]
        else:
            return []
```
