<h2><a href="https://leetcode.com/problems/shift-2d-grid/">1386. Shift 2D Grid</a></h2><h3>Easy</h3><hr><p>Given a 2D <code>grid</code> of size <code>m x n</code>&nbsp;and an integer <code>k</code>. You need to shift the <code>grid</code>&nbsp;<code>k</code> times.</p>

<p>In one shift operation:</p>

<ul>
	<li>Element at <code>grid[i][j]</code> moves to <code>grid[i][j + 1]</code>.</li>
	<li>Element at <code>grid[i][n - 1]</code> moves to <code>grid[i + 1][0]</code>.</li>
	<li>Element at <code>grid[m&nbsp;- 1][n - 1]</code> moves to <code>grid[0][0]</code>.</li>
</ul>

<p>Return the <em>2D grid</em> after applying shift operation <code>k</code> times.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/11/05/e1.png" style="width: 400px; height: 178px;" />
<pre>
<strong>Input:</strong> <code>grid</code> = [[1,2,3],[4,5,6],[7,8,9]], k = 1
<strong>Output:</strong> [[9,1,2],[3,4,5],[6,7,8]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/11/05/e2.png" style="width: 400px; height: 166px;" />
<pre>
<strong>Input:</strong> <code>grid</code> = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
<strong>Output:</strong> [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> <code>grid</code> = [[1,2,3],[4,5,6],[7,8,9]], k = 9
<strong>Output:</strong> [[1,2,3],[4,5,6],[7,8,9]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m ==&nbsp;grid.length</code></li>
	<li><code>n ==&nbsp;grid[i].length</code></li>
	<li><code>1 &lt;= m &lt;= 50</code></li>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>-1000 &lt;= grid[i][j] &lt;= 1000</code></li>
	<li><code>0 &lt;= k &lt;= 100</code></li>
</ul>

# Approach
`Flatten this 2d array and do some modulo with k if is bigger than the length.`
**When approaching this problem, it's helpful to think of the 2D grid as a flattened 1D array for easier indexing. By treating the grid this way, each element's position can be represented by a single index, which simplifies the logic needed to perform the shift.**

**To Rotate a `1D` array by `k` step make sure `k = k % n` and then ` grid1D[:k], grid1D[k:] = grid1D[-k:], grid1D[:-k]`**

* Conver the `1D` array into `2D` array with row size `m`

* Conver `2D` array into `1D`: `1D = [2D[i][j] for i in range(m) for j in range(n)]`
```ini
arr = [1,2,3,4,5,6,7,8,9]
m = 3
res = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(0, len(arr), m): (start, stop, step)
            res.append(arr[i:i+m])
```

```python
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid[0])
        grid1D = []
        res = []

        for row in grid:
            grid1D.extend(row)
        
        k = (k % len(grid1D))

        if k == 0:
            return grid
        
        grid1D[:k], grid1D[k:] = grid1D[-k:], grid1D[:-k] # Rotating the 1D array by 
        
        for i in range(0, len(grid1D), m):
            res.append(grid1D[i:i+m])

        return res
```
---
```python
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        
        # Flatten the grid
        flat = [grid[i][j] for i in range(m) for j in range(n)]
        
        # Effective shifts
        k = k % total
        
        # Rotate the array
        flat = flat[-k:] + flat[:-k]
        
        # Rebuild the grid
        new_grid = []
        for i in range(m):
            row = flat[i*n:(i+1)*n]
            new_grid.append(row)
        
        return new_grid
```
        
