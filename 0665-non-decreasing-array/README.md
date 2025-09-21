<h2><a href="https://leetcode.com/problems/non-decreasing-array">665. Non-decreasing Array</a></h2><h3>Medium</h3><hr><p>Given an array <code>nums</code> with <code>n</code> integers, your task is to check if it could become non-decreasing by modifying <strong>at most one element</strong>.</p>

<p>We define an array is non-decreasing if <code>nums[i] &lt;= nums[i + 1]</code> holds for every <code>i</code> (<strong>0-based</strong>) such that (<code>0 &lt;= i &lt;= n - 2</code>).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> You could modify the first 4 to 1 to get a non-decreasing array.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,1]
<strong>Output:</strong> false
<strong>Explanation:</strong> You cannot get a non-decreasing array by modifying at most one element.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

# Solution 
```python
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        violation = 0

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                violation += 1

                if violation > 1:
                    return False 
                
                if i == 0:
                    nums[i] = nums[i+1]
                elif nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
        
        return True
```
* We track the violation and when more then one violation is detected we return early. 

##### Fixing the Violation
* When we find a violation `nums[i] > nums[i+1]`, We have two choices either lower the `num[i]` or increase the `num[i+1]`. 
* If the violation is at the beginning `i=0` only way is to lower the first number `nums[i] = nums[i+1]`. 
* If the violation is in the middle, `Lower nums[i] to match nums[i+1]`or `Raise nums[i+1] to match nums[i]`
* `nums[i-1] <= nums[i+1]`. This tells us if lowering `nums[i] to match nums[i+1]` would still keep the array non-decreasing up to that point.

```python
if nums[i-1] <= nums[i+1]:
    # Lowering nums[i] works
    nums[i] = nums[i+1]
else:
    # Must raise nums[i+1]
    nums[i+1] = nums[i]
```

```ini
Example 1: When Lowering Works
Consider the array [1, 5, 2, 6]:

Violation at 5 > 2
Should we lower 5 or raise 2?
Check: Is 1 <= 2? Yes!
So we can lower 5 to 2 safely: [1, 2, 2, 6]
This works because lowering 5 to 2 doesn't create a new violation with its predecessor
Example 2: When Lowering Fails
Consider the array [3, 5, 2, 6]:

Violation at 5 > 2
Should we lower 5 or raise 2?
Check: Is 3 <= 2? No!
If we lowered 5 to 2, we'd get [3, 2, 2, 6], creating a new violation
So we must raise 2 to 5: [3, 5, 5, 6]
```

```ini
Imagine arranging books on a shelf by height:

You find two books out of order (one tall book before a short book)
You can either make the tall book shorter or the short book taller
If making the tall book shorter would make it shorter than the book before it, that creates a new problem
In that case, you have to make the short book taller instead
```
