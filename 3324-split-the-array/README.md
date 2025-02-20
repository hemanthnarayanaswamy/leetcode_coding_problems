<h2><a href="https://leetcode.com/problems/split-the-array">3324. Split the Array</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code> of <strong>even</strong> length. You have to split the array into two parts <code>nums1</code> and <code>nums2</code> such that:</p>

<ul>
	<li><code>nums1.length == nums2.length == nums.length / 2</code>.</li>
	<li><code>nums1</code> should contain <strong>distinct </strong>elements.</li>
	<li><code>nums2</code> should also contain <strong>distinct</strong> elements.</li>
</ul>

<p>Return <code>true</code><em> if it is possible to split the array, and </em><code>false</code> <em>otherwise</em><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2,2,3,4]
<strong>Output:</strong> true
<strong>Explanation:</strong> One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,1]
<strong>Output:</strong> false
<strong>Explanation:</strong> The only possible way to split nums is nums1 = [1,1] and nums2 = [1,1]. Both nums1 and nums2 do not contain distinct elements. Therefore, we return false.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>nums.length % 2 == 0 </code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>

## Approach 

The problem requires us to split the given array into two parts such that both contain distinct elements. The key observation is that if any number appears more than twice, it becomes impossible to distribute it between the two subarrays while keeping both distinct.

* Meaning elements in nums1 should be unique `len(nums1) == len(set(nums1))`

Approach
1. Count the occurrences of each number in nums using Counter().
2. If any number appears more than twice, return False, since it would be impossible to distribute it while maintaining distinct elements in both halves.
3. Otherwise, return True, as we can always split the array into two valid halves.

```python 
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums_map = {}

        for i in range(len(nums)):
            nums_map[nums[i]] = nums_map.get(nums[i], 0) + 1
						
        for key in nums_map:
            if nums_map[key] > 2:
                return False
        return True
```

```python 
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums) # Using Counter to get frequency

        for value in counter.values():
            if value > 2:
                return False

        return True
```    

