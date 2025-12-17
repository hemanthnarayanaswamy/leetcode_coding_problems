<h2><a href="https://leetcode.com/problems/max-increase-to-keep-city-skyline/?envType=problem-list-v2&envId=n6j4czn6">825. Max Increase to Keep City Skyline</a></h2><h3>Medium</h3><hr><p>There is a city composed of <code>n x n</code> blocks, where each block contains a single building shaped like a vertical square prism. You are given a <strong>0-indexed</strong> <code>n x n</code> integer matrix <code>grid</code> where <code>grid[r][c]</code> represents the <strong>height</strong> of the building located in the block at row <code>r</code> and column <code>c</code>.</p>

<p>A city&#39;s <strong>skyline</strong> is the&nbsp;outer contour formed by all the building when viewing the side of the city from a distance. The <strong>skyline</strong> from each cardinal direction north, east, south, and west may be different.</p>

<p>We are allowed to increase the height of <strong>any number of buildings by any amount</strong> (the amount can be different per building). The height of a <code>0</code>-height building can also be increased. However, increasing the height of a building should <strong>not</strong> affect the city&#39;s <strong>skyline</strong> from any cardinal direction.</p>

<p>Return <em>the <strong>maximum total sum</strong> that the height of the buildings can be increased by <strong>without</strong> changing the city&#39;s <strong>skyline</strong> from any cardinal direction</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/21/807-ex1.png" style="width: 700px; height: 603px;" />
<pre>
<strong>Input:</strong> grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
<strong>Output:</strong> 35
<strong>Explanation:</strong> The building heights are shown in the center of the above image.
The skylines when viewed from each cardinal direction are drawn in red.
The grid after increasing the height of buildings without affecting skylines is:
gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[0,0,0],[0,0,0],[0,0,0]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Increasing the height of any building will result in the skyline changing.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>n == grid[r].length</code></li>
	<li><code>2 &lt;= n &lt;= 50</code></li>
	<li><code>0 &lt;= grid[r][c] &lt;= 100</code></li>
</ul>

# Approach 
**For every `square ([i][j])` calculate the max value it can have without altering the city skyline `(i.e. the minimum of the highest value of the column and row it is in)`**
`Than calculate the total sum of height increases you could do. So all your max values - the actual values. and return that number.`

The skyline looking from the top is `col_maxes = [max(column_0), max(column_1), ...]`. Similarly, the skyline from the left is `row_maxes [max(row_0), max(row_1), ...]`

In particular, each building `grid[r][c]` could become height `min(max(row_r), max(col_c))`, and this is the largest such height. If it were larger, say `grid[r][c] > max(row_r)`, then the part of the skyline `row_maxes = [..., max(row_r), ...]` would change.

These increases are also independent (none of them change the skyline), so we can perform them independently.
# Solution 
```python
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = defaultdict(int)
        colMax = defaultdict(int)
        totalSum = 0
        n = len(grid)

        for i in range(n):
            rowMax[i] = max(grid[i])
            for j in range(n):
                h = grid[i][j]
                if colMax[j] < h:
                    colMax[j] = h
        
        for i in range(n):
            for j in range(n):
                totalSum += abs(grid[i][j] - min(rowMax[i], colMax[j]))
        
        return totalSum
```
---
```python
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowMax = [max(row) for row in grid]
        colMax = [max(col) for col in zip(*grid)]
        
        totalSum = 0
        for i in range(n):
            for j in range(n):
                totalSum += min(rowMax[i], colMax[j]) - grid[i][j]
        
        return totalSum
```
