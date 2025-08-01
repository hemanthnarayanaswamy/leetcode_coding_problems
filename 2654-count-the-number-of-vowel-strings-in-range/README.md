<h2><a href="https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range">2654. Count the Number of Vowel Strings in Range</a></h2><h3>Easy</h3><hr><p>You are given a <strong>0-indexed</strong> array of string <code>words</code> and two integers <code>left</code> and <code>right</code>.</p>

<p>A string is called a <strong>vowel string</strong> if it starts with a vowel character and ends with a vowel character where vowel characters are <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, and <code>&#39;u&#39;</code>.</p>

<p>Return <em>the number of vowel strings </em><code>words[i]</code><em> where </em><code>i</code><em> belongs to the inclusive range </em><code>[left, right]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;are&quot;,&quot;amy&quot;,&quot;u&quot;], left = 0, right = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
- &quot;are&quot; is a vowel string because it starts with &#39;a&#39; and ends with &#39;e&#39;.
- &quot;amy&quot; is not a vowel string because it does not end with a vowel.
- &quot;u&quot; is a vowel string because it starts with &#39;u&#39; and ends with &#39;u&#39;.
The number of vowel strings in the mentioned range is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;hey&quot;,&quot;aeo&quot;,&quot;mu&quot;,&quot;ooo&quot;,&quot;artro&quot;], left = 1, right = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
- &quot;aeo&quot; is a vowel string because it starts with &#39;a&#39; and ends with &#39;o&#39;.
- &quot;mu&quot; is not a vowel string because it does not start with a vowel.
- &quot;ooo&quot; is a vowel string because it starts with &#39;o&#39; and ends with &#39;o&#39;.
- &quot;artro&quot; is a vowel string because it starts with &#39;a&#39; and ends with &#39;o&#39;.
The number of vowel strings in the mentioned range is 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 1000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>words[i]</code> consists of only lowercase English letters.</li>
	<li><code>0 &lt;= left &lt;= right &lt; words.length</code></li>
</ul>

# Solution 
* The problem is straight forward figure out yourself 

```python
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        vowelChars = {'a', 'e', 'i', 'o', 'u'}

        for i in range(left, right+1):
            if words[i][0] in vowelChars and words[i][-1] in vowelChars:
                count += 1
        
        return count
```

* Other solution wihtout using the set to store the vowels 

```python
class Solution:
    def vowelStrings(self, w: List[str], left: int, right: int) -> int:
        ans = 0
        for i in range(left,right+1):
            if w[i][0] in 'aeiou' and w[i][-1] in 'aeiou':
                ans += 1
        return ans
```
