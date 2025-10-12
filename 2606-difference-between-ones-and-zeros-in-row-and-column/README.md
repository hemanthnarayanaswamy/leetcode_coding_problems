<h2><a href="https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column">2606. Difference Between Ones and Zeros in Row and Column</a></h2><h3>Medium</h3><hr><p>You are given a <strong>0-indexed</strong> <code>m x n</code> binary matrix <code>grid</code>.</p>

<p>A <strong>0-indexed</strong> <code>m x n</code> difference matrix <code>diff</code> is created with the following procedure:</p>

<ul>
	<li>Let the number of ones in the <code>i<sup>th</sup></code> row be <code>onesRow<sub>i</sub></code>.</li>
	<li>Let the number of ones in the <code>j<sup>th</sup></code> column be <code>onesCol<sub>j</sub></code>.</li>
	<li>Let the number of zeros in the <code>i<sup>th</sup></code> row be <code>zerosRow<sub>i</sub></code>.</li>
	<li>Let the number of zeros in the <code>j<sup>th</sup></code> column be <code>zerosCol<sub>j</sub></code>.</li>
	<li><code>diff[i][j] = onesRow<sub>i</sub> + onesCol<sub>j</sub> - zerosRow<sub>i</sub> - zerosCol<sub>j</sub></code></li>
</ul>

<p>Return <em>the difference matrix </em><code>diff</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/11/06/image-20221106171729-5.png" style="width: 400px; height: 208px;" />
<pre>
<strong>Input:</strong> grid = [[0,1,1],[1,0,1],[0,0,1]]
<strong>Output:</strong> [[0,0,4],[0,0,4],[-2,-2,2]]
<strong>Explanation:</strong>
- diff[0][0] = <code>onesRow<sub>0</sub> + onesCol<sub>0</sub> - zerosRow<sub>0</sub> - zerosCol<sub>0</sub></code> = 2 + 1 - 1 - 2 = 0 
- diff[0][1] = <code>onesRow<sub>0</sub> + onesCol<sub>1</sub> - zerosRow<sub>0</sub> - zerosCol<sub>1</sub></code> = 2 + 1 - 1 - 2 = 0 
- diff[0][2] = <code>onesRow<sub>0</sub> + onesCol<sub>2</sub> - zerosRow<sub>0</sub> - zerosCol<sub>2</sub></code> = 2 + 3 - 1 - 0 = 4 
- diff[1][0] = <code>onesRow<sub>1</sub> + onesCol<sub>0</sub> - zerosRow<sub>1</sub> - zerosCol<sub>0</sub></code> = 2 + 1 - 1 - 2 = 0 
- diff[1][1] = <code>onesRow<sub>1</sub> + onesCol<sub>1</sub> - zerosRow<sub>1</sub> - zerosCol<sub>1</sub></code> = 2 + 1 - 1 - 2 = 0 
- diff[1][2] = <code>onesRow<sub>1</sub> + onesCol<sub>2</sub> - zerosRow<sub>1</sub> - zerosCol<sub>2</sub></code> = 2 + 3 - 1 - 0 = 4 
- diff[2][0] = <code>onesRow<sub>2</sub> + onesCol<sub>0</sub> - zerosRow<sub>2</sub> - zerosCol<sub>0</sub></code> = 1 + 1 - 2 - 2 = -2
- diff[2][1] = <code>onesRow<sub>2</sub> + onesCol<sub>1</sub> - zerosRow<sub>2</sub> - zerosCol<sub>1</sub></code> = 1 + 1 - 2 - 2 = -2
- diff[2][2] = <code>onesRow<sub>2</sub> + onesCol<sub>2</sub> - zerosRow<sub>2</sub> - zerosCol<sub>2</sub></code> = 1 + 3 - 2 - 0 = 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/11/06/image-20221106171747-6.png" style="width: 358px; height: 150px;" />
<pre>
<strong>Input:</strong> grid = [[1,1,1],[1,1,1]]
<strong>Output:</strong> [[5,5,5],[5,5,5]]
<strong>Explanation:</strong>
- diff[0][0] = onesRow<sub>0</sub> + onesCol<sub>0</sub> - zerosRow<sub>0</sub> - zerosCol<sub>0</sub> = 3 + 2 - 0 - 0 = 5
- diff[0][1] = onesRow<sub>0</sub> + onesCol<sub>1</sub> - zerosRow<sub>0</sub> - zerosCol<sub>1</sub> = 3 + 2 - 0 - 0 = 5
- diff[0][2] = onesRow<sub>0</sub> + onesCol<sub>2</sub> - zerosRow<sub>0</sub> - zerosCol<sub>2</sub> = 3 + 2 - 0 - 0 = 5
- diff[1][0] = onesRow<sub>1</sub> + onesCol<sub>0</sub> - zerosRow<sub>1</sub> - zerosCol<sub>0</sub> = 3 + 2 - 0 - 0 = 5
- diff[1][1] = onesRow<sub>1</sub> + onesCol<sub>1</sub> - zerosRow<sub>1</sub> - zerosCol<sub>1</sub> = 3 + 2 - 0 - 0 = 5
- diff[1][2] = onesRow<sub>1</sub> + onesCol<sub>2</sub> - zerosRow<sub>1</sub> - zerosCol<sub>2</sub> = 3 + 2 - 0 - 0 = 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

