<h2><a href="https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/?envType=problem-list-v2&envId=n6j4czn6">957. Minimum Add to Make Parentheses Valid</a></h2><h3>Medium</h3><hr><p>A parentheses string is valid if and only if:</p>

<ul>
	<li>It is the empty string,</li>
	<li>It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid strings, or</li>
	<li>It can be written as <code>(A)</code>, where <code>A</code> is a valid string.</li>
</ul>

<p>You are given a parentheses string <code>s</code>. In one move, you can insert a parenthesis at any position of the string.</p>

<ul>
	<li>For example, if <code>s = &quot;()))&quot;</code>, you can insert an opening parenthesis to be <code>&quot;(<strong>(</strong>)))&quot;</code> or a closing parenthesis to be <code>&quot;())<strong>)</strong>)&quot;</code>.</li>
</ul>

<p>Return <em>the minimum number of moves required to make </em><code>s</code><em> valid</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;())&quot;
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(((&quot;
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code> is either <code>&#39;(&#39;</code> or <code>&#39;)&#39;</code>.</li>
</ul>

# Solution 
1. Every `(`, we put it into the stack
2. When `)`, we see if there are any `)` in `stack` and `pop()` it.
3. If `)` and no elements in `stack` means we need to add a extra `(` to make the string valid. 
4. Now after the iteration **If there are still elements in the stack that means, We need to add extrac closing brackets for all opening brackets in stack**

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        toAdd = 0

        for c in s:
            if c == '(':
                stack.append(c)
            elif stack:
                stack.pop()
            else:
                toAdd += 1
        
        toAdd += len(stack)

        return toAdd
```
