<h2><a href="https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i">2999. Check if Strings Can be Made Equal With Operations I</a></h2><h3>Easy</h3><hr><p>You are given two strings <code>s1</code> and <code>s2</code>, both of length <code>4</code>, consisting of <strong>lowercase</strong> English letters.</p>

<p>You can apply the following operation on any of the two strings <strong>any</strong> number of times:</p>

<ul>
	<li>Choose any two indices <code>i</code> and <code>j</code> such that <code>j - i = 2</code>, then <strong>swap</strong> the two characters at those indices in the string.</li>
</ul>

<p>Return <code>true</code><em> if you can make the strings </em><code>s1</code><em> and </em><code>s2</code><em> equal, and </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;abcd&quot;, s2 = &quot;cdab&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> We can do the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = &quot;cbad&quot;.
- Choose the indices i = 1, j = 3. The resulting string is s1 = &quot;cdab&quot; = s2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;abcd&quot;, s2 = &quot;dacb&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> It is not possible to make the two strings equal.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>s1.length == s2.length == 4</code></li>
	<li><code>s1</code> and <code>s2</code> consist only of lowercase English letters.</li>
</ul>

# Solution
* Simple Problem, Don't complicate it. 
* We need to swap ` two indices i and j such that j - i = 2` 
```ini 
Since the length of S1 and S2 will only be 4 
we can only swap 0, 2 and 1, 3 are the only swaps 

and We don't need to check all index 
we check only 0, 1 index to see if character of both strings at that index is equal 

if its not equal we swap it 

and check if they are equal
```

```python
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)

        i = 0

        while i < 2:
            if s1[i] != s2[i]:
                s1[i], s1[i+2] = s1[i+2], s1[i]
            i += 1
        
        return s1 == s2
```

* Don't need to convert both to list, since we'll be only swapping elements in one array so use S1.

```python
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        i = 0

        while i < 2:
            if s1[i] != s2[i]:
                s1[i], s1[i+2] = s1[i+2], s1[i]
            i += 1
        
        return ''.join(s1) == s2
```
---
```python
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if set([s1[0], s1[2]]) != set([s2[0], s2[2]]) or set([s1[1], s1[3]]) != set([s2[1], s2[3]]):
            return False
        return True
```
