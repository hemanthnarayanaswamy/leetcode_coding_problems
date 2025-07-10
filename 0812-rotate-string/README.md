<h2><a href="https://leetcode.com/problems/rotate-string">812. Rotate String</a></h2><h3>Easy</h3><hr><p>Given two strings <code>s</code> and <code>goal</code>, return <code>true</code> <em>if and only if</em> <code>s</code> <em>can become</em> <code>goal</code> <em>after some number of <strong>shifts</strong> on</em> <code>s</code>.</p>

<p>A <strong>shift</strong> on <code>s</code> consists of moving the leftmost character of <code>s</code> to the rightmost position.</p>

<ul>
	<li>For example, if <code>s = &quot;abcde&quot;</code>, then it will be <code>&quot;bcdea&quot;</code> after one shift.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abcde", goal = "cdeab"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abcde", goal = "abced"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, goal.length &lt;= 100</code></li>
	<li><code>s</code> and <code>goal</code> consist of lowercase English letters.</li>
</ul>

# Solution 
* We need to perform the rotation of up to len(s) times and for each rotation we need to check if the rotated value matches the goal. 

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        slist = list(s)
        n = len(s)

        while n:
            slist.append(slist.pop(0)) # Remove the leftmost element and append it to the end to the Right 

            if ''.join(slist) == goal:
                return True 
            
            n -= 1
        
        return False 
```

* Improved version without using the list and only using the string slicing.

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if(s[i:] + s[:i] == goal):
                return True
        return False
```

# Optimal solution 
1.	If two strings are equal via some rotation, then goal must appear as a contiguous substring of s+s.
2.	Also they must be the same length.

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Quick length check
        if len(s) != len(goal):
            return False
        
        # Double s and see if goal sits inside
        return goal in (s + s)
```
