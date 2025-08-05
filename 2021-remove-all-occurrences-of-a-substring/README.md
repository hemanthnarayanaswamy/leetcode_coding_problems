<h2><a href="https://leetcode.com/problems/remove-all-occurrences-of-a-substring">2021. Remove All Occurrences of a Substring</a></h2><h3>Medium</h3><hr><p>Given two strings <code>s</code> and <code>part</code>, perform the following operation on <code>s</code> until <strong>all</strong> occurrences of the substring <code>part</code> are removed:</p>

<ul>
	<li>Find the <strong>leftmost</strong> occurrence of the substring <code>part</code> and <strong>remove</strong> it from <code>s</code>.</li>
</ul>

<p>Return <code>s</code><em> after removing all occurrences of </em><code>part</code>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters in a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;daabcbaabcbc&quot;, part = &quot;abc&quot;
<strong>Output:</strong> &quot;dab&quot;
<strong>Explanation</strong>: The following operations are done:
- s = &quot;da<strong><u>abc</u></strong>baabcbc&quot;, remove &quot;abc&quot; starting at index 2, so s = &quot;dabaabcbc&quot;.
- s = &quot;daba<strong><u>abc</u></strong>bc&quot;, remove &quot;abc&quot; starting at index 4, so s = &quot;dababc&quot;.
- s = &quot;dab<strong><u>abc</u></strong>&quot;, remove &quot;abc&quot; starting at index 3, so s = &quot;dab&quot;.
Now s has no occurrences of &quot;abc&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;axxxxyyyyb&quot;, part = &quot;xy&quot;
<strong>Output:</strong> &quot;ab&quot;
<strong>Explanation</strong>: The following operations are done:
- s = &quot;axxx<strong><u>xy</u></strong>yyyb&quot;, remove &quot;xy&quot; starting at index 4 so s = &quot;axxxyyyb&quot;.
- s = &quot;axx<strong><u>xy</u></strong>yyb&quot;, remove &quot;xy&quot; starting at index 3 so s = &quot;axxyyb&quot;.
- s = &quot;ax<strong><u>xy</u></strong>yb&quot;, remove &quot;xy&quot; starting at index 2 so s = &quot;axyb&quot;.
- s = &quot;a<strong><u>xy</u></strong>b&quot;, remove &quot;xy&quot; starting at index 1 so s = &quot;ab&quot;.
Now s has no occurrences of &quot;xy&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>1 &lt;= part.length &lt;= 1000</code></li>
	<li><code>s</code>​​​​​​ and <code>part</code> consists of lowercase English letters.</li>
</ul>

# Solution 
* Need to Still learn alot and need to solve a lot of problems 
```python
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '', 1)
        return s
```

```python
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            idx = s.find(part) # Itreturns the start idx of the part work
            if idx == -1: # If not part is found break the loop and return 
                break
            s = s[:idx] + s[idx+len(part):] # The new string is sting till start idx and remove the whole part string range and rest of the string
        return s
```

## Wrong Solution and Approach
```python
def removeOccurrences(s, part):
    stack = []
    i = 0
    while i <= len(s)-1:
        print(stack)
        if stack:
            print(stack[-1]+s[i:i+len(part)-1], part)
            if stack[-1]+s[i:i+len(part)-1] == part:
                    stack.pop()
                    i += len(part) - 1
            else:
                stack.append(s[i])
                i += 1
        else:
            stack.append(s[i])
            i += 1
        print(i)

    return ''.join(stack)
```            
* Take last character from stack + next len(part)-1 characters from string, it don't identify the part formed inside the stack. 
* The pattern matching logic is fundamentally flawed - you're not checking if the last len(part) characters in the stack form the part

## Improved Solution 
```python
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        p = len(part)

        for char in s:
            stack.append(char)

            if len(stack) >= p and ''.join(stack[-p:]) == part:
                for _ in range(p):
                    stack.pop()
        
        return ''.join(stack)
```

						
