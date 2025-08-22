<h2><a href="https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i">3461. Find the Minimum Area to Cover All Ones I</a></h2><h3>Medium</h3><hr><p>You are given a 2D <strong>binary</strong> array <code>grid</code>. Find a rectangle with horizontal and vertical sides with the<strong> smallest</strong> area, such that all the 1&#39;s in <code>grid</code> lie inside this rectangle.</p>

<p>Return the <strong>minimum</strong> possible area of the rectangle.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0,1,0],[1,0,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/08/examplerect0.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 279px; height: 198px;" /></p>

<p>The smallest rectangle has a height of 2 and a width of 3, so it has an area of <code>2 * 3 = 6</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,0],[0,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/08/examplerect1.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 204px; height: 201px;" /></p>

<p>The smallest rectangle has both height and width 1, so its area is <code>1 * 1 = 1</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= grid.length, grid[i].length &lt;= 1000</code></li>
	<li><code>grid[i][j]</code> is either 0 or 1.</li>
	<li>The input is generated such that there is at least one 1 in <code>grid</code>.</li>
</ul>

# Solution 
* Its a brute force solution 
`area = (max_row - min_row + 1) * (max_col - min_col + 1)`
```python
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_height, min_width = float('inf'), float('inf')
        max_height, max_width = 0, 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    min_height = min(min_height, i)
                    min_width = min(min_width, j)
                    max_height = max(max_height, i)
                    max_width = max(max_width, j)
        
        area = (max_height - min_height + 1) * (max_width - min_width + 1)

        return area
```

---
* If the min Height and Widht are computed then we don't need to compute them anymore 
```python
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_height, min_width = float('inf'), float('inf')
        max_height, max_width = 0, 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if i == 0:
                        min_height = 0
                    elif min_height != 0:
                        min_height = min(min_height, i)

                    if j == 0:
                        min_width = 0
                    elif min_width != 0:
                        min_width = min(min_width, j)

                    if i > max_height:
                        max_height = i

                    if j > max_width:
                        max_width = j

        return (max_height - min_height + 1) * (max_width - min_width + 1)
```

---

# Optimal Solution
```python
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        widths = []
        heights = []
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    widths.append(j)
                    heights.append(i)

        return (max(heights) - min(heights) + 1) * (max(widths) - min(widths) + 1)
```
