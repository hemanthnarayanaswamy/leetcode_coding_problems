<h2><a href="https://leetcode.com/problems/minimum-increment-to-make-array-unique">982. Minimum Increment to Make Array Unique</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code>. In one move, you can pick an index <code>i</code> where <code>0 &lt;= i &lt; nums.length</code> and increment <code>nums[i]</code> by <code>1</code>.</p>

<p>Return <em>the minimum number of moves to make every value in </em><code>nums</code><em> <strong>unique</strong></em>.</p>

<p>The test cases are generated so that the answer fits in a 32-bit integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> After 1 move, the array could be [1, 2, 3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,1,2,1,7]
<strong>Output:</strong> 6
<strong>Explanation:</strong> After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown that it is impossible for the array to have all unique values with 5 or less moves.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

# Solution 

1. Sort the array and think in direction to make array increasing
2. so whenever `nums[i] <= prev` make `nums[i] to prev + 1` and the moves required in this step will be `moves += (prev + 1 - nums[i])`
every time keep updating `prev = nums[i]`
3. Trying to make the array strictly increasing i.e maintain the sorted behavior of the array without duplicates 

```python
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        operations = 0
        nums = sorted(nums)  # Sorted the Array 

        for i in range(1,len(nums)):
            pre,cur = nums[i-1], nums[i]

            if cur <= pre:  # Trying to make the array strictly increasing i.e maintain the sorted behavior of the array without duplicates 
                nums[i] = pre + 1
                operations += pre + 1 - cur
        
        return operations
```
