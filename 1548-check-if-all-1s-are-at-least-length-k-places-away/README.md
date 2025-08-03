<h2><a href="https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/?envType=problem-list-v2&envId=n9iuhemc">1548. Check If All 1's Are at Least Length K Places Away</a></h2><h3>Easy</h3><hr><p>Given an binary array <code>nums</code> and an integer <code>k</code>, return <code>true</code><em> if all </em><code>1</code><em>&#39;s are at least </em><code>k</code><em> places away from each other, otherwise return </em><code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/15/sample_1_1791.png" style="width: 428px; height: 181px;" />
<pre>
<strong>Input:</strong> nums = [1,0,0,0,1,0,0,1], k = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> Each of the 1s are at least 2 places away from each other.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/15/sample_2_1791.png" style="width: 320px; height: 173px;" />
<pre>
<strong>Input:</strong> nums = [1,0,0,1,0,1], k = 2
<strong>Output:</strong> false
<strong>Explanation:</strong> The second 1 and third 1 are only one apart from each other.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= nums.length</code></li>
	<li><code>nums[i]</code> is <code>0</code> or <code>1</code></li>
</ul>

# Solution 
```python
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        tmp = []

        for i, v in enumerate(nums):
            if v == 1:
                tmp.append(i)
        
        for j in range(1, len(tmp)):
            if tmp[j] - tmp[j-1] - 1 < k:
                return False
        
        return True
```

```python
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pre = -k - 1    

        for i, v in enumerate(nums):
            if v == 1:
                if i - pre - 1 < k:
                    return False 
                pre = i
        
        return True
```

# Optimal Solution
```python
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k
        for n in nums:
            if n == 1:
                if count < k:
                    return False
                count = 0
            else:
                count += 1
        
        return True
```
