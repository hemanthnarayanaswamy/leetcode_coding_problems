<h2><a href="https://leetcode.com/problems/clear-digits">3447. Clear Digits</a></h2><h3>Easy</h3><hr><p>You are given a string <code>s</code>.</p>

<p>Your task is to remove <strong>all</strong> digits by doing this operation repeatedly:</p>

<ul>
	<li>Delete the <em>first</em> digit and the <strong>closest</strong> <b>non-digit</b> character to its <em>left</em>.</li>
</ul>

<p>Return the resulting string after removing all digits.</p>

<p><strong>Note</strong> that the operation <em>cannot</em> be performed on a digit that does not have any non-digit character to its left.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;abc&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no digit in the string.<!-- notionvc: ff07e34f-b1d6-41fb-9f83-5d0ba3c1ecde --></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;cb34&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>First, we apply the operation on <code>s[2]</code>, and <code>s</code> becomes <code>&quot;c4&quot;</code>.</p>

<p>Then we apply the operation on <code>s[1]</code>, and <code>s</code> becomes <code>&quot;&quot;</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists only of lowercase English letters and digits.</li>
	<li>The input is generated such that it is possible to delete all digits.</li>
</ul>

# Solution 
* First we initiate the Stack then in one iteration, 
* We check the c is number if it is a number and the stack is not empty then remove the element from the stack but continue if the stack is empty. 
* if its not number append the character to the stack. 

```python
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        i = 0

        while i < len(s):
            if s[i].isnumeric():
                if stack:
                    stack.pop()
            else:
                stack.append(s[i])
            
            i += 1
        
        return ''.join(stack)
```

# Optimal Solution
```python
class Solution:
    def clearDigits(self, string: str) -> str:
        stack = []
        for s in string:
            if s.isdigit():
                stack.pop()
            else:
                stack.append(s)
        return "".join(stack)
```
