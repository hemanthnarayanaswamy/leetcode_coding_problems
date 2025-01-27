<h2><a href="https://leetcode.com/problems/monotonic-array">932. Monotonic Array</a></h2><h3>Easy</h3><hr><p>An array is <strong>monotonic</strong> if it is either monotone increasing or monotone decreasing.</p>

<p>An array <code>nums</code> is monotone increasing if for all <code>i &lt;= j</code>, <code>nums[i] &lt;= nums[j]</code>. An array <code>nums</code> is monotone decreasing if for all <code>i &lt;= j</code>, <code>nums[i] &gt;= nums[j]</code>.</p>

<p>Given an integer array <code>nums</code>, return <code>true</code><em> if the given array is monotonic, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,2,3]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [6,5,4,4]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

## SOLUTION
1. In my solution I am using flags to check whether it is increasing or decreasing if both return False.
```python
   def monoarray(arr):
    is_decreasing, is_increasing = True, True
    array_len = len(arr)
    if array_len < 2:
        return True
    for i in range(array_len):
        if i+1 < array_len:
            current_ele, next_ele = arr[i], arr[i+1]
            if current_ele > next_ele:
                is_decreasing = False
            elif current_ele < next_ele:
                is_increasing = False
            elif current_ele == next_ele:
                is_decreasing, is_increasing = is_decreasing, is_increasing
        if not is_decreasing and not is_increasing:
            return False
    return True
```
2. Optiomal solution is using two functions
```python
def is_increasing(self, nums) -> bool:
        cur_num = nums[0]
        for num in nums[1:]:
            if num < cur_num:
                return False
            cur_num = num
        return True

    def is_decreasing(self, nums) -> bool:
        cur_num = nums[0]
        for num in nums[1:]:
            if num > cur_num:
                return False
            cur_num = num
        return True
    def isMonotonic(self, nums: List[int]) -> bool:
        # nums_increasing = sorted(nums)
        # nums_decreasing = list(reversed(nums_increasing))
        # return nums == nums_increasing or nums == nums_decreasing
        if len(nums) < 2:
            return True
        else:
            return self.is_decreasing(nums) or self.is_increasing(nums)
```
