<h2><a href="https://leetcode.com/problems/pascals-triangle">118. Pascal's Triangle</a></h2><h3>Easy</h3><hr><p>Given an integer <code>numRows</code>, return the first numRows of <strong>Pascal&#39;s triangle</strong>.</p>

<p>In <strong>Pascal&#39;s triangle</strong>, each number is the sum of the two numbers directly above it as shown:</p>
<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height:240px; width:260px" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> numRows = 5
<strong>Output:</strong> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> numRows = 1
<strong>Output:</strong> [[1]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numRows &lt;= 30</code></li>
</ul>

## Solution 
1. The approach is simple first we declare the result along with the first element as `[1]`
```python
result = [[1],]
```
2. Next we have already filled 1 row, we need to fill the remaining `n-1` rows, and do a for loop that runs `n-1` times
```python
for row in range(n-1):
```
3. Next the main logic, we'll try to compute the whole row and then append that row to the results so to store the current row we need to variable list `row`
```python
arr = []
```
4. Now to compute the current row each element is the sum of the previous rows first element and its next element and so on. But for the first and last indexed number we need to puts zeros to compensate, Hence we create a temp variable.
```python
temp = [0] + result[-1] + [0] ## result[-1] we are accessing the previous rows to as reference
```
5. Now to compute the whole row first we need for loop to add elements according and the loop should run for length of previous row + 1
```python
for j in range(len(result[-1)+1):
```
6. For the each iteration of the row is sum of current temp element and the next temp element
```python
row.append(temp[j] + tem[j+1])
result.append(row) ## once the iteration of that row is complete add that row to the result
```
7. Here is the final solution
   ```python
   class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1],]

        for row in range(numRows-1): ## because we have already filled one row 
            temp = [0] + result[-1] + [0]
            row = []
            for i in range(len(result[-1]) + 1):
                row.append(temp[i]+ temp[i+1])
            result.append(row)
        return result
   ```
