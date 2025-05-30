<h2><a href="https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k">2116. Count Number of Pairs With Absolute Difference K</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the number of pairs</em> <code>(i, j)</code> <em>where</em> <code>i &lt; j</code> <em>such that</em> <code>|nums[i] - nums[j]| == k</code>.</p>

<p>The value of <code>|x|</code> is defined as:</p>

<ul>
	<li><code>x</code> if <code>x &gt;= 0</code>.</li>
	<li><code>-x</code> if <code>x &lt; 0</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,2,1], k = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong> The pairs with an absolute difference of 1 are:
- [<strong><u>1</u></strong>,<strong><u>2</u></strong>,2,1]
- [<strong><u>1</u></strong>,2,<strong><u>2</u></strong>,1]
- [1,<strong><u>2</u></strong>,2,<strong><u>1</u></strong>]
- [1,2,<strong><u>2</u></strong>,<strong><u>1</u></strong>]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3], k = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no pairs with an absolute difference of 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,1,5,4], k = 2
<strong>Output:</strong> 3
<b>Explanation:</b> The pairs with an absolute difference of 2 are:
- [<strong><u>3</u></strong>,2,<strong><u>1</u></strong>,5,4]
- [<strong><u>3</u></strong>,2,1,<strong><u>5</u></strong>,4]
- [3,<strong><u>2</u></strong>,1,5,<strong><u>4</u></strong>]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 99</code></li>
</ul>

## Solution Approach 
* We need to return the count of the occurance of the conditions 
* Brute Force Approach is you use two for loop and than checking the diff between each element to be k or not and then incrementing the count 
* But the solution takes `O(n*2)` so we need to do it much better

1. we are counting the frequency of each number and tracking them 
```python
nums_map = {}
    for num in nums: # we are counting the frequency of each number and tracking them 
        if num in nums_map:
            nums_map[num] += 1
        else:
            nums_map[num] = 1
```

2. Now we again do a second loop for nums and check is `num+k` exists inside the hash map, 
- If it exists that means we need to increment the count by the value of the frequfrequency of that numbers occurance 
```python
count = 0
    
    for num in nums:
        temp = num+k
        if temp in nums_map:
            count += nums_map[temp]
    return count
```

<b> Final Solution </b>
```python
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums_map = {}
        for num in nums: # we are counting the frequency of each number and tracking them 
            if num in nums_map:
                nums_map[num] += 1
            else:
                nums_map[num] = 1

        count = 0
        
        for num in nums:
            if num+k in nums_map:
                count += nums_map[num+k]
        return count
 ```
 
 ## Optimized Solution 
 - In if conditions use the engative statement for better result and time 
 
 ```python
 class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums_map = {}
        for num in nums: # we are counting the frequency of each number and tracking them 
            if num not in nums_map:
                nums_map[num] = 1
            else:
                nums_map[num] += 1

        count = 0
        
        for num in nums:
            if num+k in nums_map:
                count += nums_map[num+k]
        return count
```
