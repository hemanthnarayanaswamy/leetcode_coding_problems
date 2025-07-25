<h2><a href="https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition">3685. Count Subarrays of Length Three With a Condition</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code>, return the number of <span data-keyword="subarray-nonempty">subarrays</span> of length 3 such that the sum of the first and third numbers equals <em>exactly</em> half of the second number.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,1,4,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>Only the subarray <code>[1,4,1]</code> contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p><code>[1,1,1]</code> is the only subarray of length 3. However, its first and third numbers do not add to half the middle number.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 100</code></li>
	<li><code><font face="monospace">-100 &lt;= nums[i] &lt;= 100</font></code></li>
</ul>

# Solution 
* Approach is simple but with alot of edge cases to solve. 
* Use the sliding window to check all triplets. 

1. sum of first and last should be exactly exactly equal to half of second element. 
2. Exactly means no roundoff nothing including the decimal values it should be equal for to avoid that check `2(x+z) == y` instead to avoid using float. 

```python
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            x,y,z = nums[i], nums[i+1], nums[i+2]

            if 2 * (x + z) == y:
                count += 1
        
        return count
```
This checks if the middle element is the average of the first and third (i.e., y == (x + z) / 2). Using integer arithmetic avoids floating-point issues.

```python
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-2):
            a=nums[i]
            b=nums[i+1]
            c=nums[i+2]
            if b%2==0 and a+c==b//2:
                count+=1
        return count
```

