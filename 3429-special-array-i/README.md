<h2><a href="https://leetcode.com/problems/special-array-i">3429. Special Array I</a></h2><h3>Easy</h3><hr><p>An array is considered <strong>special</strong> if the <em>parity</em> of every pair of adjacent elements is different. In other words, one element in each pair <strong>must</strong> be even, and the other <strong>must</strong> be odd.</p>

<p>You are given an array of integers <code>nums</code>. Return <code>true</code> if <code>nums</code> is a <strong>special</strong> array, otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>There is only one element. So the answer is <code>true</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,1,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>There is only two pairs: <code>(2,1)</code> and <code>(1,4)</code>, and both of them contain numbers with different parity. So the answer is <code>true</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,3,1,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p><code>nums[1]</code> and <code>nums[2]</code> are both odd. So the answer is <code>false</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>

# Solution 
```python
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] % 2 == 0:
                if nums[i-1] % 2 == 0:
                    return False
            else:
                if nums[i-1] % 2 == 1:
                    return False
        
        return True
```

* Can be improved by changine and improving the if condition more optimally 

# Improved solution

```python
class Solution:
    def isArraySpecial(self, nums):
        # Iterate through indexes 0 to n - 1
        for index in range(len(nums) - 1):

            # Compare the parities of the current and next number
            if nums[index] % 2 == nums[index + 1] % 2:

                # If the two adjacent numbers have the same parity, return False
                return False

        # Return True if no pair of adjacent numbers with the same parity are found
        return True
```
