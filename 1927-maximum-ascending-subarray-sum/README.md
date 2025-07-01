<h2><a href="https://leetcode.com/problems/maximum-ascending-subarray-sum">1927. Maximum Ascending Subarray Sum</a></h2><h3>Easy</h3><hr><p>Given an array of positive integers <code>nums</code>, return the <strong>maximum</strong> possible sum of an <span data-keyword="strictly-increasing-array">strictly increasing subarray</span> in<em> </em><code>nums</code>.</p>

<p>A subarray is defined as a contiguous sequence of numbers in an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,20,30,5,10,50]
<strong>Output:</strong> 65
<strong>Explanation: </strong>[5,10,50] is the ascending subarray with the maximum sum of 65.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,20,30,40,50]
<strong>Output:</strong> 150
<strong>Explanation: </strong>[10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [12,17,15,13,10,11,12]
<strong>Output:</strong> 33
<strong>Explanation: </strong>[10,11,12] is the ascending subarray with the maximum sum of 33.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>

# Solution 
* Store all the sums of the subarrays into a array 
* Have a variable to track all the subarray sums and append when the subarray condition is not meet and resetting the temp sum variable. 
* In the last iteration handle the last element.

```python
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSums = []
        tempSum = 0

        i = 0

        while i < len(nums) - 1:
            if nums[i] < nums[i+1]:
                tempSum += nums[i]
            else:
                tempSum += nums[i]
                maxSums.append(tempSum)
                tempSum = 0
            
            i += 1
        
        if tempSum:
            tempSum += nums[i]
            maxSums.append(tempSum)
        else:
            maxSums.append(nums[i])
        
        return max(maxSums)
```

# Improved Solution 
```python
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
            
            if curr_sum > max_sum:
                max_sum = curr_sum
        
        return max_sum
```
