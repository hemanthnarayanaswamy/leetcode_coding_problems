<h2><a href="https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three">2542. Average Value of Even Numbers That Are Divisible by Three</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code> of <strong>positive</strong> integers, return <em>the average value of all even integers that are divisible by</em> <code>3</code><i>.</i></p>

<p>Note that the <strong>average</strong> of <code>n</code> elements is the <strong>sum</strong> of the <code>n</code> elements divided by <code>n</code> and <strong>rounded down</strong> to the nearest integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,6,10,12,15]
<strong>Output:</strong> 9
<strong>Explanation:</strong> 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,4,7,10]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no single number that satisfies the requirement, so return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

# Solution 
* Simple problem figure out yourself 

```python
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        avgsum  = []

        for num in nums:
            if num % 2 == 0 and num % 3 == 0: 
                avgsum.append(num)

        return sum(avgsum) // len(avgsum) if avgsum else 0
```
# Improved 
* Instead of both conditions use `6` modulo as 6 is gcd for 2 and 3.

```python
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        avgsum  = []

        for num in nums:
            if num % 6 == 0: 
                avgsum.append(num)

        return sum(avgsum) // len(avgsum) if avgsum else 0
```
# ONE Liner 
```python
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        return sum(a) // len(a) if (a := [num for num in nums if num % 6 == 0]) else 0
```
