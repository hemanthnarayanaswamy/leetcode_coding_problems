<h2><a href="https://leetcode.com/problems/string-matching-in-an-array">1524. String Matching in an Array</a></h2><h3>Easy</h3><hr><p>Given an array of string <code>words</code>, return all strings in<em> </em><code>words</code><em> </em>that are a <span data-keyword="substring-nonempty">substring</span> of another word. You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;mass&quot;,&quot;as&quot;,&quot;hero&quot;,&quot;superhero&quot;]
<strong>Output:</strong> [&quot;as&quot;,&quot;hero&quot;]
<strong>Explanation:</strong> &quot;as&quot; is substring of &quot;mass&quot; and &quot;hero&quot; is substring of &quot;superhero&quot;.
[&quot;hero&quot;,&quot;as&quot;] is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;leetcode&quot;,&quot;et&quot;,&quot;code&quot;]
<strong>Output:</strong> [&quot;et&quot;,&quot;code&quot;]
<strong>Explanation:</strong> &quot;et&quot;, &quot;code&quot; are substring of &quot;leetcode&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;blue&quot;,&quot;green&quot;,&quot;bu&quot;]
<strong>Output:</strong> []
<strong>Explanation:</strong> No string of words is substring of another string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 30</code></li>
	<li><code>words[i]</code> contains only lowercase English letters.</li>
	<li>All the strings of <code>words</code> are <strong>unique</strong>.</li>
</ul>

# Brute Force Solution 
* Straight forward approach only need to handle duplicates in the result by using the `set()` instread of `list()`
```python
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.add(words[i])
        
        return list(result)
```

# Improved Solution
* First sort the words in according to the lenght of the words 
* Now run two inner loops, main loop for the word and other loop from next letter to end of array. 
* In the second loop break the loop when the substring is detected to avoid duplicates 
```python
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        # sort ascending by length
        words_sorted = sorted(words, key=len)

        for i, w in enumerate(words_sorted):
            # only check against words longer than w
            for longer in words_sorted[i+1:]:
                if w in longer:
                    res.append(w)  # We can use list because we are breaking the loop whenever the word is detected in one of the other strings, that way there'll be only one occurance of word
                    break        # no need to check other longer words

        return res
```

