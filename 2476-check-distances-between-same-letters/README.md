<h2><a href="https://leetcode.com/problems/check-distances-between-same-letters/?envType=problem-list-v2&envId=n9iuhemc">2476. Check Distances Between Same Letters</a></h2><h3>Easy</h3><hr><p>You are given a <strong>0-indexed</strong> string <code>s</code> consisting of only lowercase English letters, where each letter in <code>s</code> appears <strong>exactly</strong> <strong>twice</strong>. You are also given a <strong>0-indexed</strong> integer array <code>distance</code> of length <code>26</code>.</p>

<p>Each letter in the alphabet is numbered from <code>0</code> to <code>25</code> (i.e. <code>&#39;a&#39; -&gt; 0</code>, <code>&#39;b&#39; -&gt; 1</code>, <code>&#39;c&#39; -&gt; 2</code>, ... , <code>&#39;z&#39; -&gt; 25</code>).</p>

<p>In a <strong>well-spaced</strong> string, the number of letters between the two occurrences of the <code>i<sup>th</sup></code> letter is <code>distance[i]</code>. If the <code>i<sup>th</sup></code> letter does not appear in <code>s</code>, then <code>distance[i]</code> can be <strong>ignored</strong>.</p>

<p>Return <code>true</code><em> if </em><code>s</code><em> is a <strong>well-spaced</strong> string, otherwise return </em><code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abaccb&quot;, distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
<strong>Output:</strong> true
<strong>Explanation:</strong>
- &#39;a&#39; appears at indices 0 and 2 so it satisfies distance[0] = 1.
- &#39;b&#39; appears at indices 1 and 5 so it satisfies distance[1] = 3.
- &#39;c&#39; appears at indices 3 and 4 so it satisfies distance[2] = 0.
Note that distance[3] = 5, but since &#39;d&#39; does not appear in s, it can be ignored.
Return true because s is a well-spaced string.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aa&quot;, distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
<strong>Output:</strong> false
<strong>Explanation:</strong>
- &#39;a&#39; appears at indices 0 and 1 so there are zero letters between them.
Because distance[0] = 1, s is not a well-spaced string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 52</code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
	<li>Each letter appears in <code>s</code> exactly twice.</li>
	<li><code>distance.length == 26</code></li>
	<li><code>0 &lt;= distance[i] &lt;= 50</code></li>
</ul>

# Solution 
* Make a hashmap to map the char with its distance, to calculate the distance take advantage to fact that each char occures exactly twice. 
* and compare the distance of map and the distance array

```python
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        charDist = {}

        for i, chr in enumerate(s):
            charDist[chr] = i - charDist.get(chr, 0)
        
        for c in charDist:
            if charDist[c] - 1 != distance[ord(c)-97]:
                return False
        
        return True
```

# Optimal Solution 
```python
from collections import defaultdict

class Solution:
    def checkDistances(self, s: str, distances: List[int]) -> bool:
        # Dictionary to keep track of the first occurrence index of each character
        first_occurrence = defaultdict(int)
      
        # Iterate through the string while enumerating, which provides both
        # the index and the character
        for index, char in enumerate(s, 1): # Starting index at 1 for calculation convenience
            # If the character has been seen before and the distance constraint is not met
            if first_occurrence[char] and index - first_occurrence[char] - 1 != distances[ord(char) - ord('a')]:
                return False  # The distance constraint is violated
            # Record the first occurrence index of the character
            first_occurrence[char] = index
          
        # If all characters meet their distance constraints, return True
        return True
```
