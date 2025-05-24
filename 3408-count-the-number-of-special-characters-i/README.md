<h2><a href="https://leetcode.com/problems/count-the-number-of-special-characters-i">3408. Count the Number of Special Characters I</a></h2><h3>Easy</h3><hr><p>You are given a string <code>word</code>. A letter is called <strong>special</strong> if it appears <strong>both</strong> in lowercase and uppercase in <code>word</code>.</p>

<p>Return the number of<em> </em><strong>special</strong> letters in<em> </em><code>word</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;aaAbcBC&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The special characters in <code>word</code> are <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;abc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>No character in <code>word</code> appears in uppercase.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;abBCab&quot;</span></p>

<p><strong>Output:</strong> 1</p>

<p><strong>Explanation:</strong></p>

<p>The only special character in <code>word</code> is <code>&#39;b&#39;</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 50</code></li>
	<li><code>word</code> consists of only lowercase and uppercase English letters.</li>
</ul>

# Solution 
* Generate all the 26 alphabets and check for each character if the word has upper and lower character in it. 

* Code snippet to generate all characters
```python
for i in range(ord('a'), ord('z') + 1):
        print(chr(i))
```

```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        result = 0

        for i in range(ord('a'), ord('z') + 1):
            x = chr(i)
            if x.lower() in word and x.upper() in word:
                result += 1
        
        return result
```

# Optimal 
```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0
        word = set(word)
        for i in word:
            if i.islower() and i.upper() in word:
                res+=1
        return res
```
				
