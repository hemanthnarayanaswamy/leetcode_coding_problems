<h2><a href="https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/">3476. Find Minimum Operations to Make All Elements Divisible by Three</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code>. In one operation, you can add or subtract 1 from <strong>any</strong> element of <code>nums</code>.</p>

<p>Return the <strong>minimum</strong> number of operations to make all elements of <code>nums</code> divisible by 3.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>All array elements can be made divisible by 3 using 3 operations:</p>

<ul>
	<li>Subtract 1 from 1.</li>
	<li>Add 1 to 2.</li>
	<li>Subtract 1 from 4.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,6,9]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>

# Approach 
```
1 2 3 4 5 6 7 8 9 

* subtract 1 
* Increment 1
* no operation 
* decrement 1
* increment 1
* no operation 
* decrement 1
* increment 1
* no operation 
```
**If you observe the pattern all the number that are not divisible by 3 require one opeation either increment or decrement to be divisible by 3**

* So the total number of operations will be number of elements that are not divisible by 3 

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0

        for num in nums:
            if num % 3 != 0:
                operations += 1
        
        return operations
```

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len([num for num in nums if num % 3 != 0])
```
