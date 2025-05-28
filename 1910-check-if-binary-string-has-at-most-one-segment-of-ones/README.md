<h2><a href="https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/?envType=problem-list-v2&envId=string">1910. Check if Binary String Has at Most One Segment of Ones</a></h2><h3>Easy</h3><hr><p>Given a binary string <code>s</code> <strong>​​​​​without leading zeros</strong>, return <code>true</code>​​​ <em>if </em><code>s</code><em> contains <strong>at most one contiguous segment of ones</strong></em>. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;1001&quot;
<strong>Output:</strong> false
<strong>Explanation: </strong>The ones do not form a contiguous segment.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;110&quot;
<strong>Output:</strong> true</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s[i]</code>​​​​ is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
	<li><code>s[0]</code> is&nbsp;<code>&#39;1&#39;</code>.</li>
</ul>

# FXKing Solution 
* A contiguous segment of ones is one or more continuously occurring 1 in the string. The question asks you to find if the given string has only one contiguous segment of ones.

```
e.g. 1001 - has two contiguous segments of one - false
110 - has only one contiguous segment of one - true
11101 - has two contiguous segments of one - false
```
* Since the input string s cannot have any leading zeroes and must contain at most one contiguous segment of 1s, we need to check if "01" is present in s or not. If it is present, we can return False, else True.

* A few testcases to help understand the intuition:

```
1100 - True
11001 - False (since 01 is present).
111111000000 - True
1101010100 - False
1 - True
1111110000111 - False
```

```python
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s
```

# Optimal Solution
* `strip("0")` will remove both the leading and trailing zeroes in the string. Thus, if zeroes are present inside the string even after that operation, the output must be False.

```python
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        s = s.strip("0")
        return ("0" not in s)
```
