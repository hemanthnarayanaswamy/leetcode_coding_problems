<h2><a href="https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram">1469. Minimum Number of Steps to Make Two Strings Anagram</a></h2><h3>Medium</h3><hr><p>You are given two strings of the same length <code>s</code> and <code>t</code>. In one step you can choose <strong>any character</strong> of <code>t</code> and replace it with <strong>another character</strong>.</p>

<p>Return <em>the minimum number of steps</em> to make <code>t</code> an anagram of <code>s</code>.</p>

<p>An <strong>Anagram</strong> of a string is a string that contains the same characters with a different (or the same) ordering.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bab&quot;, t = &quot;aba&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> Replace the first &#39;a&#39; in t with b, t = &quot;bba&quot; which is anagram of s.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leetcode&quot;, t = &quot;practice&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> Replace &#39;p&#39;, &#39;r&#39;, &#39;a&#39;, &#39;i&#39; and &#39;c&#39; from t with proper characters to make t anagram of s.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;anagram&quot;, t = &quot;mangaar&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> &quot;anagram&quot; and &quot;mangaar&quot; are anagrams. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s.length == t.length</code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters only.</li>
</ul>

## Solution Approach
* Compute the Frequency of the elements 
* Iterater through in char in t to see if that element is in s
* If it is not then all the occurance of the elements needs to be changed 
* Then If that char is in s also it is excess in t compared to s, all the excess occurance of that char also needs to change. 

```python
from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_feq = Counter(s)  ## Compute the Frequency of the elements 
        t_feq = Counter(t)

        count = 0           # To track the Changes Required

        for char in t_feq:  # Check each char in t
            if char not in s_feq:   # If that char is not in s
                count += t_feq[char]  # All that char needs to be changed
            else:
                temp_diff = t_feq[char] - s_feq[char]
                if temp_diff > 0:  # If that element is present and If its count is excess than s 
                    count += temp_diff  # it also needs to be changed
        return count
```

## Solution without Counters
```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_feq, t_feq = {}, {} 
        for i in range(len(s)):
            s_feq[s[i]] = s_feq.get(s[i], 0) + 1
            t_feq[t[i]] = t_feq.get(t[i], 0) + 1


        count = 0           # To track the Changes Required

        for char in t_feq:  # Check each char in t
            if char not in s_feq:   # If that char is not in s
                count += t_feq[char]  # All that char needs to be changed
            else:
                temp_diff = t_feq[char] - s_feq[char]
                if temp_diff > 0:  # If that element is present and If its count is excess than s 
                    count += temp_diff  # it also needs to be changed
        return count
```

## Optimal Solution

```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        replacementCount = 0
        
        s = Counter(s)
        t = Counter(t)
        
        for val, count in s.items():
            if t[val] < count:
                replacementCount += count - t[val]
        
        return replacementCount
```
