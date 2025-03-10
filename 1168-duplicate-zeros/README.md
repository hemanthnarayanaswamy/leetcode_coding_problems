<h2><a href="https://leetcode.com/problems/duplicate-zeros">1168. Duplicate Zeros</a></h2><h3>Easy</h3><hr><p>Given a fixed-length integer array <code>arr</code>, duplicate each occurrence of zero, shifting the remaining elements to the right.</p>

<p><strong>Note</strong> that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,0,2,3,0,4,5,0]
<strong>Output:</strong> [1,0,0,2,3,0,0,4]
<strong>Explanation:</strong> After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,3]
<strong>Output:</strong> [1,2,3]
<strong>Explanation:</strong> After calling your function, the input array is modified to: [1,2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 9</code></li>
</ul>


## Solution Approach 
* Whenever a 0 is detected
---> `pop()` the right most element 
---> Increment the left pointer 
---> Insert `0` at the incremented value

```python
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l, r = 0, len(arr)-1
        while l < r:
            if arr[l] == 0:
                arr.pop(r)   # pop the right most element 
                l += 1       # Increment the left pointer to place 0
                arr.insert(l, 0)
            l += 1           # Skip that element 
        
```
