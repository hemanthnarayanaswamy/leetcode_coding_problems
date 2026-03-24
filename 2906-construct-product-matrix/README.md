<h2><a href="https://leetcode.com/problems/construct-product-matrix">3031. Construct Product Matrix</a></h2><h3>Medium</h3><hr><p>Given a <strong>0-indexed</strong> 2D integer matrix <code><font face="monospace">grid</font></code><font face="monospace"> </font>of size <code>n * m</code>, we define a <strong>0-indexed</strong> 2D matrix <code>p</code> of size <code>n * m</code> as the <strong>product</strong> matrix of <code>grid</code> if the following condition is met:</p>

<ul>
	<li>Each element <code>p[i][j]</code> is calculated as the product of all elements in <code>grid</code> except for the element <code>grid[i][j]</code>. This product is then taken modulo <code><font face="monospace">12345</font></code>.</li>
</ul>

<p>Return <em>the product matrix of</em> <code><font face="monospace">grid</font></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,2],[3,4]]
<strong>Output:</strong> [[24,12],[8,6]]
<strong>Explanation:</strong> p[0][0] = grid[0][1] * grid[1][0] * grid[1][1] = 2 * 3 * 4 = 24
p[0][1] = grid[0][0] * grid[1][0] * grid[1][1] = 1 * 3 * 4 = 12
p[1][0] = grid[0][0] * grid[0][1] * grid[1][1] = 1 * 2 * 4 = 8
p[1][1] = grid[0][0] * grid[0][1] * grid[1][0] = 1 * 2 * 3 = 6
So the answer is [[24,12],[8,6]].</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[12345],[2],[1]]
<strong>Output:</strong> [[2],[0],[0]]
<strong>Explanation:</strong> p[0][0] = grid[0][1] * grid[0][2] = 2 * 1 = 2.
p[0][1] = grid[0][0] * grid[0][2] = 12345 * 1 = 12345. 12345 % 12345 = 0. So p[0][1] = 0.
p[0][2] = grid[0][0] * grid[0][1] = 12345 * 2 = 24690. 24690 % 12345 = 0. So p[0][2] = 0.
So the answer is [[2],[0],[0]].</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == grid.length&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m == grid[i].length&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= n * m &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>9</sup></code></li>
</ul>

# Solution
1. Convert the 2D into 1D array
2. Then compute the `prefix` product and `postfix` product, use the `% 12345` for `prefix & postfix` also `res` to store lower numbers.

```python
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        nums = []

        for i in range(m):
            for j in range(n):
                nums.append(grid[i][j])

        res = [1]*(n*m)

        prefix = 1
        for i in range(n*m):
            res[i] = prefix
            prefix = (prefix * nums[i]) % 12345
        
        postfix = 1
        for i in range((n*m)-1, -1, -1):
            res[i] = (res[i] * postfix) % 12345
            postfix = (postfix * nums[i]) % 12345
        
        i = 0
        prodMat = []
        for _ in range(m):
            tmp = []
            for _ in range(n):
                tmp.append(res[i])
                i += 1
            prodMat.append(tmp)

        return prodMat
```
* use list compression for conversion between `1D -> 2D` & `2D to 1D`

```python
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        nums = [element for row in grid for element in row]
        lenght = len(nums)

        res = [1]*(lenght)

        prefix = 1
        for i in range(lenght):
            res[i] = prefix
            prefix = (prefix * nums[i]) % 12345
        
        postfix = 1
        for i in range((lenght)-1, -1, -1):
            res[i] = (res[i] * postfix) % 12345
            postfix = (postfix * nums[i]) % 12345
        
        return [res[i:i+n] for i in range(0, lenght, n)]
```
---
* you can avoid the conversion

```python
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        p = [[0] * m for _ in range(n)]

        suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = suffix
                suffix = (suffix * grid[i][j]) % MOD

        prefix = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = (p[i][j] * prefix) % MOD
                prefix = (prefix * grid[i][j]) % MOD

        return p
```
