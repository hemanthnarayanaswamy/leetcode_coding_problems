<h2><a href="https://leetcode.com/problems/number-of-arithmetic-triplets">2442. Number of Arithmetic Triplets</a></h2><h3>Easy</h3><hr><p>You are given a <strong>0-indexed</strong>, <strong>strictly increasing</strong> integer array <code>nums</code> and a positive integer <code>diff</code>. A triplet <code>(i, j, k)</code> is an <strong>arithmetic triplet</strong> if the following conditions are met:</p>

<ul>
	<li><code>i &lt; j &lt; k</code>,</li>
	<li><code>nums[j] - nums[i] == diff</code>, and</li>
	<li><code>nums[k] - nums[j] == diff</code>.</li>
</ul>

<p>Return <em>the number of unique <strong>arithmetic triplets</strong>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,4,6,7,10], diff = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong>
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,5,6,7,8,9], diff = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong>
(0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
(1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 200</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 200</code></li>
	<li><code>1 &lt;= diff &lt;= 50</code></li>
	<li><code>nums</code> is <strong>strictly</strong> increasing.</li>
</ul>

# Python 
```
j - i = d
i = j - d & j = d + i 

k - j = d
k - i - d = d 
i = k - 2d 

j = d + i
k = 2d + i
```
* The meaning of the above formula is for a number i if there exists are number `i+d` then that number is `num[j]` and if `i+2d` exists that number is `num[k]` which we can increase the count. 
* `diff` is always positive and the array is always increasing that means we don't need to worry about condition `i < j < k` since j and k values are obtained after adding associated d values. 

```python
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        numsU = set(nums)

        for num in nums:
            y = num + diff
            z = num + 2*diff 

            if y in numsU and z in numsU:
                count += 1
        
        return count
```
---
```python
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        num_set = set(nums)
        count = 0
        
        for x in nums:
            if (x + diff in num_set) and (x + 2 * diff in num_set):
                count += 1
        
        return count
```

