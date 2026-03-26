<h2><a href="https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced">2095. Minimum Number of Swaps to Make the String Balanced</a></h2><h3>Medium</h3><hr><p>You are given a <strong>0-indexed</strong> string <code>s</code> of <strong>even</strong> length <code>n</code>. The string consists of <strong>exactly</strong> <code>n / 2</code> opening brackets <code>&#39;[&#39;</code> and <code>n / 2</code> closing brackets <code>&#39;]&#39;</code>.</p>

<p>A string is called <strong>balanced</strong> if and only if:</p>

<ul>
	<li>It is the empty string, or</li>
	<li>It can be written as <code>AB</code>, where both <code>A</code> and <code>B</code> are <strong>balanced</strong> strings, or</li>
	<li>It can be written as <code>[C]</code>, where <code>C</code> is a <strong>balanced</strong> string.</li>
</ul>

<p>You may swap the brackets at <strong>any</strong> two indices <strong>any</strong> number of times.</p>

<p>Return <em>the <strong>minimum</strong> number of swaps to make </em><code>s</code> <em><strong>balanced</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;][][&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> You can make the string balanced by swapping index 0 with index 3.
The resulting string is &quot;[[]]&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;]]][[[&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> You can do the following to make the string balanced:
- Swap index 0 with index 4. s = &quot;[]][][&quot;.
- Swap index 1 with index 5. s = &quot;[[][]]&quot;.
The resulting string is &quot;[[][]]&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;[]&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> The string is already balanced.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == s.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>6</sup></code></li>
	<li><code>n</code> is even.</li>
	<li><code>s[i]</code> is either <code>&#39;[&#39; </code>or <code>&#39;]&#39;</code>.</li>
	<li>The number of opening brackets <code>&#39;[&#39;</code> equals <code>n / 2</code>, and the number of closing brackets <code>&#39;]&#39;</code> equals <code>n / 2</code>.</li>
</ul>

# Hints
* Iterate over the string and keep track of the number of opening and closing brackets on each step.
**If the number of closing brackets is even larger, you need to make a swap.**
**Swap it with the opening bracket closest to the end of `s`.**

```python
class Solution:
    def minSwaps(self, s: str) -> int:
        s = list(s)
        brackets = {'[': 0, ']': 0}
        l, r = 0, len(s)-1
        swaps = 0

        while l < r:
            brackets[s[l]] += 1

            while brackets[']'] > brackets['[']:
                if s[l] == ']' and s[r] == '[':
                    s[l], s[r] = s[r], s[l]
                    brackets['['] += 1
                    brackets[']'] -= 1
                    swaps += 1
                else:
                    r -= 1  
            l += 1
        
        return swaps
```
---
* We are given a 0-indexed string `s` of even length `n` made up of `n/2` opening brackets `[` and `n/2` closing brackets `]`. Our task is to return the minimum number of swaps to make the string balanced.
* Balanced parentheses mean that every opening bracket `[` has a matching closing bracket `]` in the correct order. **Unbalanced parentheses**occur when there are more closing brackets `]` than opening brackets `[` at some point in the string.

1. Swapping balanced brackets won't help. If you swap characters in a balanced pair like `[]`, it becomes `][`, which makes the string unbalanced. So, this type of swap increases the problem instead of solving it.
2. Swapping unbalanced brackets can fix the string. If a closing bracket `]` appears before its matching opening bracket `[`, a swap between an unbalanced `]` and an unbalanced `[` will balance one pair.

**What is the maximum number of brackets that you can balance with a single swap?**
- The answer is `2` for all parentheses of the form `][`. Therefore, the optimal approach is to swap unbalanced parentheses with each other. Since 2 unbalanced parentheses are made balanced with a single swap, **the total number of swaps to balance are given by `unbalanced / 2`.**

```python
class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        
        for ch in s:
            if ch == '[':
                stack.append(ch)
            else:  # ch == ']'
                if stack:
                    stack.pop()  # balancing closing bracket ] with an open bracket in the stack
        
        # size of stack = number of unbalanced open brackets
        return math.ceil(len(stack)/2)
```
---
```python
class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        
        for ch in s:
            if ch == '[':
                stack.append(ch)
            else:  # ch == ']'
                if stack:
                    stack.pop()  # balancing closing bracket ] with an open bracket in the stack
        
        # size of stack = number of unbalanced open brackets
        return (len(stack) + 1) // 2
```
