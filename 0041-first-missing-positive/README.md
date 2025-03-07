<h2><a href="https://leetcode.com/problems/first-missing-positive">41. First Missing Positive</a></h2><h3>Hard</h3><hr><p>Given an unsorted integer array <code>nums</code>. Return the <em>smallest positive integer</em> that is <em>not present</em> in <code>nums</code>.</p>

<p>You must implement an algorithm that runs in <code>O(n)</code> time and uses <code>O(1)</code> auxiliary space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,0]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The numbers in the range [1,2] are all in the array.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,-1,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 1 is in the array but 2 is missing.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,8,9,11,12]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The smallest positive integer 1 is missing.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

## Solution Approach 
* The basic idea is that we have an array with n cells (n is the length of the array). If a positive integer is not in the given array it, the missing integer must be in the range `[1..n]`. This is the crucial observation we use to deduce the algorithm.
* So, If an integer is missing it must be in the range [1..n], if an integer is not missing then the answer is n+1


1. If there is no missing integers, this means that the array has all number from 1 to n. This must mean that the array is full. Why, because in the range [1..n] there are exactly n numbers, and if you place n numbers in an array of length n, the array is by definition full. (in this case the solution is to return n+1 which is the first smallest integer).
2. Once you understand the first case above understanding the second is easy. If there is a missing integer (or more than one), the missing integer(s), let's call it X, must be in the range 1..n. Why, because if the missing integer X is not in the range [1..n] that would imply that all integers [1..n] are in the array, which would mean that the array is full, leaving no space to place X (since X is not in the range [1..n]).
```
* Ignore all numbers <=0 and >n since they are outside the range of possible answers (which we proved was [1..n]). We do this by replacing them with the value n+1.
* For all other integers <n+1, mark their bucket (cell) to indicate the integer exists. (*see below)
* Find the first cell not marked, that is the first missing integer. If you did not find an unmarked cell, there was no missing integer, so return n+1.
```

## Solution 
* Used set to get unique elements from nums 
* Did a manual iteration Loop, to Compute the number between range `[1,n]`
* By returning the i if any detected else returning `n+1`
* But the Time Complexity: `O(n)`, Space: `O(n)` we want `O(1)` for Space.
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_unique = set(nums)
        for i in range(1,len(nums)+1):
            if i not in nums_unique:
                return i 
        return len(nums) + 1
```
## Optimal Solution 
* Initialize a variable n to the length of nums.
* Initialize an array seen to size n + 1.
* Mark the elements in nums as seen in the array seen.
* For each num in nums, if num is greater than 0 and less than or equal to n, set seen[num] to true.
---> Find the smallest missing positive number:
---> For i from 1 to n, If seen[i] is not true, return i, the smallest missing integer.
---> If seen contains all elements 1 to n, return n + 1 as the smallest missing positive number.

```python
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        seen = [False] * (n + 1)  # Array for lookup

        # Mark the elements from nums in the lookup array
        for num in nums:
            if 0 < num <= n:
                seen[num] = True

        # Iterate through integers 1 to n
        # return smallest missing positive integer
        for i in range(1, n + 1):
            if not seen[i]:
                return i

        # If seen contains all elements 1 to n
        # the smallest missing positive number is n + 1
        return n + 1
```
