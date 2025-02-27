<h2><a href="https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array">1787. Sum of Absolute Differences in a Sorted Array</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code> sorted in <strong>non-decreasing</strong> order.</p>

<p>Build and return <em>an integer array </em><code>result</code><em> with the same length as </em><code>nums</code><em> such that </em><code>result[i]</code><em> is equal to the <strong>summation of absolute differences</strong> between </em><code>nums[i]</code><em> and all the other elements in the array.</em></p>

<p>In other words, <code>result[i]</code> is equal to <code>sum(|nums[i]-nums[j]|)</code> where <code>0 &lt;= j &lt; nums.length</code> and <code>j != i</code> (<strong>0-indexed</strong>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,5]
<strong>Output:</strong> [4,3,5]
<strong>Explanation:</strong> Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,4,6,8,10]
<strong>Output:</strong> [24,15,13,15,21]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= nums[i + 1] &lt;= 10<sup>4</sup></code></li>
</ul>

## Solution Approach 
* Its a bit of a complex approach to explain, but we need to use left and right prefix sum approach and note the array is sorted 
```
[1,4,6,8,10]
- Left Prefix Sum is 0 and Right Prefix sum is Sum(nums)
1st Iteration  --> First Iteration i=0 and left sum = 0 and right sum = 29 
   --> result[0] = abs(num*i - left_sum) + abs(num*([len(nums)-i] - right_sum)
	       result[0] = abs(1*0 - 0) + abs(1*5 - 29) = 24
	--> Left_sum += num === 1
	--> Right_sum -= num === 28
	
2nd Iteration --> num= 4, i = 1, left_sum= 1, right_sum = 28 
  --> result[1] = abs(4*1 - 1) + abs(4*4 - 28) == 3 + 12 == 15 
	--> left_sum = 4
	--> right_sum = 24 
```
* We cannot do `i - sum(nums)` because some number are greater than i and some number are not that way its hard to predict 
* Thats why we calculate the 2 different values for numbers sum where num is greater than those numbers and num is less than those numbers 
* Multiple by `i` and  `len(nums)-i` it is to calculate number of times num needed to compute the difference. 

```python
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_sum, right_sum = 0, sum(nums)
        n = len(nums)
        result = [0] * n
        
        for i in range(len(nums)):
            result[i] = abs(nums[i]*i - left_sum) + abs(nums[i]*n - right_sum)
            n -= 1
            left_sum += nums[i]
            right_sum -= nums[i]
        return result
```

* To further improve the Solution we remove the `n -= 1` and use `(right_sum - nums[i] * (n - i - 1))`
* Than no need to alter the 

```python
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left_sum, right_sum = 0, sum(nums)
        n = len(nums)
        result = [0] * n
        
        for i in range(n):
            right_sum -= nums[i]
            result[i] = (nums[i]*i - left_sum) + (right_sum - nums[i] * (n-i-1))
            left_sum += nums[i]
            
        return result
```
