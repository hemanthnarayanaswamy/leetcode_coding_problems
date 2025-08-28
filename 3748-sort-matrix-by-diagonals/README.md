<h2><a href="https://leetcode.com/problems/sort-matrix-by-diagonals">3748. Sort Matrix by Diagonals</a></h2><h3>Medium</h3><hr><p>You are given an <code>n x n</code> square matrix of integers <code>grid</code>. Return the matrix such that:</p>

<ul>
	<li>The diagonals in the <strong>bottom-left triangle</strong> (including the middle diagonal) are sorted in <strong>non-increasing order</strong>.</li>
	<li>The diagonals in the <strong>top-right triangle</strong> are sorted in <strong>non-decreasing order</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,7,3],[9,8,2],[4,5,6]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[8,2,3],[9,6,7],[4,5,1]]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/12/29/4052example1drawio.png" style="width: 461px; height: 181px;" /></p>

<p>The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:</p>

<ul>
	<li><code>[1, 8, 6]</code> becomes <code>[8, 6, 1]</code>.</li>
	<li><code>[9, 5]</code> and <code>[4]</code> remain unchanged.</li>
</ul>

<p>The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:</p>

<ul>
	<li><code>[7, 2]</code> becomes <code>[2, 7]</code>.</li>
	<li><code>[3]</code> remains unchanged.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0,1],[1,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[2,1],[1,0]]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/12/29/4052example2adrawio.png" style="width: 383px; height: 141px;" /></p>

<p>The diagonals with a black arrow must be non-increasing, so <code>[0, 2]</code> is changed to <code>[2, 0]</code>. The other diagonals are already in the correct order.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[1]]</span></p>

<p><strong>Explanation:</strong></p>

<p>Diagonals with exactly one element are already in order, so no changes are needed.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>grid.length == grid[i].length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>-10<sup>5</sup> &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>

# Solution 
* Looking at your code, you're currently grouping elements by their main diagonal (top-left to bottom-right) using `i+j` as the key.
`gridMap[i+j].append(grid[i][j])`
* If the problem is asking for the anti-diagonal (top-right to bottom-left), you need to change the key formula to `i-j`
`gridMap[i-j].append(grid[i][j])`

* Group the diagonal elements and to sort based on upper and lower triangel use greater and lesser then 0 logic
* Sort individual based on the increasing and decreasing conditions. 
```python
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        gridMap = defaultdict(list)
        n = len(grid)

        for i in range(n):
            for j in range(n):
                gridMap[i-j].append(grid[i][j])
        
        for k in gridMap:
            if k < 0: 
                gridMap[k].sort(reverse=True)
            else:
                gridMap[k].sort()

        for i in range(n):
            for j in range(n):
                grid[i][j] = gridMap[i-j].pop()
                
        return grid
```
---
# Diagonal Matrix Sorting - Logic Notes

## Problem Understanding
- Sort elements within each anti-diagonal of a matrix
- Anti-diagonals run from top-right to bottom-left
- Each anti-diagonal has elements where `i-j` is constant

## Key Logic Points

### 1. Grouping Elements by Anti-Diagonal
```python
gridMap[i-j].append(grid[i][j])
```
- Use `i-j` as the key to group elements on same anti-diagonal
- Elements with same `i-j` value belong to same anti-diagonal

### 2. Anti-Diagonal Classification
- **Positive keys (k > 0)**: Upper anti-diagonals (above main diagonal)
- **Zero key (k = 0)**: Main anti-diagonal 
- **Negative keys (k < 0)**: Lower anti-diagonals (below main diagonal)

### 3. Sorting Strategy
```python
if k > 0:
    gridMap[k].sort(reverse=True)  # Descending
else:
    gridMap[k].sort()              # Ascending
```

### 4. Placing Elements Back
```python
grid[i][j] = gridMap[i-j].pop(0)  # Use pop(0) to maintain order
```
- Use `pop(0)` instead of `pop()` to remove from beginning
- Maintains the sorted order when placing back

## Common Mistakes to Avoid
1. Using `i+j` instead of `i-j` (groups main diagonals, not anti-diagonals)
2. Wrong sorting condition (`k < 0` vs `k > 0`)
3. Using `pop()` instead of `pop(0)` - disrupts sorted order
4. Forgetting that matrix traversal order matters for placement

## Visual Example
For 3x3 matrix, anti-diagonal groups by `i-j`:
```
k=2:  [grid[2][0]]
k=1:  [grid[1][0], grid[2][1]]
k=0:  [grid[0][0], grid[1][1], grid[2][2]]
k=-1: [grid[0][1], grid[1][2]]
k=-2: [grid[0][2]]
```
```python
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        gridMap = defaultdict(list)
        n = len(grid)

        for i in range(n):
            for j in range(n):
                gridMap[i-j].append(grid[i][j])
        
        for k in gridMap:
            if k < 0: 
                gridMap[k].sort()
            else:
                gridMap[k].sort(reverse=True)

        for i in range(n):
            for j in range(n):
                grid[i][j] = gridMap[i-j].pop(0)
                
        return grid
```
