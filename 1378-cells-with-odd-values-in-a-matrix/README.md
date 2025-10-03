<h2><a href="https://leetcode.com/problems/cells-with-odd-values-in-a-matrix">1378. Cells with Odd Values in a Matrix</a></h2><h3>Easy</h3><hr><p>There is an <code>m x n</code> matrix that is initialized to all <code>0</code>&#39;s. There is also a 2D array <code>indices</code> where each <code>indices[i] = [r<sub>i</sub>, c<sub>i</sub>]</code> represents a <strong>0-indexed location</strong> to perform some increment operations on the matrix.</p>

<p>For each location <code>indices[i]</code>, do <strong>both</strong> of the following:</p>

<ol>
	<li>Increment <strong>all</strong> the cells on row <code>r<sub>i</sub></code>.</li>
	<li>Increment <strong>all</strong> the cells on column <code>c<sub>i</sub></code>.</li>
</ol>

<p>Given <code>m</code>, <code>n</code>, and <code>indices</code>, return <em>the <strong>number of odd-valued cells</strong> in the matrix after applying the increment to all locations in </em><code>indices</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/10/30/e1.png" style="width: 600px; height: 118px;" />
<pre>
<strong>Input:</strong> m = 2, n = 3, indices = [[0,1],[1,1]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/10/30/e2.png" style="width: 600px; height: 150px;" />
<pre>
<strong>Input:</strong> m = 2, n = 2, indices = [[1,1],[0,0]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Final matrix = [[2,2],[2,2]]. There are no odd numbers in the final matrix.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>1 &lt;= indices.length &lt;= 100</code></li>
	<li><code>0 &lt;= r<sub>i</sub> &lt; m</code></li>
	<li><code>0 &lt;= c<sub>i</sub> &lt; n</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve this in <code>O(n + m + indices.length)</code> time with only <code>O(n + m)</code> extra space?</p>

# Solution 
* We create two hashMaps `rows` & `columns`, and cumulative the values for each row and each column by incrementing it. 
* In the next iteration, for the position `result[i][j] = rows.get(i, 0) + columns.get(j, 0)` for that position 
* We incement that count if its odd and finially return the count.

```python
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = {}
        column = {}
        result = [[0]*n] * m
        count = 0

        for r,c in indices:
            row[r] = row.get(r, 0) + 1
            column[c] = column.get(c, 0) + 1
        
        for i in range(m):
            for j in range(n):
                result[i][j] = row.get(i, 0) + column.get(j, 0)
                
                if result[i][j] % 2:
                    count += 1 

        return count
```
---
* We don't need to store the result array, we just need to count the odd values. 

```python
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = {}
        column = {}
        count = 0

        for r,c in indices: # cumulative values 
            row[r] = row.get(r, 0) + 1  
            column[c] = column.get(c, 0) + 1
        
        for i in range(m):
            for j in range(n): 
                if (row.get(i, 0) + column.get(j, 0)) % 2:
                    count += 1 

        return count  
```
---
```python
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0] * m
        column = [0] * n

        for r,c in indices: # cumulative values 
            row[r] +=  1  
            column[c] += 1
        
        odd_count = 0
        for i in range(m):
            for j in range(n): 
                if (row[i] + column[j]) % 2:
                    odd_count += 1 

        return odd_count  
```
---
```python
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row = [0] * m
        column = [0] * n

        for r,c in indices:  
            row[r] +=  1  
            column[c] += 1
        
        odd_count = 0
        for i in row:
            for j in column: 
                if (i + j) % 2:
                    odd_count += 1 

        return odd_count  
```
