<h2><a href="https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i">3768. Check If Digits Are Equal in String After Operations I</a></h2><h3>Easy</h3><hr><p>You are given a string <code>s</code> consisting of digits. Perform the following operation repeatedly until the string has <strong>exactly</strong> two digits:</p>

<ul>
	<li>For each pair of consecutive digits in <code>s</code>, starting from the first digit, calculate a new digit as the sum of the two digits <strong>modulo</strong> 10.</li>
	<li>Replace <code>s</code> with the sequence of newly calculated digits, <em>maintaining the order</em> in which they are computed.</li>
</ul>

<p>Return <code>true</code> if the final two digits in <code>s</code> are the <strong>same</strong>; otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;3902&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Initially, <code>s = &quot;3902&quot;</code></li>
	<li>First operation:
	<ul>
		<li><code>(s[0] + s[1]) % 10 = (3 + 9) % 10 = 2</code></li>
		<li><code>(s[1] + s[2]) % 10 = (9 + 0) % 10 = 9</code></li>
		<li><code>(s[2] + s[3]) % 10 = (0 + 2) % 10 = 2</code></li>
		<li><code>s</code> becomes <code>&quot;292&quot;</code></li>
	</ul>
	</li>
	<li>Second operation:
	<ul>
		<li><code>(s[0] + s[1]) % 10 = (2 + 9) % 10 = 1</code></li>
		<li><code>(s[1] + s[2]) % 10 = (9 + 2) % 10 = 1</code></li>
		<li><code>s</code> becomes <code>&quot;11&quot;</code></li>
	</ul>
	</li>
	<li>Since the digits in <code>&quot;11&quot;</code> are the same, the output is <code>true</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;34789&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Initially, <code>s = &quot;34789&quot;</code>.</li>
	<li>After the first operation, <code>s = &quot;7157&quot;</code>.</li>
	<li>After the second operation, <code>s = &quot;862&quot;</code>.</li>
	<li>After the third operation, <code>s = &quot;48&quot;</code>.</li>
	<li>Since <code>&#39;4&#39; != &#39;8&#39;</code>, the output is <code>false</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of only digits.</li>
</ul>

# Solution 
* First convert the string into a list of interger numbers before doing the iteration with the WHILE Loop. 

```python
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(x) for x in s]
        
        while len(s) > 2:
            newS = []
            for i in range(len(s)-1):
                tmp = (s[i] + s[i+1]) % 10
                newS.append(tmp)
            s = newS
        
        return s[0] == s[1]
```

# Optimal Solution 
```python
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # map characters → integers
        digits = list(map(int, s))
        # repeatedly replace with pairwise sums mod 10
        while len(digits) > 2:
            # zip(digits, digits[1:]) walks through pairs (a, b)
            digits = [(a + b) % 10 for a, b in zip(digits, digits[1:])]

        return digits[0] == digits[1]
```

```python
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        t = list(map(int, s))
        while len(t) > 2:
            for i in range(len(t) - 1):
                t[i] = (t[i] + t[i + 1]) % 10
            t.pop()
        return t[0] == t[1]
```
