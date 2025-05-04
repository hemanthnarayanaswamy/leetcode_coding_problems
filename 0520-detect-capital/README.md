<h2><a href="https://leetcode.com/problems/detect-capital">520. Detect Capital</a></h2><h3>Easy</h3><hr><p>We define the usage of capitals in a word to be right when one of the following cases holds:</p>

<ul>
	<li>All letters in this word are capitals, like <code>&quot;USA&quot;</code>.</li>
	<li>All letters in this word are not capitals, like <code>&quot;leetcode&quot;</code>.</li>
	<li>Only the first letter in this word is capital, like <code>&quot;Google&quot;</code>.</li>
</ul>

<p>Given a string <code>word</code>, return <code>true</code> if the usage of capitals in it is right.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> word = "USA"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> word = "FlaG"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 100</code></li>
	<li><code>word</code> consists of lowercase and uppercase English letters.</li>
</ul>

# Solution
* Generate all possible options and check one by one and return True is it matches with any of the condition else return False.
```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upperWord = word.upper()
        lowerWord = word.lower()
        captialWord = word.capitalize()

        if word == upperWord:
            return True
        elif word == lowerWord:
            return True 
        elif word == captialWord:
            return True 
        else:
            return False
```

## Optimal Solution 
```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
```
