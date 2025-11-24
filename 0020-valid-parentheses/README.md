<h2><a href="https://leetcode.com/problems/valid-parentheses">20. Valid Parentheses</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code> containing just the characters <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;[&#39;</code> and <code>&#39;]&#39;</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
	<li>Every close bracket has a corresponding open bracket of the same type.</li>
</ol>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;()&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;()[]{}&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;(]&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;([])&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p><strong class="example">Example 5:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;([)]&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of parentheses only <code>&#39;()[]{}&#39;</code>.</li>
</ul>

# Solution 
We use `HashMap` and `Stack`. We know valid combination, so initialize the combination with `HashMap` before we iterate through the input string.

`mapping = { ")":"(", "}":"{", "]":"[" }`
**`Stack` has only open parentheses. When a close parenthesis comes, we use it as a key to find valid open parenthesis in the mapping. If the two parentheses(current parenthesis and the latest parenthesis in Stack) are not valid combination, we should return `False`.**
* At last, `if Stack is empty, we should return True`.
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in brackets:
                if stack and brackets[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return False if stack else True
```
---
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in brackets:
                if stack and brackets[i] == stack.pop():
                    return False
            else:
                stack.append(i)
        
        return False if stack else True
```
