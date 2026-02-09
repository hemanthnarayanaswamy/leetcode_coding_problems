<h2><a href="https://leetcode.com/problems/max-pair-sum-in-an-array">2902. Max Pair Sum in an Array</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code>. You have to find the <strong>maximum</strong> sum of a pair of numbers from <code>nums</code> such that the <strong>largest digit </strong>in both numbers is equal.</p>

<p>For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among them.</p>

<p>Return the <strong>maximum</strong> sum or -1 if no such pair exists.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [112,131,411]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>Each numbers largest digit in order is [2,3,4].</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2536,1613,3366,162]</span></p>

<p><strong>Output:</strong> <span class="example-io">5902</span></p>

<p><strong>Explanation:</strong></p>

<p>All the numbers have 6 as their largest digit, so the answer is <span class="example-io">2536 + 3366 = 5902.</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [51,71,17,24,42]</span></p>

<p><strong>Output:</strong> <span class="example-io">88</span></p>

<p><strong>Explanation:</strong></p>

<p>Each number&#39;s largest digit in order is [5,7,7,4,4].</p>

<p>So we have only two possible pairs, 71 + 17 = 88 and 24 + 42 = 66.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

# Approach
1. Create a `defaultdict(list)` to store the maximum digit and the list will contains its associated numbers in them. 
2. Now Iterate that `defaultdict` and find the list with `lenght > 2`, sort that and store the `sum of first 2 numbers` and iterate thought other lists with length > 2 and store to check which one is maximum sum and return the sum.

```python
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        numsMap = defaultdict(list)
        res = -1

        def maxDigit(num):
            d = 0
            while num:
                q, r = divmod(num, 10)
                d = max(d, r)
                num = q
            return d
        
        for num in nums:
            d = maxDigit(num)
            numsMap[d].append(num)
        
        for _, numList in numsMap.items():
            if len(numList) >= 2:
                numList.sort()
                res = max(res, sum(numList[-2:]))
        
        return res
```
---
# Improved Version

```python
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_by_digit = defaultdict(int)
        max_sum = -1

        for num in nums:
            digit = max(str(num))

            if digit in max_by_digit:
                max_sum = max(max_sum, max_by_digit[digit] + num)

            max_by_digit[digit] = max(max_by_digit[digit], num)

        return max_sum
```
---
### NO SORT
```python
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_num_by_d = [0] * 10
        max_sum = -1

        for num in nums:
            key, temp = 0, num
            while temp > 0:
                key = max(key, temp % 10)
                temp //= 10
            if max_num_by_d[key]:
                max_sum = max(max_sum, num + max_num_by_d[key])
                max_num_by_d[key] = max(max_num_by_d[key], num)
            else:
                max_num_by_d[key] = num
        
        return max_sum
```
