<h2><a href="https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii">2978. Check if Strings Can be Made Equal With Operations II</a></h2><h3>Medium</h3><hr><p>You are given two strings <code>s1</code> and <code>s2</code>, both of length <code>n</code>, consisting of <strong>lowercase</strong> English letters.</p>

<p>You can apply the following operation on <strong>any</strong> of the two strings <strong>any</strong> number of times:</p>

<ul>
	<li>Choose any two indices <code>i</code> and <code>j</code> such that <code>i &lt; j</code> and the difference <code>j - i</code> is <strong>even</strong>, then <strong>swap</strong> the two characters at those indices in the string.</li>
</ul>

<p>Return <code>true</code><em> if you can make the strings </em><code>s1</code><em> and </em><code>s2</code><em> equal, and&nbsp;</em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;abcdba&quot;, s2 = &quot;cabdab&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> We can apply the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = &quot;cbadba&quot;.
- Choose the indices i = 2, j = 4. The resulting string is s1 = &quot;cbbdaa&quot;.
- Choose the indices i = 1, j = 5. The resulting string is s1 = &quot;cabdab&quot; = s2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;abe&quot;, s2 = &quot;bea&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> It is not possible to make the two strings equal.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == s1.length == s2.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>s1</code> and <code>s2</code> consist only of lowercase English letters.</li>
</ul>

# Solution
```python
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False
        
        oddParity_s1 = []
        evenParity_s1 = []
        oddParity_s2 = []
        evenParity_s2 = []
        
        for i in range(len(s1)):
            if i % 2:
                oddParity_s1.append(s1[i])
                oddParity_s2.append(s2[i])
            else:
                evenParity_s1.append(s1[i])
                evenParity_s2.append(s2[i])
        
        if len(oddParity_s1) != len(oddParity_s2) or len(evenParity_s1) != len(evenParity_s2):
            return False
        
        if Counter(oddParity_s1) != Counter(oddParity_s2) or Counter(evenParity_s1) != Counter(evenParity_s2):
            return False
        
        return True
```
---
```python
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        odds1 = s1[1:n:2]
        evens1 = s1[0:n:2]
        odds2 = s2[1:n:2]
        evens2 = s2[0:n:2]
        
        if len(odds1) != len(odds2) or len(evens1) != len(evens2) or Counter(odds1) != Counter(odds2) or Counter(evens1) != Counter(evens2):
            return False
        
        return True
```
# Optimal Solution 
```python
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # strategy:
        # 1. odd indexes should contain the same elements in s1 and s2        
        # 2. even indexes should contain the same elements in s1 and s2

        return Counter(s1[::2]) == Counter(s2[::2]) and \
               Counter(s1[1::2]) == Counter(s2[1::2])
```							 
