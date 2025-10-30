<h2><a href="https://leetcode.com/problems/find-the-original-typed-string-i">3617. Find the Original Typed String I</a></h2><h3>Easy</h3><hr><p>Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and <strong>may</strong> press a key for too long, resulting in a character being typed <strong>multiple</strong> times.</p>

<p>Although Alice tried to focus on her typing, she is aware that she may still have done this <strong>at most</strong> <em>once</em>.</p>

<p>You are given a string <code>word</code>, which represents the <strong>final</strong> output displayed on Alice&#39;s screen.</p>

<p>Return the total number of <em>possible</em> original strings that Alice <em>might</em> have intended to type.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;abbcccc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The possible strings are: <code>&quot;abbcccc&quot;</code>, <code>&quot;abbccc&quot;</code>, <code>&quot;abbcc&quot;</code>, <code>&quot;abbc&quot;</code>, and <code>&quot;abcccc&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;abcd&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The only possible string is <code>&quot;abcd&quot;</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;aaaa&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 100</code></li>
	<li><code>word</code> consists only of lowercase English letters.</li>
</ul>

# Approach 
* If a character in word appears consecutively `k` times `(where k>1)`, and Alice makes a mistake in this part, then in the actual original string, this character could have appeared `1,2,…,k−1` times. That is, there are **`k−1`** possible variations.
* For the case  `k=1`, Alice will not make a mistake, so there are `0` possibilities, which is consistent with the formula `k−1`

# Solution 
* We keep track of the consecutive Count for a char in the word, when the consecutivity breaks, we add the count, reset the counter and change the previous char to current char and continue. 

```python
class Solution:
    def possibleStringCount(self, word: str) -> int:
        total = 1
        consecutiveCount = 0
        previousChar = ''

        for i in range(len(word)):
            if word[i] != previousChar:
                total += consecutiveCount
                consecutiveCount = 0
                previousChar = word[i]
            else:
                consecutiveCount += 1
        
        if consecutiveCount:
            total += consecutiveCount
            
        return total
```
---
# Optimal Solution 
```python
class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1

        for i in range(1, len(word)):
            if (word[i] == word[i-1]):
                res += 1
        return res
```
