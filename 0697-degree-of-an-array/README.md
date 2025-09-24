<h2><a href="https://leetcode.com/problems/degree-of-an-array">697. Degree of an Array</a></h2><h3>Easy</h3><hr><p>Given a non-empty array of non-negative integers <code>nums</code>, the <b>degree</b> of this array is defined as the maximum frequency of any one of its elements.</p>

<p>Your task is to find the smallest possible length of a (contiguous) subarray of <code>nums</code>, that has the same degree as <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,2,3,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,2,3,1,4,2]
<strong>Output:</strong> 6
<strong>Explanation:</strong> 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums.length</code> will be between 1 and 50,000.</li>
	<li><code>nums[i]</code> will be an integer between 0 and 49,999.</li>
</ul>

# Solution 
An array that has degree `d`, must have some element `x` occur `d` times. If some subarray has the same degree, then some element `x` (that occurred `d` times), still occurs `d` times. The shortest such subarray would be from the first occurrence of `x` until the last occurrence.

* For each element in the given array, let's know `left`, **the index of its first occurrence**; and `right`, the** index of its last occurrence**. For example, with `nums = [1,2,3,2,5]` we have `left[2] = 1` and `right[2] = 3`.

* Then, for each element x that occurs the maximum number of times, `right[x] - left[x] + 1` will be our candidate answer, and we'll take the minimum of those candidates.

```python
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}

        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            
            right[num] = i
            count[num] = count.get(num, 0) + 1
        
        degree = max(count.values())
        ans = len(nums)

        for x, d in count.items():
            if d == degree:
                ans = min(ans, right[x] - left[x] + 1)
        
        return ans
```
