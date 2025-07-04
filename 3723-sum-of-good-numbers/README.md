<h2><a href="https://leetcode.com/problems/sum-of-good-numbers">3723. Sum of Good Numbers</a></h2><h3>Easy</h3><hr><p>Given an array of integers <code>nums</code> and an integer <code>k</code>, an element <code>nums[i]</code> is considered <strong>good</strong> if it is <strong>strictly</strong> greater than the elements at indices <code>i - k</code> and <code>i + k</code> (if those indices exist). If neither of these indices <em>exists</em>, <code>nums[i]</code> is still considered <strong>good</strong>.</p>

<p>Return the <strong>sum</strong> of all the <strong>good</strong> elements in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3,2,1,5,4], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<p>The good numbers are <code>nums[1] = 3</code>, <code>nums[4] = 5</code>, and <code>nums[5] = 4</code> because they are strictly greater than the numbers at indices <code>i - k</code> and <code>i + k</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,1], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The only good number is <code>nums[0] = 2</code> because it is strictly greater than <code>nums[1]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= floor(nums.length / 2)</code></li>
</ul>


# Brute Force Solution 
```python
class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        res = 0

        for i in range(len(nums)):
            p = i - k
            n = i + k

            if p > -1 and n < len(nums):
                if nums[i] > nums[p] and nums[i] > nums[n]:
                    res += nums[i]
            elif p < 0 and n < len(nums):
                if nums[i] > nums[n]:
                    res += nums[i]
            elif p > -1 and n >= len(nums):
                if nums[i] > nums[p]:
                    res += nums[i]
            else:
                res += nums[i]

        return res   
```

# Improved Solution 
```python
class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total = 0
        NEG_INF = float('-inf')
        
        for i, v in enumerate(nums):
            left  = nums[i-k] if i - k >= 0   else NEG_INF
            right = nums[i+k] if i + k < n    else NEG_INF
            
            if v > left and v > right:
                total += v
        
        return total
```
