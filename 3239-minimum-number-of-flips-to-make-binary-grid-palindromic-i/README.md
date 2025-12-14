<h2><a href="https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i">3526. Minimum Number of Flips to Make Binary Grid Palindromic I</a></h2><h3>Medium</h3><hr><p>You are given an <code>m x n</code> binary matrix <code>grid</code>.</p>

<p>A row or column is considered <strong>palindromic</strong> if its values read the same forward and backward.</p>

<p>You can <strong>flip</strong> any number of cells in <code>grid</code> from <code>0</code> to <code>1</code>, or from <code>1</code> to <code>0</code>.</p>

<p>Return the <strong>minimum</strong> number of cells that need to be flipped to make <strong>either</strong> all rows <strong>palindromic</strong> or all columns <strong>palindromic</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,0,0],[0,0,0],[0,0,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/07/07/screenshot-from-2024-07-08-00-20-10.png" style="width: 420px; height: 108px;" /></p>

<p>Flipping the highlighted cells makes all the rows palindromic.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = </span>[[0,1],[0,1],[0,0]]</p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/07/07/screenshot-from-2024-07-08-00-31-23.png" style="width: 300px; height: 100px;" /></p>

<p>Flipping the highlighted cell makes all the columns palindromic.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1],[0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>All rows are already palindromic.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m * n &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 1</code></li>
</ul>

# Solution 
**Split the problem into 2 parts `minimum flips to make all rows palindromatic` and `minimum flips to all column palindromatic`.**
**Get the flip count for both operations and return the minimum**
**Use two pointer to check the palindrome seperately**

```python
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        flipr = 0
        flipc = 0
        
        def checkPalindrome(seq):
            flip = 0
            l, r = 0, len(seq)-1
            while l <= r:
                if seq[l] != seq[r]:
                    flip += 1
                l += 1
                r -= 1
            return flip
        
        for row in grid:
            flipr += checkPalindrome(row)
        
        for col in zip(*grid):
            flipc += checkPalindrome(col)
            
            if flipc >= flipr: # Quick return of flipr if flipc at any point is greater or equal the the flipr value
                return flipr
        
        return flipc
```
---
# Optimal Solution
```python
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if n == 1 or m == 1: return 0
        rc = 0
        for r in grid:
            x = 0
            y = m - 1
            while x < y:
                if r[x] != r[y]:
                    rc += 1
                x += 1
                y -= 1
        cc = 0
        for j in range(m):
            x = 0
            y = n - 1
            while x < y:
                if grid[x][j] != grid[y][j]:
                    cc += 1
                x += 1
                y -= 1
        return min(rc,cc)
```
