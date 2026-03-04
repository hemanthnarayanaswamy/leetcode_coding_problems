<h2><a href="https://leetcode.com/problems/special-positions-in-a-binary-matrix">1704. Special Positions in a Binary Matrix</a></h2><h3>Easy</h3><hr><p>Given an <code>m x n</code> binary matrix <code>mat</code>, return <em>the number of special positions in </em><code>mat</code><em>.</em></p>

<p>A position <code>(i, j)</code> is called <strong>special</strong> if <code>mat[i][j] == 1</code> and all other elements in row <code>i</code> and column <code>j</code> are <code>0</code> (rows and columns are <strong>0-indexed</strong>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/23/special1.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>Input:</strong> mat = [[1,0,0],[0,0,1],[1,0,0]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/special-grid.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>Input:</strong> mat = [[1,0,0],[0,1,0],[0,0,1]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> (0, 0), (1, 1) and (2, 2) are special positions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>mat[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

# Solution
* First Iteration, We count the frequency of ones, in each `rows` and `columns`
* and In the Second Iteration, when there is one, for that respective `row` and `col`, when check if the frequency is exactly `1`, than that means **We have a special position +1**

```python
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        
        res = 0
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    res += 1
        
        return res
```
---
```python
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    if rows[i] == 1 and cols[j] == 1:
                        ans += 1
        
        return ans
```
