<h2><a href="https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation">2015. Determine Whether Matrix Can Be Obtained By Rotation</a></h2><h3>Easy</h3><hr><p>Given two <code>n x n</code> binary matrices <code>mat</code> and <code>target</code>, return <code>true</code><em> if it is possible to make </em><code>mat</code><em> equal to </em><code>target</code><em> by <strong>rotating</strong> </em><code>mat</code><em> in <strong>90-degree increments</strong>, or </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/20/grid3.png" style="width: 301px; height: 121px;" />
<pre>
<strong>Input:</strong> mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
<strong>Output:</strong> true
<strong>Explanation: </strong>We can rotate mat 90 degrees clockwise to make mat equal target.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/20/grid4.png" style="width: 301px; height: 121px;" />
<pre>
<strong>Input:</strong> mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to make mat equal to target by rotating mat.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/26/grid4.png" style="width: 661px; height: 184px;" />
<pre>
<strong>Input:</strong> mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
<strong>Output:</strong> true
<strong>Explanation: </strong>We can rotate mat 90 degrees clockwise two times to make mat equal target.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == mat.length == target.length</code></li>
	<li><code>n == mat[i].length == target[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>mat[i][j]</code> and <code>target[i][j]</code> are either <code>0</code> or <code>1</code>.</li>
</ul>

# Solution 
**90 Degree Rotation `mat[i][j] -> mat[j][n-i-1]`**
* Lets have a function that does the rotation of the array, and array can to rotated 3 times to have unique orientation but the 4 time will be same the first time
* first rotation 90, second rotation 180, thrid rotation 270 and fouth will return to the original array. 

**Use the Different fresh variable to store the result instead of inline assignment to the same variable**

```ini
tmp = [[0] * n] * n creates n references to the same row. 
Writing tmp[i][j] updates every row at column j. Build with a list-comprehension instead:

Correct way: tmp = [[0] * n for _ in range(n)]

Because it duplicates the same row object n times. List multiplication is shallow: [[0] * n] * n builds one inner list, then repeats references to it. All rows alias each other, so writing tmp[i][j] updates column j in every row.

Quick demonstration:

Construct:

row = [0, 0, 0]

tmp = [row, row, row] ← all entries point to the same row

Do tmp[1][2] = 9

Now tmp becomes [[0,0,9],[0,0,9],[0,0,9]] because it’s the same row three times.

You can see it via identities: id(tmp[0]) == id(tmp[1]) == id(tmp[2]).

tmp = [[0] * n for _ in range(n)]

Here the comprehension runs n times, building a new inner list each time, so rows are independent and mutating one doesn’t affect the others.
```
```python
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
        if mat == target:
            return True 

        def rotateMatrix(mat):
            tmp = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    tmp[i][j] = mat[j][n - i - 1] #out[i][j] = in[n - 1 - j][i]
            return tmp
        
        rotations = 0

        while rotations < 3:
            tmp = rotateMatrix(mat)
            if tmp == target:
                return True 
            mat = tmp
            rotations += 1
        
        return False
```
