<h2><a href="https://leetcode.com/problems/max-consecutive-ones">485. Max Consecutive Ones</a></h2><h3>Easy</h3><hr><p>Given a binary array <code>nums</code>, return <em>the maximum number of consecutive </em><code>1</code><em>&#39;s in the array</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,0,1,1,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,0,1,1,0,1]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>

## Solution Appoach 
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum, max_sum = 1, 1 
        for num in nums:
            if sum*num: ## If zero is not detected than proceed 
                sum += num 
            else:
                sum = 1
            max_sum = max(sum, max_sum) ## Compute the MAx sum 
        return max_sum - 1
```

## Improved Solution 
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count, max_count = 0, 0
        for num in nums:
            if num == 1:
                current_count += 1  # Increment count for consecutive 1s
            else:
                max_count = max(max_count, current_count)  # Update max before resetting
                current_count = 0  # Reset counter on encountering 0

        return max(max_count, current_count)  # Final check for ending with 1s

```

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count, max_count = 0, 0
        for num in nums:
            if num == 1:
                current_count += 1  # Increment count for consecutive 1s
            else:
                if max_count < current_count:
                    max_count = current_count  # Update max before resetting
                current_count = 0  # Reset counter on encountering 0

        return max(max_count, current_count)  # Final check for ending with 1s
```
