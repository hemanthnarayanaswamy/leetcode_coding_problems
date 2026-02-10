<h2><a href="https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap">3484. Lexicographically Smallest String After a Swap</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code> containing only digits, return the <span data-keyword="lexicographically-smaller-string">lexicographically smallest string</span> that can be obtained after swapping <strong>adjacent</strong> digits in <code>s</code> with the same <strong>parity</strong> at most <strong>once</strong>.</p>

<p>Digits have the same parity if both are odd or both are even. For example, 5 and 9, as well as 2 and 4, have the same parity, while 6 and 9 do not.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;45320&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;43520&quot;</span></p>

<p><strong>Explanation: </strong></p>

<p><code>s[1] == &#39;5&#39;</code> and <code>s[2] == &#39;3&#39;</code> both have the same parity, and swapping them results in the lexicographically smallest string.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;001&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;001&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no need to perform a swap because <code>s</code> is already the lexicographically smallest.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists only of digits.</li>
</ul>

# Solution 
* Stop after one swap and after checking the swap, revert back to the original. 

1. We iterate through the digits of s by pairs, checking whether the pair is in descending order and whether the two digits have the same even-odd parity.
2. Once we encounter such a pair we reverse their order and return the revised string.
3. 
```python
class Solution:
    def getSmallestString(self, s: str) -> str:
        res = s
        n = len(s)

        for i in range(n-1):
            a, b = s[i], s[i+1]

            #if int(a) % 2 == int(b) % 2:   # Only check if b < a 
			if int(a) % 2 == int(b) % 2 and b < a:
                num = s[:i]+b+a+s[i+2:] 
                if num < res:
                    res = num
                    
        return res
```
---
```python
class Solution:
    def getSmallestString(self, s: str) -> str:
        res = s
        n = len(s)

        for i in range(n-1):
            a, b = s[i], s[i+1]

            if int(a) % 2 == int(b) % 2 and b < a:
                num = s[:i] + s[i:i+2][::-1] + s[i+2:] 
                if num < res:
                    res = num
                    
        return res
```
---
```python
class Solution:
    def getSmallestString(self, s: str) -> str:
        for i in range(len(s)-1):
            cur = int(s[i])
            nxt = int(s[i+1])
            if cur > nxt and cur % 2 == nxt % 2:
                return s[:i] + s[i:i+2][::-1] + s[i+2:]
        
        return s
```
