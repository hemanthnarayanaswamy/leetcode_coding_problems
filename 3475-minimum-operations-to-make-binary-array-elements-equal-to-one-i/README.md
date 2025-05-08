<h2><a href="https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/?envType=problem-list-v2&envId=array">3475. Minimum Operations to Make Binary Array Elements Equal to One I</a></h2><h3>Medium</h3><hr><p>You are given a <span data-keyword="binary-array">binary array</span> <code>nums</code>.</p>

<p>You can do the following operation on the array <strong>any</strong> number of times (possibly zero):</p>

<ul>
	<li>Choose <strong>any</strong> 3 <strong>consecutive</strong> elements from the array and <strong>flip</strong> <strong>all</strong> of them.</li>
</ul>

<p><strong>Flipping</strong> an element means changing its value from 0 to 1, and from 1 to 0.</p>

<p>Return the <strong>minimum</strong> number of operations required to make all elements in <code>nums</code> equal to 1. If it is impossible, return -1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,1,1,1,0,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong><br />
We can do the following operations:</p>

<ul>
	<li>Choose the elements at indices 0, 1 and 2. The resulting array is <code>nums = [<u><strong>1</strong></u>,<u><strong>0</strong></u>,<u><strong>0</strong></u>,1,0,0]</code>.</li>
	<li>Choose the elements at indices 1, 2 and 3. The resulting array is <code>nums = [1,<u><strong>1</strong></u>,<u><strong>1</strong></u>,<strong><u>0</u></strong>,0,0]</code>.</li>
	<li>Choose the elements at indices 3, 4 and 5. The resulting array is <code>nums = [1,1,1,<strong><u>1</u></strong>,<u><strong>1</strong></u>,<u><strong>1</strong></u>]</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,1,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong><br />
It is impossible to make all elements equal to 1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1</code></li>
</ul>

# Solution Appraoch 
* Initialize n as the size of nums.

* Initialize count to track the number of flip operations.

* Iterate through nums up to n - 3:

*  If nums[i] is 0, perform a triplet flip starting at i:
		*  Flip nums[i] to 1.
		*  Flip nums[i + 1] (toggle 0 to 1 or 1 to 0).
		*  Flip nums[i + 2] (toggle 0 to 1 or 1 to 0).
		*  Increment count as a flip operation was performed.
		*  If nums[n - 2] or nums[n - 1] is still 0, return -1 since making all elements 1 is impossible.

Otherwise, return count as the minimum number of operations needed.

`The first observation is that if a 0 appears near the end of the array (specifically within the last two positions), we cannot flip it using a full triplet. This means that if any 0 is left in the last two places after processing, it is impossible to make the entire array 1, so we return -1`

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        for i in range(n-2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                nums[i + 2] = 1 if nums[i + 2] == 0 else 0
                count += 1
        
        if nums[i+1] == 0 or nums[i+2] == 0:
            return -1
        
        return count
```
