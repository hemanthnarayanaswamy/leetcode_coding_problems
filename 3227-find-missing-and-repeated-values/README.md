<h2><a href="https://leetcode.com/problems/find-missing-and-repeated-values">3227. Find Missing and Repeated Values</a></h2><h3>Easy</h3><hr><p>You are given a <strong>0-indexed</strong> 2D integer matrix <code><font face="monospace">grid</font></code> of size <code>n * n</code> with values in the range <code>[1, n<sup>2</sup>]</code>. Each integer appears <strong>exactly once</strong> except <code>a</code> which appears <strong>twice</strong> and <code>b</code> which is <strong>missing</strong>. The task is to find the repeating and missing numbers <code>a</code> and <code>b</code>.</p>

<p>Return <em>a <strong>0-indexed </strong>integer array </em><code>ans</code><em> of size </em><code>2</code><em> where </em><code>ans[0]</code><em> equals to </em><code>a</code><em> and </em><code>ans[1]</code><em> equals to </em><code>b</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,3],[2,2]]
<strong>Output:</strong> [2,4]
<strong>Explanation:</strong> Number 2 is repeated and number 4 is missing so the answer is [2,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[9,1,7],[8,9,2],[3,4,6]]
<strong>Output:</strong> [9,5]
<strong>Explanation:</strong> Number 9 is repeated and number 5 is missing so the answer is [9,5].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n == grid.length == grid[i].length &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= n * n</code></li>
	<li>For all <code>x</code> that <code>1 &lt;= x &lt;= n * n</code> there is exactly one <code>x</code> that is not equal to any of the grid members.</li>
	<li>For all <code>x</code> that <code>1 &lt;= x &lt;= n * n</code> there is exactly one <code>x</code> that is equal to exactly two of the grid members.</li>
	<li>For all <code>x</code> that <code>1 &lt;= x &lt;= n * n</code> except two of them there is exactly one pair of <code>i, j</code> that <code>0 &lt;= i, j &lt;= n - 1</code> and <code>grid[i][j] == x</code>.</li>
</ul>

# Solution 
* Use HashMap to store the numbers and its Frequency. 
* If the frequency if 2 then its the repeated number. 
* Check numbers from range (1, n*n) to see the any number is missing then that is the missing number 

```python
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        numsFreq = {}
        n = len(grid)
        total = n * n

        for nums in grid:
            for num in nums:
                numsFreq[num] = numsFreq.get(num, 0) + 1
        
        for num, fq in numsFreq.items():
            if fq == 2:
                repeated_num = num 
        
        for num in range(1, total+1):
            if num not in numsFreq:
                missing_num = num 
        
        return [repeated_num, missing_num]
```

# Optimal Solution 
```python
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        freq = {}

        # Store frequency of each number in the grid
        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1

        # Check numbers from 1 to n^2 to find missing and repeated values
        for num in range(1, n * n + 1):
            if num not in freq:
                missing = num  # Number not present in grid
            elif freq[num] == 2:
                repeat = num  # Number appears twice

        return [repeat, missing]
```
* Using the Array instead of the HashMaps
```python
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        freq=[0]*(n*n+1)
        for row in grid:
            for val in row:
                freq[val]+=1
        repeated=missing=-1
        for val in range(1,n*n+1):
            if freq[val]==0:
                missing=val
            elif freq[val]==2:
                repeated=val
        return [repeated,missing]
```
