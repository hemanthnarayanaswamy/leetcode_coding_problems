<h2><a href="https://leetcode.com/problems/valid-perfect-square">367. Valid Perfect Square</a></h2><h3>Easy</h3><hr><p>Given a positive integer num, return <code>true</code> <em>if</em> <code>num</code> <em>is a perfect square or</em> <code>false</code> <em>otherwise</em>.</p>

<p>A <strong>perfect square</strong> is an integer that is the square of an integer. In other words, it is the product of some integer with itself.</p>

<p>You must not use any built-in library function, such as <code>sqrt</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 16
<strong>Output:</strong> true
<strong>Explanation:</strong> We return true because 4 * 4 = 16 and 4 is an integer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 14
<strong>Output:</strong> false
<strong>Explanation:</strong> We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

# Solution 
![img](https://assets.leetcode.com/users/images/7470ff2b-6011-4a5b-b290-a457efd5dbec_1744310528.295415.png)
```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num 

        while l <= r:
            mid = (l + r) // 2
            square = mid ** 2
        
            if square == num:
                return True
            elif square > num:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
```
* you can reduce the right limit to `num // 2` instead of `num`

```python
class Solution(object):
    def isPerfectSquare(self, num):
        if num < 2:
            return True

        left, right = 2, num // 2
        while left <= right:
            mid = (left + right) // 2
            squared = mid * mid
            if squared == num:
                return True
            elif squared < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
```
**Binary search between `2` and `num / 2`:**

1. Compute `mid` and compare `mid * mid` with num.
2. Adjust boundaries until you find a match or exhaust the range.
3. Return `false` if no integer square root is found.

---
### Approach
The solution attempts to determine if a number is a perfect square:

1. Calculate the square root of the number using the power operator `(num ** 0.5)`
2. Check if the square root `modulo 2 equals 0 or 1`
3. If either condition is true, return True; otherwise return False
