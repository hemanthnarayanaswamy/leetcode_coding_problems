<h2><a href="https://leetcode.com/problems/find-greatest-common-divisor-of-array">2106. Find Greatest Common Divisor of Array</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code>, return<strong> </strong><em>the <strong>greatest common divisor</strong> of the smallest number and largest number in </em><code>nums</code>.</p>

<p>The <strong>greatest common divisor</strong> of two numbers is the largest positive integer that evenly divides both numbers.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,5,6,9,10]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [7,5,6,8,3]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

# Solution 
* Find the minmum and maxmimum number in the list and find the gcd between them. 

```python
import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        return math.gcd(mn, mx)
```

# Long Solution 
```python
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_ele=min(nums)
        max_ele=max(nums)
        for i in range(1,min_ele+1):
            if(min_ele%i==0 and max_ele%i==0):
                gcd=i
        return gcd
```
