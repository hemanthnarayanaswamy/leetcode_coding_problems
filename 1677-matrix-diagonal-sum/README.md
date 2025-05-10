<h2><a href="https://leetcode.com/problems/matrix-diagonal-sum">1677. Matrix Diagonal Sum</a></h2><h3>Easy</h3><hr><p>Given a&nbsp;square&nbsp;matrix&nbsp;<code>mat</code>, return the sum of the matrix diagonals.</p>

<p>Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/14/sample_1911.png" style="width: 336px; height: 174px;" />
<pre>
<strong>Input:</strong> mat = [[<strong>1</strong>,2,<strong>3</strong>],
&nbsp;             [4,<strong>5</strong>,6],
&nbsp;             [<strong>7</strong>,8,<strong>9</strong>]]
<strong>Output:</strong> 25
<strong>Explanation: </strong>Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> mat = [[<strong>1</strong>,1,1,<strong>1</strong>],
&nbsp;             [1,<strong>1</strong>,<strong>1</strong>,1],
&nbsp;             [1,<strong>1</strong>,<strong>1</strong>,1],
&nbsp;             [<strong>1</strong>,1,1,<strong>1</strong>]]
<strong>Output:</strong> 8
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> mat = [[<strong>5</strong>]]
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == mat.length == mat[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= mat[i][j] &lt;= 100</code></li>
</ul>

**if You observe matrix the primary diagonal are ( i == j ) and secondary diagonal are ( i + j = n-1)**

# Approach
* Travers a matrix
* primary diagonal are ( i == j ) i and j value is same so i use sum += mat[i][i];
* Not repete the value if( i != mat.length - i - 1)
* we know j = ( i + j = n-1), so we can write this also j= n-1-i
* In code we write line this sum += mat[i][mat.length-i-1];

```python 
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        result = 0

        for i in range(n):
            for j in range(n):
                if i == j:
                    result += mat[i][j]
                
                if i + j == n - 1:
                    result += mat[i][j]
        
        if n % 2 == 1:
            x = n // 2
            result -= mat[x][x]
        
        return result
```

# Improves Version 
```python
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        if n == 1:
            return mat[0][0]

        total_sum = 0

        for i in range(n):
            # primary diagonal
            total_sum += mat[i][i]

            # secondary diagonal
            if i != n - 1 - i:
                total_sum += mat[i][n - 1 - i]

        return total_sum
```
