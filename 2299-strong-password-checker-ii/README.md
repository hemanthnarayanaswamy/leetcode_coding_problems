<h2><a href="https://leetcode.com/problems/strong-password-checker-ii">2391. Strong Password Checker II</a></h2><h3>Easy</h3><hr><p>A password is said to be <strong>strong</strong> if it satisfies all the following criteria:</p>

<ul>
	<li>It has at least <code>8</code> characters.</li>
	<li>It contains at least <strong>one lowercase</strong> letter.</li>
	<li>It contains at least <strong>one uppercase</strong> letter.</li>
	<li>It contains at least <strong>one digit</strong>.</li>
	<li>It contains at least <strong>one special character</strong>. The special characters are the characters in the following string: <code>&quot;!@#$%^&amp;*()-+&quot;</code>.</li>
	<li>It does <strong>not</strong> contain <code>2</code> of the same character in adjacent positions (i.e., <code>&quot;aab&quot;</code> violates this condition, but <code>&quot;aba&quot;</code> does not).</li>
</ul>

<p>Given a string <code>password</code>, return <code>true</code><em> if it is a <strong>strong</strong> password</em>. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> password = &quot;IloveLe3tcode!&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The password meets all the requirements. Therefore, we return true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> password = &quot;Me+You--IsMyDream&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> password = &quot;1aB!&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> The password does not meet the length requirement. Therefore, we return false.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= password.length &lt;= 100</code></li>
	<li><code>password</code> consists of letters, digits, and special characters: <code>&quot;!@#$%^&amp;*()-+&quot;</code>.</li>
</ul>

# Solution 
* Use the Flags to check each condition 

```python
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        length = False
        low = False
        up = False
        digit = False
        special = False
        specialChars = "!@#$%^&*()-+"
        prev = ''

        n = len(password)

        if n >= 8:
            length = True

        for c in password:
            if c == prev:
                return False
            elif c.islower():
                low = True
            elif c.isupper():
                up = True
            elif c.isdigit():
                digit = True
            elif c in specialChars:
                special = True
            prev = c

        return length and low and up and special and digit
```
---
```python
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n = len(password)
        if n < 8:
            return False
        up, lo, num, sp, spc = False, False, False, "!@#$%^&*()-+", False
        for i in range(n):
            if i > 0 and password[i] == password[i - 1]:
                return False
            
            if password[i].isupper():
                up = True
            elif password[i].islower():
                lo = True
            elif password[i].isdigit():
                num = True
            elif password[i] in sp:
                spc = True
            
        return up and lo and spc and num
```
