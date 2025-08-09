<h2><a href="https://leetcode.com/problems/power-of-two">231. Power of Two</a></h2><h3>Easy</h3><hr><p>Given an integer <code>n</code>, return <em><code>true</code> if it is a power of two. Otherwise, return <code>false</code></em>.</p>

<p>An integer <code>n</code> is a power of two, if there exists an integer <code>x</code> such that <code>n == 2<sup>x</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>0</sup> = 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 16
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>4</sup> = 16
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without loops/recursion?

# Solution 
I wish the poster for the n&(n-1) trick gave a more intuitive reason for why it works. This is my reasoning:

> At a power of 2, we only have one bit set to 1 at its respective decimal place (e.g. 1000).
> At the power of 2 minus 1, we have all the bits before the current decimal place set to 1 (e.g. 0111), which means that n & (n - 1) == 0 for powers of 2.
> The reason why this happens is because we're in the binary number system and a power of 2 means we're going to the next decimal place (i.e. 0111 + 1 = 1000).

* What about when n is not a power of 2? If you look at a list of binary numbers:
* 0100
* 0101
* 0110
* 0111
* 1000

```
Remember how the power of 2 is the special case where adding 1 results in us moving to the next decimal place (i.e. 0111 + 1 = 1000)? Since every other case doesn't result in that, there is at least the current power of 2's 1 bit overlapping with whatever the number is (i.e. we're at 0100, 0101 will always share the 0100 bit. The only time the 0100 bit becomes 0 again is if we go to the next power of 2).
```
```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n & (n-1) == 0)
```
