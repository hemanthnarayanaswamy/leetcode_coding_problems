<h2><a href="https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative">2524. Largest Positive Integer That Exists With Its Negative</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code> that <strong>does not contain</strong> any zeros, find <strong>the largest positive</strong> integer <code>k</code> such that <code>-k</code> also exists in the array.</p>

<p>Return <em>the positive integer </em><code>k</code>. If there is no such integer, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,2,-3,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> 3 is the only valid k we can find in the array.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,10,6,7,-7,1]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [-10,8,6,7,-2,-3]
<strong>Output:</strong> -1
<strong>Explanation:</strong> There is no a single valid k, we return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>nums[i] != 0</code></li>
</ul>

# Solution 
* Lets use `set()` to store the unique numbers and have a lookup thing, for a number check if its counter number is present is greater than the present large number and after all iteration return the large number. 

```python
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        larNum = -1 

        numsUniq = set(nums)

        for num in numsUniq:
            if -num in numsUniq and abs(num) > larNum:
                larNum = abs(num)
        
        return larNum
```

# Optimal Solution 
* Instead of building the full set and then looping over it again, you can check for the negation as you go:
```python
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        larNum = -1 
        seen = set()

        for num in nums:
            if -num in seen:
                if abs(num) > larNum:
                    larNum = abs(num)
            
            seen.add(num)
        
        return larNum
```

```python
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        # generate abs(x) for every x whose negation is also in s
        return max((abs(x) for x in s if -x in s), default=-1)
```
