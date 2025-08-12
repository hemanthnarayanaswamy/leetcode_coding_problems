<h2><a href="https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements">2269. Count Elements With Strictly Smaller and Greater Elements </a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code>, return <em>the number of elements that have <strong>both</strong> a strictly smaller and a strictly greater element appear in </em><code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [11,7,2,15]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The element 7 has the element 2 strictly smaller than it and the element 11 strictly greater than it.
Element 11 has element 7 strictly smaller than it and element 15 strictly greater than it.
In total there are 2 elements having both a strictly smaller and a strictly greater element appear in <code>nums</code>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-3,3,3,90]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The element 3 has the element -3 strictly smaller than it and the element 90 strictly greater than it.
Since there are two elements with the value 3, in total there are 2 elements having both a strictly smaller and a strictly greater element appear in <code>nums</code>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

# Solution 
```python
class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = 0
        max_val, min_val = max(nums), min(nums)

        for num in nums:
            if min_val < num < max_val:  
                count += 1
        
        return count
```

#### The problem wants to count elements that have:

* At least one element in the entire array that is strictly smaller
* At least one element in the entire array that is strictly greater

- It's not about the position or neighbors - it's about whether smaller and larger values exist anywhere in the array.

```ini
Example to Illustrate the Difference
Let's say nums = [11, 7, 2, 15]:
Your approach checks neighbors:

Index 1 (value 7): neighbors are 11 and 2 → 11 > 7 > 2 ✓ (counts it)
Index 2 (value 2): neighbors are 7 and 15 → 7 > 2 < 15 ✗ (doesn't count)

Correct approach checks entire array:

11: has smaller (7,2) and larger (15) ✓
7: has smaller (2) and larger (11,15) ✓
2: has larger (7,11,15) but no smaller ✗
15: has smaller (11,7,2) but no larger ✗
```

```python
class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)
        
        return sum(1 for num in nums if min_val < num < max_val)
```
