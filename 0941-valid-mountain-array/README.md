<h2><a href="https://leetcode.com/problems/valid-mountain-array">978. Valid Mountain Array</a></h2><h3>Easy</h3><hr><p>Given an array of integers <code>arr</code>, return <em><code>true</code> if and only if it is a valid mountain array</em>.</p>

<p>Recall that arr is a mountain array if and only if:</p>

<ul>
	<li><code>arr.length &gt;= 3</code></li>
	<li>There exists some <code>i</code> with <code>0 &lt; i &lt; arr.length - 1</code> such that:
	<ul>
		<li><code>arr[0] &lt; arr[1] &lt; ... &lt; arr[i - 1] &lt; arr[i] </code></li>
		<li><code>arr[i] &gt; arr[i + 1] &gt; ... &gt; arr[arr.length - 1]</code></li>
	</ul>
	</li>
</ul>
<img src="https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png" width="500" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> arr = [2,1]
<strong>Output:</strong> false
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> arr = [3,5,5]
<strong>Output:</strong> false
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> arr = [0,3,2,1]
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
</ul>

# Solution 
* Edge cases to handle is if the array only has `upward` or `downward`, code will fail so we need to check the `sorting` result.

```python
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        mountainPeak = False
        n = len(arr)
        sortedArr = sorted(arr)

        if n < 3:             # If lenght is < 3 return False
            return False
        elif sortedArr == arr or sortedArr == arr[::-1]:   # If array has only upward or downward range then return False
            return False

        for i in range(n - 1):
            if arr[i] > arr[i+1]: # When the formate breaks we found the peak of the mountain
                mountainPeak = True 

            if not mountainPeak and arr[i] >= arr[i+1]: # when the peak is not found and the prefix is upwards then return
                return False
            elif mountainPeak and arr[i] <= arr[i+1]: # is the 
                return False
        
        return True
```
---
# Optimal Solution 
```python
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        peak = arr.index(max(arr))

        # Peak cannot be at edges
        if peak == 0 or peak == n - 1:
            return False

        # Check strictly increasing
        for i in range(peak):
            if arr[i] >= arr[i + 1]:
                return False

        # Check strictly decreasing
        for i in range(peak, n - 1):
            if arr[i] <= arr[i + 1]:
                return False

        return True
```
---
```python
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        Increasing = True

        for i in range(1, len(arr)):
            if arr[i] > arr[i-1] and Increasing:
                continue
            elif arr[i] < arr[i-1] and i > 1:
                Increasing = False
            else:
                return False
        return True and not Increasing
```
