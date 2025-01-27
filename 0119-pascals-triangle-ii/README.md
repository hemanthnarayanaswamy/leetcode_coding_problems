<h2><a href="https://leetcode.com/problems/pascals-triangle-ii">119. Pascal's Triangle II</a></h2><h3>Easy</h3><hr><p>Given an integer <code>rowIndex</code>, return the <code>rowIndex<sup>th</sup></code> (<strong>0-indexed</strong>) row of the <strong>Pascal&#39;s triangle</strong>.</p>

<p>In <strong>Pascal&#39;s triangle</strong>, each number is the sum of the two numbers directly above it as shown:</p>
<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height:240px; width:260px" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> rowIndex = 3
<strong>Output:</strong> [1,3,3,1]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> rowIndex = 0
<strong>Output:</strong> [1]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> rowIndex = 1
<strong>Output:</strong> [1,1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= rowIndex &lt;= 33</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you optimize your algorithm to use only <code>O(rowIndex)</code> extra space?</p>

### SOLUTION 
1. Optimal solution
```python
def triangle(index):
    res = [1]

    for i in range(index):
        print(i)
        next_row = [0] * (len(res) + 1)
        print(next_row)
        print(res)
        for j in range(len(res)):
            next_row[j] += res[j]
            print(next_row)
            next_row[j + 1] += res[j]
            print(next_row)
        
        res = next_row
    
    return res
```

2. My solution
```python
def getRow(self, index: int) -> List[int]:
        result = [[1],]
        for row in range(index):
            temp = [0] + result[-1] + [0]
            currentRow = []
            for j in range(len(result[-1])+1):
                currentRow.append(temp[j] + temp[j+1])
            result.append(currentRow)
        return result[index]
```

3. My improved solution
   * Your code builds all rows of Pascal’s Triangle up to the given index, even though only the row at index is required. This wastes both time and memory.
   * You use an additional temporary list (temp = [0] + result[-1] + [0]) for each row, which increases memory usage unnecessarily.
   * The result list stores all rows of the triangle, but only the current and previous rows are needed to compute the desired row.
```python
row = [1]  # Start with the first row
for i in range(1, index + 1):
# Update the row in reverse to avoid overwriting values
	row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1]
return row
```
