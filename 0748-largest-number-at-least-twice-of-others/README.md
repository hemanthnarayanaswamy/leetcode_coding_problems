<h2><a href="https://leetcode.com/problems/largest-number-at-least-twice-of-others">748. Largest Number At Least Twice of Others</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code> where the largest integer is <strong>unique</strong>.</p>

<p>Determine whether the largest element in the array is <strong>at least twice</strong> as much as every other number in the array. If it is, return <em>the <strong>index</strong> of the largest element, or return </em><code>-1</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,6,1,0]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> -1
<strong>Explanation:</strong> 4 is less than twice the value of 3, so we return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 50</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
	<li>The largest element in <code>nums</code> is unique.</li>
</ul>

# Solution
* As the maximum number is unqiue so initially find the max number and the index of the maximum number. 
* Then iterate to check if the twice of that number is greater then the maximum number then immediately return `-1`
* or after the loop return the stored index.

```python
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNum = max(nums)
        idx = nums.index(maxNum)

        for num in nums:
            if num != maxNum and num*2 > maxNum:
                return -1
        
        return idx
```

## Optimal Solution
* we don't need to check each and every number we only need to check the max and next max

```python
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        numSort = sorted(nums)

        if numSort[-1] >= 2*numSort[-2]:
            return nums.index(numSort[-1])
        else:
            return -1
```
