<h2><a href="https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer">1406. Subtract the Product and Sum of Digits of an Integer</a></h2><h3>Easy</h3><hr>Given an integer number <code>n</code>, return the difference between the product of its digits and the sum of its digits.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 234
<strong>Output:</strong> 15 
<b>Explanation:</b> 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 4421
<strong>Output:</strong> 21
<b>Explanation: 
</b>Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
</ul>


# Solution
```python
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, p = 0, 1
        n = [int(num) for num in str(n)]
        
        for num in n:
            s += num
            p *= num
        
        return p - s 
```

# Optimal Solution
```python
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_digits = 0
        product_digits = 1

        while n > 0:
            digit = n % 10
            sum_digits += digit
            product_digits *= digit
            n //= 10

        return product_digits - sum_digits
```
