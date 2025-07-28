<h2><a href="https://leetcode.com/problems/minimum-operations-to-collect-elements">3044. Minimum Operations to Collect Elements</a></h2><h3>Easy</h3><hr><p>You are given an array <code>nums</code> of positive integers and an integer <code>k</code>.</p>

<p>In one operation, you can remove the last element of the array and add it to your collection.</p>

<p>Return <em>the <strong>minimum number of operations</strong> needed to collect elements</em> <code>1, 2, ..., k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,5,4,2], k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> After 4 operations, we collect elements 2, 4, 5, and 1, in this order. Our collection contains elements 1 and 2. Hence, the answer is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,5,4,2], k = 5
<strong>Output:</strong> 5
<strong>Explanation:</strong> After 5 operations, we collect elements 2, 4, 5, 1, and 3, in this order. Our collection contains elements 1 through 5. Hence, the answer is 5.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,5,3,1], k = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> After 4 operations, we collect elements 1, 3, 5, and 2, in this order. Our collection contains elements 1 through 3. Hence, the answer is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= nums.length</code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
	<li>The input is generated such that you can collect elements <code>1, 2, ..., k</code>.</li>
</ul>

# Solution
* You're finding the earliest position where all numbers 1 to k appear, then calculating operations from the end.

```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        numsMap = {nu: i for i, nu in enumerate(nums)}
        idx = []

        for i in range(1, k+1):
            idx.append(numsMap[i])
        
        return len(nums) - min(idx)
 ```

# Optimal Solution 
```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s1 = set()
        s2 = set()
        for i in range(1, k+1):
            s1.add(i)
        n = len(nums)-1
        r = 0
        while (s1 != s2 and n>-1):
            if nums[n] in s1:
                s2.add(nums[n])
            r += 1
            n -= 1
        return r
```

```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        collected = set()
        
        for i in range(len(nums) - 1, -1, -1):
            operations += 1
            
            # If we found one of our target numbers
            if 1 <= nums[i] <= k:
                collected.add(nums[i])
            
            # Check if we have collected all numbers from 1 to k
            if len(collected) == k:
                return operations
```
