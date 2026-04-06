<h2><a href="https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i">3773. Minimum Pair Removal to Sort Array I</a></h2><h3>Easy</h3><hr><p>Given an array <code>nums</code>, you can perform the following operation any number of times:</p>

<ul>
	<li>Select the <strong>adjacent</strong> pair with the <strong>minimum</strong> sum in <code>nums</code>. If multiple such pairs exist, choose the leftmost one.</li>
	<li>Replace the pair with their sum.</li>
</ul>

<p>Return the <strong>minimum number of operations</strong> needed to make the array <strong>non-decreasing</strong>.</p>

<p>An array is said to be <strong>non-decreasing</strong> if each element is greater than or equal to its previous element (if it exists).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,2,3,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The pair <code>(3,1)</code> has the minimum sum of 4. After replacement, <code>nums = [5,2,4]</code>.</li>
	<li>The pair <code>(2,4)</code> has the minimum sum of 6. After replacement, <code>nums = [5,6]</code>.</li>
</ul>

<p>The array <code>nums</code> became non-decreasing in two operations.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The array <code>nums</code> is already sorted.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

# Solution 
* Follow the proceduce until the array becomes sorted.

```python
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        moves = 0

        if len(nums) < 2:
            return moves

        def check_sorted(nums):
            return nums == sorted(nums)
        
        def replacePair(nums, i1, i2):
            new = nums[:i1] + [sum(nums[i1:i2+1])] + nums[i2+1:]
            return new
        
        while not check_sorted(nums):
            minSum = float('inf')
            i1 = i2 = None

            for i in range(1, len(nums)):
                p, c = nums[i-1], nums[i]
                tmp = p+c
                if tmp < minSum:
                    minSum = tmp
                    i1 = i-1
                    i2 = i

            nums = replacePair(nums, i1, i2)
            moves += 1
        
        return moves
```
* No need to `sort()` each time instead check for `nums[i] < nums[i-1]`
* Instead of recalculating and reconstructing the `nums` array, sort the index and replace that index with the minSum and `pop()` and second index.

```python
	nums[idx] = min_sum
	nums.pop(idx + 1)
	operations += 1
```
---

```python
class Solution:
    def minimumPairRemoval(self, nums):
        def is_sorted(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1]:
                    return False
            return True

        operations = 0

        while not is_sorted(nums):
            min_sum = nums[0] + nums[1]
            idx = 0

            # Find leftmost adjacent pair with minimum sum
            for i in range(1, len(nums) - 1):
                curr_sum = nums[i] + nums[i + 1]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    idx = i

            # Merge the pair
            nums[idx] = min_sum
            nums.pop(idx + 1)
            operations += 1

        return operations
```
