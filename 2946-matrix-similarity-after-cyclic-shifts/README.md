<h2><a href="https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts">3215. Matrix Similarity After Cyclic Shifts</a></h2><h3>Easy</h3><hr><p>You are given an <code>m x n</code> integer matrix <code>mat</code> and an integer <code>k</code>. The matrix rows are 0-indexed.</p>

<p>The following proccess happens <code>k</code> times:</p>

<ul>
	<li><strong>Even-indexed</strong> rows (0, 2, 4, ...) are cyclically shifted to the left.</li>
</ul>

<p><img src="https://assets.leetcode.com/uploads/2024/05/19/lshift.jpg" style="width: 283px; height: 90px;" /></p>

<ul>
	<li><strong>Odd-indexed</strong> rows (1, 3, 5, ...) are cyclically shifted to the right.</li>
</ul>

<p><img src="https://assets.leetcode.com/uploads/2024/05/19/rshift-stlone.jpg" style="width: 283px; height: 90px;" /></p>

<p>Return <code>true</code> if the final modified matrix after <code>k</code> steps is identical to the original matrix, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>In each step left shift is applied to rows 0 and 2 (even indices), and right shift to row 1 (odd index).</p>

<p><img src="https://assets.leetcode.com/uploads/2024/05/19/t1-2.jpg" style="width: 857px; height: 150px;" /></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2024/05/19/t1-3.jpg" style="width: 632px; height: 150px;" /></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">mat = [[2,2],[2,2]], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>As all the values are equal in the matrix, even after performing cyclic shifts the matrix will remain the same.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= mat.length &lt;= 25</code></li>
	<li><code>1 &lt;= mat[i].length &lt;= 25</code></li>
	<li><code>1 &lt;= mat[i][j] &lt;= 25</code></li>
	<li><code>1 &lt;= k &lt;= 50</code></li>
</ul>

# Solution
* we cannot `mat = smat` change `smat` and check because here `mat & smat` are both reference to the same object so changing `smat` will also change `mat` and eventually both will be the same.

```python
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        r = k % n
        smat = copy.deepcopy(mat)

        if r == 0:
            return True
        
        while r:
            for i in range(len(smat)):
                if i % 2 == 0:
                    smat[i] = smat[i][1:] + smat[i][:1]
                else:
                    smat[i] = smat[i][-1:] + smat[i][:n-1]   
            r -= 1
        
        return mat == smat
```
* Instead of doing `one rotation` at a time, do `r` rotations at once.
* Determining whether a row cyclically shifted to the right by `k` positions is identical to the original is equivalent to checking whether it remains the same when shifted to the left by `k` positions. In essence, both checks verify whether `mat[i][j]=mat[i][(j+k) mod n]`, where `n` is the number of columns.

```python
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        k %= n

        for i in range(m):
            for j in range(n):
                if mat[i][j] != mat[i][(j+k) % n]:
                    return False
        
        return True
```

