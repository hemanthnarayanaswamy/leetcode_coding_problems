<h2><a href="https://leetcode.com/problems/maximum-average-subarray-i">643. Maximum Average Subarray I</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code> consisting of <code>n</code> elements, and an integer <code>k</code>.</p>

<p>Find a contiguous subarray whose <strong>length is equal to</strong> <code>k</code> that has the maximum average value and return <em>this value</em>. Any answer with a calculation error less than <code>10<sup>-5</sup></code> will be accepted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,12,-5,-6,50,3], k = 4
<strong>Output:</strong> 12.75000
<strong>Explanation:</strong> Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5], k = 1
<strong>Output:</strong> 5.00000
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## Solution Approach 
* Calculate the initial sum of the window and the result 
* Than iterate by remove the previous value and adding the next element that is by moving the window ( sliding window).
```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = float('-inf')
        n = len(nums)
        if n <= k:
            result = sum(nums) / k
        else:
            initial_sum = sum(nums[0:k])
            result = initial_sum / k
        
        for i in range(1, n):
            if i+k-1 < n:
                initial_sum = initial_sum - nums[i-1] + nums[i+k-1]
                result = max(initial_sum / k, result)
        return result
```
### Issues with above solution 
* If `n == k`, the sliding window logic still works correctly.
* you're manually computing the first sum `(sum(nums[0:k]))` and then looping from `i = 1`
* Unnecessary Comparisons & Conditions `(if i + k - 1 < n)`

## optimal Solution
```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])        # Compute the sum of the first window
        max_sum = current_sum              # Initialize max_sum with the first window sum

        # Slide the window from index 1 to n-k
        for i in range(k, len(nums)):                      # We have already calcluated the sum till K 
            current_sum += nums[i] - nums[i - k]  # Remove leftmost element, add new element
            max_sum = max(max_sum, current_sum)  # Update max_sum if the new sum is larger

        return max_sum / k  # Compute and return the maximum average
```
