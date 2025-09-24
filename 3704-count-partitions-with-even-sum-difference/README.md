<h2><a href="https://leetcode.com/problems/count-partitions-with-even-sum-difference">3704. Count Partitions with Even Sum Difference</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code> of length <code>n</code>.</p>

<p>A <strong>partition</strong> is defined as an index <code>i</code> where <code>0 &lt;= i &lt; n - 1</code>, splitting the array into two <strong>non-empty</strong> subarrays such that:</p>

<ul>
	<li>Left subarray contains indices <code>[0, i]</code>.</li>
	<li>Right subarray contains indices <code>[i + 1, n - 1]</code>.</li>
</ul>

<p>Return the number of <strong>partitions</strong> where the <strong>difference</strong> between the <strong>sum</strong> of the left and right subarrays is <strong>even</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [10,10,3,7,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The 4 partitions are:</p>

<ul>
	<li><code>[10]</code>, <code>[10, 3, 7, 6]</code> with a sum difference of <code>10 - 26 = -16</code>, which is even.</li>
	<li><code>[10, 10]</code>, <code>[3, 7, 6]</code> with a sum difference of <code>20 - 16 = 4</code>, which is even.</li>
	<li><code>[10, 10, 3]</code>, <code>[7, 6]</code> with a sum difference of <code>23 - 13 = 10</code>, which is even.</li>
	<li><code>[10, 10, 3, 7]</code>, <code>[6]</code> with a sum difference of <code>30 - 6 = 24</code>, which is even.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>No partition results in an even sum difference.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,4,6,8]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>All partitions result in an even sum difference.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n == nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>

# Solution 
* No complication use prefix sum to track the right and left sums and 
* Before finding the difference make sure both sums are not zero 

```python
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        rightSum = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum -= nums[i]
            leftSum += nums[i]
        
            if leftSum and rightSum and (leftSum - rightSum) % 2 == 0:
                count += 1
        
        return count
```
---
# Optimal Solution 
* what we need to calculate after split the array is the difference between the sum of the left and right subarrays
```
diff = left_sum - right_sum
right_sum = total - left_sum
```
```
diff = left_sum - (total - left_sum)
diff = 2 * left_sum - total
```
* To check if diff is even, calculate diff % 2.
Since `diff = 2 * left_sum - total` , we can write: `(2 * left_sum - total) % 2`.
Using **modular arithmetic, the term `(2 * left_sum) % 2` equals 0 because any number multiplied by 2 is always even. Thus, the expression simplifies to: `− total % 2`, this further simplifies to:`total % 2`.**

what is it mean if total is even?
**It means you can cut the each valid position in the array, so the number of partitions is n - 1.**

```python
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        if sum(nums)%2==0:
            return len(nums)-1
        else:
            return 0        
```
