<h2><a href="https://leetcode.com/problems/count-good-triplets/?envType=problem-list-v2&envId=n9iuhemc">1656. Count Good Triplets</a></h2><h3>Easy</h3><hr><p>Given an array of integers <code>arr</code>, and three integers&nbsp;<code>a</code>,&nbsp;<code>b</code>&nbsp;and&nbsp;<code>c</code>. You need to find the number of good triplets.</p>

<p>A triplet <code>(arr[i], arr[j], arr[k])</code>&nbsp;is <strong>good</strong> if the following conditions are true:</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt; k &lt;&nbsp;arr.length</code></li>
	<li><code>|arr[i] - arr[j]| &lt;= a</code></li>
	<li><code>|arr[j] - arr[k]| &lt;= b</code></li>
	<li><code>|arr[i] - arr[k]| &lt;= c</code></li>
</ul>

<p>Where <code>|x|</code> denotes the absolute value of <code>x</code>.</p>

<p>Return<em> the number of good triplets</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong>&nbsp;There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,1,2,2,3], a = 0, b = 0, c = 1
<strong>Output:</strong> 0
<strong>Explanation: </strong>No triplet satisfies all conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= arr.length &lt;= 100</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 1000</code></li>
	<li><code>0 &lt;= a, b, c &lt;= 1000</code></li>

</ul>

# Solution 
```python
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        
        return count
```
---
```python
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0

        for i in range(n-2):
            ai = arr[i]
            for j in range(i+1, n-1):
                aj = arr[j]
                if abs(ai - aj) > a:
                    continue
                for k in range(j+1, n):
                    ak = arr[k]
                    diff_jk = abs(aj - ak)
                    
                    if diff_jk > b:
                        continue
                    if abs(ai - ak) <= c:
                        count += 1
        return count
```
---
```python
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        n = len(arr)
        
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                
                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1

        return count
```
