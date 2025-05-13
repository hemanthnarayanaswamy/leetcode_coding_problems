<h2><a href="https://leetcode.com/problems/rearrange-characters-to-make-target-string">2372. Rearrange Characters to Make Target String</a></h2><h3>Easy</h3><hr><p>You are given two <strong>0-indexed</strong> strings <code>s</code> and <code>target</code>. You can take some letters from <code>s</code> and rearrange them to form new strings.</p>

<p>Return<em> the <strong>maximum</strong> number of copies of </em><code>target</code><em> that can be formed by taking letters from </em><code>s</code><em> and rearranging them.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ilovecodingonleetcode&quot;, target = &quot;code&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong>
For the first copy of &quot;code&quot;, take the letters at indices 4, 5, 6, and 7.
For the second copy of &quot;code&quot;, take the letters at indices 17, 18, 19, and 20.
The strings that are formed are &quot;ecod&quot; and &quot;code&quot; which can both be rearranged into &quot;code&quot;.
We can make at most two copies of &quot;code&quot;, so we return 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcba&quot;, target = &quot;abc&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong>
We can make one copy of &quot;abc&quot; by taking the letters at indices 0, 1, and 2.
We can make at most one copy of &quot;abc&quot;, so we return 1.
Note that while there is an extra &#39;a&#39; and &#39;b&#39; at indices 3 and 4, we cannot reuse the letter &#39;c&#39; at index 2, so we cannot make a second copy of &quot;abc&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abbaccaddaeea&quot;, target = &quot;aaaaa&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong>
We can make one copy of &quot;aaaaa&quot; by taking the letters at indices 0, 3, 6, 9, and 12.
We can make at most one copy of &quot;aaaaa&quot;, so we return 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>1 &lt;= target.length &lt;= 10</code></li>
	<li><code>s</code> and <code>target</code> consist of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as <a href="https://leetcode.com/problems/maximum-number-of-balloons/description/" target="_blank"> 1189: Maximum Number of Balloons.</a></p>

# Approach
* freq_s to count occurrences of each character in s.
* freq_t to count occurrences of each character in target.

` For each character in target, calculate how many times it can be formed from s based on its frequency in both freq_s and freq_t.
The limiting factor will be the character with the smallest ratio of freq_s[i] to freq_t[i].`
**Return the minimum value among all ratios as the maximum number of times target can be formed.**

1. Consider each letter one at a time. If there are x occurrences of a letter in s and y occurrences of the same letter in target, how many copies of this letter can we make?
2. We can make floor(x / y) copies of the letter.

```python
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        target = Counter(target)
        s = {k:v for (k, v) in Counter(s).items() if k in target}

        for char in target:
            if char not in s:
                return 0
            else:
                s[char] = (s[char] // target[char])
        
        return min(s.values())
```
