<h2><a href="https://leetcode.com/problems/check-if-a-string-can-break-another-string">1530. Check If a String Can Break Another String</a></h2><h3>Medium</h3><hr><p>Given two strings: <code>s1</code> and <code>s2</code> with the same&nbsp;size, check if some&nbsp;permutation of string <code>s1</code> can break&nbsp;some&nbsp;permutation of string <code>s2</code> or vice-versa. In other words <code>s2</code> can break <code>s1</code>&nbsp;or vice-versa.</p>

<p>A string <code>x</code>&nbsp;can break&nbsp;string <code>y</code>&nbsp;(both of size <code>n</code>) if <code>x[i] &gt;= y[i]</code>&nbsp;(in alphabetical order)&nbsp;for all <code>i</code>&nbsp;between <code>0</code> and <code>n-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;abc&quot;, s2 = &quot;xya&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> &quot;ayx&quot; is a permutation of s2=&quot;xya&quot; which can break to string &quot;abc&quot; which is a permutation of s1=&quot;abc&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;abe&quot;, s2 = &quot;acd&quot;
<strong>Output:</strong> false 
<strong>Explanation:</strong> All permutations for s1=&quot;abe&quot; are: &quot;abe&quot;, &quot;aeb&quot;, &quot;bae&quot;, &quot;bea&quot;, &quot;eab&quot; and &quot;eba&quot; and all permutation for s2=&quot;acd&quot; are: &quot;acd&quot;, &quot;adc&quot;, &quot;cad&quot;, &quot;cda&quot;, &quot;dac&quot; and &quot;dca&quot;. However, there is not any permutation from s1 which can break some permutation from s2 and vice-versa.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;leetcodee&quot;, s2 = &quot;interview&quot;
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>s1.length == n</code></li>
	<li><code>s2.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10^5</code></li>
	<li>All strings consist of lowercase English letters.</li>
</ul>

# Approach 
```
Meaning of 'breakable' : After sorting alphanumerically, if s1[i .. n] >= s2[i .. n], s1 can break s2.

For example, 'axy' can break 'abc' like this:

a == a x > b y > c

All chars in 'axy' is bigger or equal than 'abc', so it's breakable.

And, 'abe' cannot break 'acd':

a == a b < c e > d

It's unbreakable because 'abe' cannot break 'acd' since 'b'.
```

* Only Return `True` if S1 breaks S2 or S2 break S1 else False

# Solution 
* Have two flags that checks if either operation breaks the other 
* Return the or operation of those Flags.
```python
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)

        BreakFlag1, BreakFlag2 = True, True   

        for i in range(len(s1)):
            if ord(s1[i]) >= ord(s2[i]):
                continue
            else:
                BreakFlag1 = False
                break 
        
        for i in range(len(s1)):
            if ord(s2[i]) >= ord(s1[i]):
                continue
            else:
                BreakFlag2 = False
                break
        
        return BreakFlag1 or BreakFlag2
```
-------------------------------------------------------------
* Optimized the user flag usage 

```python
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)

        BreakFlag = True

        for i in range(len(s1)):
            if ord(s1[i]) >= ord(s2[i]):
                continue
            else:
                BreakFlag = False
                break
        
        if BreakFlag == True:
            return BreakFlag
        else:
            for i in range(len(s1)):
                if ord(s2[i]) >= ord(s1[i]):
                    continue
                else:
                    BreakFlag = True
                    break

        return not BreakFlag
```
-----------------------------------------------------------------------------------
## Optimized Solution 
 ```python
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        canBreak1 = all(s1[i] >= s2[i] for i in range(len(s1)))
        canBreak2 = all(s2[i] >= s1[i] for i in range(len(s1)))
        return canBreak1 or canBreak2
```
-----------------------------------------------------------------------------------

```python
from collections import Counter

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:

        s1_counter = Counter(s1)
        s2_counter = Counter(s2)

        diff = 0
        s = set()

        for char in string.ascii_lowercase:
            diff += s1_counter[char] - s2_counter[char]

            if diff:
                s.add(diff > 0)
        
        return len(s) < 2
```
