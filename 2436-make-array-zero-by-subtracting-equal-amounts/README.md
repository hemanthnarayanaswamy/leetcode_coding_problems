<h2><a href="https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/?envType=problem-list-v2&envId=n9iuhemc">2436. Make Array Zero by Subtracting Equal Amounts</a></h2><h3>Easy</h3><hr><p>You are given a non-negative integer array <code>nums</code>. In one operation, you must:</p>

<ul>
	<li>Choose a positive integer <code>x</code> such that <code>x</code> is less than or equal to the <strong>smallest non-zero</strong> element in <code>nums</code>.</li>
	<li>Subtract <code>x</code> from every <strong>positive</strong> element in <code>nums</code>.</li>
</ul>

<p>Return <em>the <strong>minimum</strong> number of operations to make every element in </em><code>nums</code><em> equal to </em><code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,0,3,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Each element in nums is already 0 so no operations are needed.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>

# Solution 
* Elements with the same value will always take the same number of operations to become 0. Contrarily, elements with different values will always take a different number of operations to become 0. So, its better to remove the duplicates from the original array. 
* The answer is the number of unique non-zero numbers in nums, 

```ini 
Think in this way suppose there are 3 different unique elements at a time you could target each element with it's own value to make it ZERO then for 3 elements you need 3 operations,
Suppose there are 5 elements you need 5 operations,
If there are n unique elements you need n opertations.
```

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        uniNum = set()

        for num in nums: 
            if num and num not in uniNum:
                uniNum.add(num)
        
        return len(uniNum)
```

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(n for n in nums if n!=0))
```

