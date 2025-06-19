<h2><a href="https://leetcode.com/problems/maximum-odd-binary-number">3055. Maximum Odd Binary Number</a></h2><h3>Easy</h3><hr><p>You are given a <strong>binary</strong> string <code>s</code> that contains at least one <code>&#39;1&#39;</code>.</p>

<p>You have to <strong>rearrange</strong> the bits in such a way that the resulting binary number is the <strong>maximum odd binary number</strong> that can be created from this combination.</p>

<p>Return <em>a string representing the maximum odd binary number that can be created from the given combination.</em></p>

<p><strong>Note </strong>that the resulting string <strong>can</strong> have leading zeros.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;010&quot;
<strong>Output:</strong> &quot;001&quot;
<strong>Explanation:</strong> Because there is just one &#39;1&#39;, it must be in the last position. So the answer is &quot;001&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;0101&quot;
<strong>Output:</strong> &quot;1001&quot;
<strong>Explanation: </strong>One of the &#39;1&#39;s must be in the last position. The maximum number that can be made with the remaining digits is &quot;100&quot;. So the answer is &quot;1001&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists only of <code>&#39;0&#39;</code> and <code>&#39;1&#39;</code>.</li>
	<li><code>s</code> contains at least one <code>&#39;1&#39;</code>.</li>
</ul>

# Solution 
```ini 
Binary number values 
<even Numbers>......8 4 2 1
```
* The numbers to be odd the right most digit should be 1.
* To make the number maximum the 1 should be towards the left side together 

1. Get the numbers of 1s present in the string and construct your own version of the number. 

```python
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        onesCount = s.count('1') 
        zerosCount = len(s) - onesCount

        return '1'*(onesCount-1) + '0'*zerosCount + '1'
```

```python
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        # place all but one '1' at the front, then all  '0's, then the final '1'
        return '1'*(ones-1) + '0'*(len(s)-ones) + '1'
```
