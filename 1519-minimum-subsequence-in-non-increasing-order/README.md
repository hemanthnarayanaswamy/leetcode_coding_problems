<h2><a href="https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order">1519. Minimum Subsequence in Non-Increasing Order</a></h2><h3>Easy</h3><hr><p>Given the array <code>nums</code>, obtain a subsequence of the array whose sum of elements is <strong>strictly greater</strong> than the sum of the non&nbsp;included elements in such subsequence.&nbsp;</p>

<p>If there are multiple solutions, return the subsequence with <strong>minimum size</strong> and if there still exist multiple solutions, return the subsequence with the <strong>maximum total sum</strong> of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.&nbsp;</p>

<p>Note that the solution with the given constraints is guaranteed to be&nbsp;<strong>unique</strong>. Also return the answer sorted in <strong>non-increasing</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,3,10,9,8]
<strong>Output:</strong> [10,9] 
<strong>Explanation:</strong> The subsequences [10,9] and [10,8] are minimal such that the sum of their elements is strictly greater than the sum of elements not included. However, the subsequence [10,9] has the maximum total sum of its elements.&nbsp;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,4,7,6,7]
<strong>Output:</strong> [7,7,6] 
<strong>Explanation:</strong> The subsequence [7,7] has the sum of its elements equal to 14 which is not strictly greater than the sum of elements not included (14 = 4 + 4 + 6). Therefore, the subsequence [7,6,7] is the minimal satisfying the conditions. Note the subsequence has to be returned in non-increasing order.  
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>

# Solution 
```python
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        totalsum = sum(nums)
        nums.sort(reverse=True)
        res = []
        tmp = 0

        for n in nums:
            tmp += n 
            if tmp <= totalsum - n:
                res.append(n)
                totalsum -= n
            else:
                res.append(n)
                return res
        
        return res
```

```python
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)

        for i in range(len(nums)):
            if sum(nums[:i+1]) > sum(nums[i+1:]):
                return nums[:i+1]
```

# Improved Solution 
```python
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        totalSum = sum(nums)
        currentSum = 0

        for i in range(len(nums)):
            if currentSum > totalSum:
                return nums[:i]
            else:
                totalSum -= nums[i]
                currentSum += nums[i]
        
        return nums
```

```python
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)

        subseq = []
        subseq_sum = 0

        for x in nums:
            subseq_sum += x      
            total -= x         
            subseq.append(x)

            if subseq_sum > total:
                break

        return subseq
```

# Optimal Solution
```python
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        totalSum, curr, res, p = sum(nums), 0, [], -1
        while curr <= totalSum:
            res += [nums[p]]
            curr += nums[p]
            totalSum -= nums[p]
            p -= 1
        return res
```
