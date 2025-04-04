<h2><a href="https://leetcode.com/problems/minimum-length-of-string-after-operations">3455. Minimum Length of String After Operations</a></h2><h3>Medium</h3><hr><p>You are given a string <code>s</code>.</p>

<p>You can perform the following process on <code>s</code> <strong>any</strong> number of times:</p>

<ul>
	<li>Choose an index <code>i</code> in the string such that there is <strong>at least</strong> one character to the left of index <code>i</code> that is equal to <code>s[i]</code>, and <strong>at least</strong> one character to the right that is also equal to <code>s[i]</code>.</li>
	<li>Delete the <strong>closest</strong> occurrence of <code>s[i]</code> located to the <strong>left</strong> of <code>i</code>.</li>
	<li>Delete the <strong>closest</strong> occurrence of <code>s[i]</code> located to the <strong>right</strong> of <code>i</code>.</li>
</ul>

<p>Return the <strong>minimum</strong> length of the final string <code>s</code> that you can achieve.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abaacbcbb&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong><br />
We do the following operations:</p>

<ul>
	<li>Choose index 2, then remove the characters at indices 0 and 3. The resulting string is <code>s = &quot;bacbcbb&quot;</code>.</li>
	<li>Choose index 3, then remove the characters at indices 0 and 5. The resulting string is <code>s = &quot;acbcb&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aa&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong><br />
We cannot perform any operations, so we return the length of the original string.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>

# Solution Approach 
* Only the frequency of each character matters in finding the final answer.
* Suppose there is a character that occurs at least 3 times in the string, we can repeatedly delete two of these characters until there are at most 2 occurrences left of it.
* So if the ffrequency of that character is `>3` and that number is even after delecting everything we should atleast have 2 left at the end 
* But if its odd then only 1 will be left in the end 

```python
from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        s_freq = Counter(s)
        count = 0

        for k,v in s_freq.items():
            if v >= 3:
                if v % 2 == 0:
                    count += 2
                else:
                    count += 1
            else:
                count += v
            
        return count
 ```
 
 ## Optimal Solution
 
```python
class Solution:
    def minimumLength(self, s: str) -> int:
        ans = 0
        for i in set(s):
            if s.count(i) % 2:
                ans += 1
            else:
                ans += 2
        return ans
```
*if  ` s.count(i) % 2` exists that is not zero then add += 1
* else += 2
