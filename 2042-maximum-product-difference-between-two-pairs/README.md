<h2><a href="https://leetcode.com/problems/maximum-product-difference-between-two-pairs">2042. Maximum Product Difference Between Two Pairs</a></h2><h3>Easy</h3><hr><p>The <strong>product difference</strong> between two pairs <code>(a, b)</code> and <code>(c, d)</code> is defined as <code>(a * b) - (c * d)</code>.</p>

<ul>
	<li>For example, the product difference between <code>(5, 6)</code> and <code>(2, 7)</code> is <code>(5 * 6) - (2 * 7) = 16</code>.</li>
</ul>

<p>Given an integer array <code>nums</code>, choose four <strong>distinct</strong> indices <code>w</code>, <code>x</code>, <code>y</code>, and <code>z</code> such that the <strong>product difference</strong> between pairs <code>(nums[w], nums[x])</code> and <code>(nums[y], nums[z])</code> is <strong>maximized</strong>.</p>

<p>Return <em>the <strong>maximum</strong> such product difference</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,6,2,7,4]
<strong>Output:</strong> 34
<strong>Explanation:</strong> We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,5,9,7,4,8]
<strong>Output:</strong> 64
<strong>Explanation:</strong> We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

## SOLUTION
1. My solution is a simple solution with time complexity O(n* logn) as we are using sorting to sort the array first 
2. Than we only want 4 numbers 2 max and 2 min numbers 
3.  `return sorted_nums[-1]* sorted_nums[-2] - sorted_nums[0]*sorted_nums[1]`

4. Sorting in place (nums.sort()) is more memory-efficient than creating a new sorted array with sorted(). Sorting in place modifies the original list, avoiding the creation of a new list. 
```python 
nums.sort()
a, b = nums[-1], nums[-2]
c, d = nums[0], nums[1]
return (a * b) - (c * d)
```

<ul>
	<li><code>4 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>
