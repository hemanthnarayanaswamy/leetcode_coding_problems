<h2><a href="https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array">1221. Element Appearing More Than 25% In Sorted Array</a></h2><h3>Easy</h3><hr><p>Given an integer array <strong>sorted</strong> in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,2,6,6,6,6,7,10]
<strong>Output:</strong> 6
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
</ul>

# Solution 
* Use HashMap and see if the values count is more then the 0.25 of the lenght of the array.

```python
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        maxLen = 0.25 * len(arr)

        arrFreq = Counter(arr)

        for num, count in arrFreq.items():
            if count > maxLen:
                return num 
```

# Optimal Solution
```python
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        threshold = n // 4

        count = 1
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                count += 1
                if count > threshold:
                    return arr[i]
            else:
                count = 1
        
        return arr[0]
```

```python 
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr) // 4
        for i in range(len(arr) - size):
            if arr[i] == arr[i + size]:
                return arr[i]
```
