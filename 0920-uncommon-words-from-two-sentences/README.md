<h2><a href="https://leetcode.com/problems/uncommon-words-from-two-sentences">920. Uncommon Words from Two Sentences</a></h2><h3>Easy</h3><hr><p>A <strong>sentence</strong> is a string of single-space separated words where each word consists only of lowercase letters.</p>

<p>A word is <strong>uncommon</strong> if it appears exactly once in one of the sentences, and <strong>does not appear</strong> in the other sentence.</p>

<p>Given two <strong>sentences</strong> <code>s1</code> and <code>s2</code>, return <em>a list of all the <strong>uncommon words</strong></em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s1 = &quot;this apple is sweet&quot;, s2 = &quot;this apple is sour&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;sweet&quot;,&quot;sour&quot;]</span></p>

<p><strong>Explanation:</strong></p>

<p>The word <code>&quot;sweet&quot;</code> appears only in <code>s1</code>, while the word <code>&quot;sour&quot;</code> appears only in <code>s2</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s1 = &quot;apple apple&quot;, s2 = &quot;banana&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;banana&quot;]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 200</code></li>
	<li><code>s1</code> and <code>s2</code> consist of lowercase English letters and spaces.</li>
	<li><code>s1</code> and <code>s2</code> do not have leading or trailing spaces.</li>
	<li>All the words in <code>s1</code> and <code>s2</code> are separated by a single space.</li>
</ul>

# Solution 
* Combine the two strings and then check for the counter of words that has only one, don't over complicate things

```python
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        combinedWords = s1.split() + s2.split()
        wordCounts = Counter(combinedWords)

        return [word for word, freq in wordCounts.items() if freq == 1]
```

```python
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        all_words = s1 + s2

        word_count_dict = Counter(all_words)

        res = []
        for word_key in word_count_dict:
            if word_count_dict[word_key] == 1:
                res.append(word_key)

        return res
```
