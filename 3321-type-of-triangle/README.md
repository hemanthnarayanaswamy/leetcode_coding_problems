<h2><a href="https://leetcode.com/problems/type-of-triangle">3321. Type of Triangle</a></h2><h3>Easy</h3><hr><p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> of size <code>3</code> which can form the sides of a triangle.</p>

<ul>
	<li>A triangle is called <strong>equilateral</strong> if it has all sides of equal length.</li>
	<li>A triangle is called <strong>isosceles</strong> if it has exactly two sides of equal length.</li>
	<li>A triangle is called <strong>scalene</strong> if all its sides are of different lengths.</li>
</ul>

<p>Return <em>a string representing</em> <em>the type of triangle that can be formed </em><em>or </em><code>&quot;none&quot;</code><em> if it <strong>cannot</strong> form a triangle.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3,3]
<strong>Output:</strong> &quot;equilateral&quot;
<strong>Explanation:</strong> Since all the sides are of equal length, therefore, it will form an equilateral triangle.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,5]
<strong>Output:</strong> &quot;scalene&quot;
<strong>Explanation:</strong> 
nums[0] + nums[1] = 3 + 4 = 7, which is greater than nums[2] = 5.
nums[0] + nums[2] = 3 + 5 = 8, which is greater than nums[1] = 4.
nums[1] + nums[2] = 4 + 5 = 9, which is greater than nums[0] = 3. 
Since the sum of the two sides is greater than the third side for all three cases, therefore, it can form a triangle.
As all the sides are of different lengths, it will form a scalene triangle.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums.length == 3</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>

# Solution 
```ini
Triangle Inequality Theorem: For three sides to form a valid triangle, the sum of any two sides must be strictly greater than the third side.

✅ a + b > c
✅ a + c > b
✅ b + c > a
Your original code used < which means you were checking if the sum was less than the third side, but you need to check if it's less than or equal to (<=) to determine when it's not a valid triangle.

Examples where your original code would fail:
[1, 2, 3] → 1 + 2 = 3 (not < 3), so your code would say it's a triangle, but it's actually "none"
[0, 1, 1] → 0 + 1 = 1 (not < 1), should be "none"
The corrected version properly identifies these as invalid triangles.
```
```python
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums[0], nums[1], nums[2]

        if (a + b <= c) or (a + c <= b) or (b+ c <= a):
            return "none"
        elif a == b == c:
            return 'equilateral'
        elif (a == b) or (b == c) or (a == c):
            return 'isosceles'
        else:
            return 'scalene'
```

---
```python
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        n = set(nums)
        a, b, c = nums
        if a + b <= c or a + c <= b or b + c <= a:
            return "none"
        if len(n) == 1:
            return "equilateral"

        elif len(n) == 2:
            return "isosceles"
        
        elif len(n) == 3:
            return "scalene"
```
