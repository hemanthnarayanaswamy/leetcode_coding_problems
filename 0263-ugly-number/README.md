<h2><a href="https://leetcode.com/problems/ugly-number/solutions/?envType=problem-list-v2&envId=n9iuhemc">263. Ugly Number</a></h2><h3>Easy</h3><hr><p>An <strong>ugly number</strong> is a <em>positive</em> integer which does not have a prime factor other than 2, 3, and 5.</p>

<p>Given an integer <code>n</code>, return <code>true</code> <em>if</em> <code>n</code> <em>is an <strong>ugly number</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> true
<strong>Explanation:</strong> 6 = 2 &times; 3
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation:</strong> 1 has no prime factors.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 14
<strong>Output:</strong> false
<strong>Explanation:</strong> 14 is not ugly since it includes the prime factor 7.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

# Ugly Numbers 
* Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. So negative numbers are by default not ugly numbers. 

```ini 
Every number N can be written as product of prime numbers as
N = (A^a)(B^b)(C^c)....
where A,B,C.. represent prime numers
e.g 135 = (3^3)*(5^1) where 3 and 5 are prime numbers

Now in this question they have asked for numbers that have 2,3,5 as A,B,C or prime numbers,
that means those numbers that can be represented as -
Ugly number (U) = (2^a)(3^b)(5^c)
where a,b,c are positive numbers
As you can see 1 also satisfy above equation as
1 = (2^0)(3^0)(5^0)
thus it is also a ugly number
I hope this insight will help you in solving this question.
```
## Intuition
* The problem asks if a number n is an ugly number, which is defined as a number whose prime factors are limited to 2, 3, and 5.
* I immediately thought of continuously dividing n by these prime factors until no further division is possible. If the result is 1, then n is ugly because it has no other prime factors.

## Approach
* If n is less than or equal to 0, it’s not an ugly number by definition, so we return False.
* Iterate through the prime factors 2, 3, and 5.
* While n is divisible by the current prime factor, divide n by that factor.
* If, after all possible divisions, n becomes 1, it means n only had the prime factors 2, 3, and 5, so return True. Otherwise, return False.

### Complexity
Time complexity: O(logn), Because in each step, we are dividing n by 2, 3, or 5 until it can no longer be divided by them.

### Space complexity: O(1)
We are using only a few variables and no additional data structures.

```python 
class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 0:
            return False 
        
        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                break
        
        return n == 1
```

# Optimal Solution
```python
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for prime in [2, 3, 5]:
            while not n % prime:
                n /= prime
        return n== 1
```
