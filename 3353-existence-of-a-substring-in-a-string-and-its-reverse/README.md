<h2><a href="https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse">3353. Existence of a Substring in a String and Its Reverse</a></h2><h3>Easy</h3><hr><p>Given a<strong> </strong>string <code>s</code>, find any <span data-keyword="substring">substring</span> of length <code>2</code> which is also present in the reverse of <code>s</code>.</p>

<p>Return <code>true</code><em> if such a substring exists, and </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s = &quot;leetcode&quot;</span></p>

<p><strong>Output: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">true</span></p>

<p><strong>Explanation:</strong> Substring <code>&quot;ee&quot;</code> is of length <code>2</code> which is also present in <code>reverse(s) == &quot;edocteel&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s = &quot;abcba&quot;</span></p>

<p><strong>Output: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">true</span></p>

<p><strong>Explanation:</strong> All of the substrings of length <code>2</code> <code>&quot;ab&quot;</code>, <code>&quot;bc&quot;</code>, <code>&quot;cb&quot;</code>, <code>&quot;ba&quot;</code> are also present in <code>reverse(s) == &quot;abcba&quot;</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s = &quot;abcd&quot;</span></p>

<p><strong>Output: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">false</span></p>

<p><strong>Explanation:</strong> There is no substring of length <code>2</code> in <code>s</code>, which is also present in the reverse of <code>s</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>

# Solution 
* its something like brute force not good practice solution 

```python
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev=s[::-1]
        for i in range(1,len(s)):
            chs=s[i-1:i+1]
            if chs in rev:
                return True
        return False
```

# Optimal Solution 
* We need to find a substring of len 2 in s that is also in sReverse, 
* Then that means a reverse substring of len 2 in s Reverse should be in s. 

```ini 
Instead of finding substring `s[i-1:i+1]` we try to find s[i]+s[i-1] which is reverse of the substring is s in s. 
```

```python
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(1, len(s)):
            if s[i]+s[i-1] in s:
                return True 
        
        return False
```
