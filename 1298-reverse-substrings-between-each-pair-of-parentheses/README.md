<h2><a href="https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses">1298. Reverse Substrings Between Each Pair of Parentheses</a></h2><h3>Medium</h3><hr><p>You are given a string <code>s</code> that consists of lower case English letters and brackets.</p>

<p>Reverse the strings in each pair of matching parentheses, starting from the innermost one.</p>

<p>Your result should <strong>not</strong> contain any brackets.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(abcd)&quot;
<strong>Output:</strong> &quot;dcba&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(u(love)i)&quot;
<strong>Output:</strong> &quot;iloveu&quot;
<strong>Explanation:</strong> The substring &quot;love&quot; is reversed first, then the whole string is reversed.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(ed(et(oc))el)&quot;
<strong>Output:</strong> &quot;leetcode&quot;
<strong>Explanation:</strong> First, we reverse the substring &quot;oc&quot;, then &quot;etco&quot;, and finally, the whole string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> only contains lower case English characters and parentheses.</li>
	<li>It is guaranteed that all parentheses are balanced.</li>
</ul>

# Solution 
* We need to reverse every substring inside the every bracket, and then remove that bracket. 
* We try to append all the characters, expext `)` when it is detected. 
* So whenever, `)` is detected, we run a loop until `(` is found in the stack. which covers working on string inside the brackets. 
* When we `pop()` the strings and store in a 'temp` array, and once `(` is detected, we can end the loop, `pop()` the `(` and than appened the stored `temp` back to the stack. 
* and return the `stack`. `''.join(stack) if stack else ''`
```python
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']

        for c in s:
            if c == ')':
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop()[::-1])
                stack.pop()
                stack.append(''.join(temp))
            else:
                stack.append(c)

        return ''.join(stack)
```
---
# Improved Solution
* We can remove the use of `temp` array and perform the operations inside the `stack` itself. 

```python
def reverseParentheses(s):
    stack = [""]

    for c in s:
        if c == "(":
            stack.append("")
        elif c == ")":
            rev = stack[-1][::-1]
            stack.pop()
            stack[-1] += rev
        else:
            stack[-1] += c

    return stack[0]
```
