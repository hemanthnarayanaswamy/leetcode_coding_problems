<h2><a href="https://leetcode.com/problems/sort-characters-by-frequency">451. Sort Characters By Frequency</a></h2><h3>Medium</h3><hr><p>Given a string <code>s</code>, sort it in <strong>decreasing order</strong> based on the <strong>frequency</strong> of the characters. The <strong>frequency</strong> of a character is the number of times it appears in the string.</p>

<p>Return <em>the sorted string</em>. If there are multiple answers, return <em>any of them</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;tree&quot;
<strong>Output:</strong> &quot;eert&quot;
<strong>Explanation:</strong> &#39;e&#39; appears twice while &#39;r&#39; and &#39;t&#39; both appear once.
So &#39;e&#39; must appear before both &#39;r&#39; and &#39;t&#39;. Therefore &quot;eetr&quot; is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cccaaa&quot;
<strong>Output:</strong> &quot;aaaccc&quot;
<strong>Explanation:</strong> Both &#39;c&#39; and &#39;a&#39; appear three times, so both &quot;cccaaa&quot; and &quot;aaaccc&quot; are valid answers.
Note that &quot;cacaca&quot; is incorrect, as the same characters must be together.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;Aabb&quot;
<strong>Output:</strong> &quot;bbAa&quot;
<strong>Explanation:</strong> &quot;bbaA&quot; is also a valid answer, but &quot;Aabb&quot; is incorrect.
Note that &#39;A&#39; and &#39;a&#39; are treated as two different characters.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists of uppercase and lowercase English letters and digits.</li>
</ul>

# Approach 
1. Count Frequency
2. Store Frequency Pairs
3. Sort the Pairs
4. Build Result String

```python 
char_freq = Counter(s)    ## Counter the frequency of chracters

sorted_chars = sorted(char_freq.items(), key=lambda item: item[1], reverse=True)
## [('e', 2), ('t', 1), ('r', 1)] 
## Sorting the Tuple 

result = ''
for char, count in sorted_chars: ## iterating the Tuple 
        result += char * count

    return result
```

## Optimal Approach 

```python
def frequencySort(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        char_count = Counter(s)
        
        # Step 2: Sort characters based on their frequency in descending order
        sorted_chars = sorted(char_count, key=char_count.get, reverse=True)
				
				## ['e', 't', 'r'] 

        # Step 3: Build the result string by repeating characters according to their frequency
        result = ''
        for char in sorted_chars:
            result += char * char_count[char]

        return result
```
