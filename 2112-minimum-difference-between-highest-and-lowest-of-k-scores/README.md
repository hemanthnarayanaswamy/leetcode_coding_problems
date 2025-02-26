<h2><a href="https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores">2112. Minimum Difference Between Highest and Lowest of K Scores</a></h2><h3>Easy</h3><hr><p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>, where <code>nums[i]</code> represents the score of the <code>i<sup>th</sup></code> student. You are also given an integer <code>k</code>.</p>

<p>Pick the scores of any <code>k</code> students from the array so that the <strong>difference</strong> between the <strong>highest</strong> and the <strong>lowest</strong> of the <code>k</code> scores is <strong>minimized</strong>.</p>

<p>Return <em>the <strong>minimum</strong> possible difference</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [90], k = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is one way to pick score(s) of one student:
- [<strong><u>90</u></strong>]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [9,4,1,7], k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are six ways to pick score(s) of two students:
- [<strong><u>9</u></strong>,<strong><u>4</u></strong>,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [<strong><u>9</u></strong>,4,<strong><u>1</u></strong>,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [<strong><u>9</u></strong>,4,1,<strong><u>7</u></strong>]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,<strong><u>4</u></strong>,<strong><u>1</u></strong>,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,<strong><u>4</u></strong>,1,<strong><u>7</u></strong>]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,<strong><u>1</u></strong>,<strong><u>7</u></strong>]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

## Problem Statement 

To explain this better, which this description failed to do in my opinion. Let's assume we have the following array {20, 200,300, 1000 } and that k is 3
we would need to compare subarrays of size k and get the minimum value out of the subtraction between the lowest and highest number of that subarray.
- {20,200, 300} the difference between the highest (300) and lowest (20) number will be 280
- {200, 300, 1000} the difference between the highest (1000) and lowest (200) will be 800
- That's it there are not more subarrays of size K and so we compare 800 and 280 and the smallest difference is 280.


## Solution Approach 
* The approach is to find the minimum different in the subarray of size k. 
* Sort the array and calculate the minimum ass a sliding window 

```python
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0 
        
        nums = sorted(nums)
        min_result = nums[k-1] - nums[0]  ## Calculate the initial difference between max and min in the first sub array

        for i in range(k, len(nums)): ## We start the loop from the kth element 
            min_result = min(min_result, nums[i] - nums[i-k+1])
## Sliding window --->  nums[i] - nums[i-k+1] --> Keeping the window size same we are getting difference between max and min while moving
        return min_result
```



<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