# Solution 
```python
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        onesRow = [0] * m
        onesColumn = [0] * n

        for i in range(m):
            for j in range(n):
                x = grid[i][j] 
                onesRow[i] +=  x
                onesColumn[j] += x
    
        diff = []

        for i in range(m):
            tmp = []
            rowScore = 2*onesRow[i] - n
            for j in range(n):
                totalScore = rowScore + (2*onesColumn[j] - m)
                tmp.append(totalScore)
            diff.append(tmp)

        return diff
```

```ini
Algebra: onesRow[i] + onesCol[j] - (m - onesRow[i]) - (n - onesCol[j]) simplifies to
(2*onesRow[i] - n) + (2*onesCol[j] - m).
Precompute rowScore[i] = 2*onesRow[i] - n and colScore[j] = 2*onesCol[j] - m, then sum.
```
---
# Optimal Solution 
```python
from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ones_row = [0] * m
        ones_col = [0] * n

        for i in range(m):
            row = grid[i]
            for j in range(n):
                v = row[j]
                ones_row[i] += v
                ones_col[j] += v

        row_score = [2*r - n for r in ones_row]
        col_score = [2*c - m for c in ones_col]

        return [[row_score[i] + col_score[j] for j in range(n)] for i in range(m)]
```
---
where:
- `onesRow[i]` = number of 1s in row `i`
- `onesColumn[j]` = number of 1s in column `j`
- `zerosRow[i] = n - onesRow[i]`
- `zerosColumn[j] = m - onesColumn[j]`

## Steps

1. **Initialize variables**
   - Let `m = len(grid)` and `n = len(grid[0])`
   - Create two arrays:
     - `onesRow` of length `m`, initialized to `0`
     - `onesColumn` of length `n`, initialized to `0`

2. **Count ones**
   - Iterate through each cell `(i, j)` in the grid:
     - If `grid[i][j] == 1`:
       - Increment `onesRow[i]` by 1
       - Increment `onesColumn[j]` by 1

3. **Precompute row and column scores**
   - For each row `i`, compute `rowScore[i] = 2 * onesRow[i] - n`
   - For each column `j`, compute `colScore[j] = 2 * onesColumn[j] - m`

4. **Compute the final diff matrix**
   - For each cell `(i, j)`:
     - `diff[i][j] = rowScore[i] + colScore[j]`

5. **Return the diff matrix**

## Complexity
- **Time Complexity:** `O(m * n)`
- **Space Complexity:** `O(m + n)`

---

### What changed: constant factors.
	•	You computed 2*onesRow[i]-n and 2*onesColumn[j]-m inside the fill loop. I precompute them once (rowScore, colScore) and add. Same big-O, fewer operations per cell.
	•	I also cache rowScore[i] per row to avoid repeated indexing. Micro win.

## Notes for the final solution:
	•	Validate input if needed: empty grid, rectangular shape.
	•	Use direct add v = grid[i][j] since values are 0/1; no branch.
	•	Prefer comprehensions for the diff build to cut Python overhead.
	•	Keep names consistent: ones_row, ones_col, row_score, col_score.
	•	Tests: [[0]], [[1,0,1]], non-square (e.g., 2×3), all-ones, all-zeros.
	•	If memory is tight and grid is large, you can stream rows: compute rowScore on the fly while keeping colScore precomputed.

---
```python
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        diffX=[0]*m
        diffY=[0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    diffX[i]+=1
                    diffY[j]+=1

        o=m+n
        for i in range(m):
            for j in range(n):
                grid[i][j]=2*(diffX[i]+diffY[j])-o
        return grid
```
