<h2><a href="https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii">462. Minimum Moves to Equal Array Elements II</a></h2><h3>Medium</h3><hr><p>Given an integer array <code>nums</code> of size <code>n</code>, return <em>the minimum number of moves required to make all array elements equal</em>.</p>

<p>In one move, you can increment or decrement an element of the array by <code>1</code>.</p>

<p>Test cases are designed so that the answer will fit in a <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Only two moves are needed (remember each move increments or decrements one element):
[<u>1</u>,2,3]  =&gt;  [2,2,<u>3</u>]  =&gt;  [2,2,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,10,2,9]
<strong>Output:</strong> 16
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


# Soution
The minimum number of moves is equal to the sum of absolute differences between each element and the median of the array.
Sorting the array helps in finding the median efficiently.
The median is the middle element for arrays with odd length and the average of the two middle elements for arrays with even length.

```python
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)

        if n%2 == 1:
            median = nums[(n - 1) // 2]
        else:
            i = n // 2
            median = (nums[i] + nums[i-1]) // 2

        return sum([abs(num - median) for num in nums])
```

# Improved 
* reduce the complexity of calculating the median 

```python
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)

        median = nums[len(nums) // 2]

        return sum([abs(num - median) for num in nums])
```
