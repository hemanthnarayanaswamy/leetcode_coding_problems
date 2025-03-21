<h2><a href="https://leetcode.com/problems/shortest-distance-to-a-character">841. Shortest Distance to a Character</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code> and a character <code>c</code> that occurs in <code>s</code>, return <em>an array of integers </em><code>answer</code><em> where </em><code>answer.length == s.length</code><em> and </em><code>answer[i]</code><em> is the <strong>distance</strong> from index </em><code>i</code><em> to the <strong>closest</strong> occurrence of character </em><code>c</code><em> in </em><code>s</code>.</p>

<p>The <strong>distance</strong> between two indices <code>i</code> and <code>j</code> is <code>abs(i - j)</code>, where <code>abs</code> is the absolute value function.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;loveleetcode&quot;, c = &quot;e&quot;
<strong>Output:</strong> [3,2,1,0,1,0,0,1,2,2,1,0]
<strong>Explanation:</strong> The character &#39;e&#39; appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of &#39;e&#39; for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of &#39;e&#39; for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
For index 4, there is a tie between the &#39;e&#39; at index 3 and the &#39;e&#39; at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of &#39;e&#39; for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaab&quot;, c = &quot;b&quot;
<strong>Output:</strong> [3,2,1,0]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s[i]</code> and <code>c</code> are lowercase English letters.</li>
	<li>It is guaranteed that <code>c</code> occurs at least once in <code>s</code>.</li>
</ul>

## Solution Approach 
* Loop once to track all the index of the character 
* Next compute the min difference and append the difference

```python
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = []
        track_index = set()
        n = len(s)

        for i in range(n):
            if s[i] == c:
                track_index.add(i)
        
        for i in range(n):
            diff_val = min(abs(i - x) for x in track_index)
            result.append(diff_val)

        return result
```
## Improved Solution
```python
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [0]*n
        track_index = set()
        

        for i in range(n):
            if s[i] == c:
                track_index.add(i)
        
        for i in range(n):
            if s[i] == c:
                continue
            diff_val = min(abs(i - x) for x in track_index)
            result[i] = diff_val

        return result
```

## Optimal Solution 
```python
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        res = [0] * n
        prev = float("-inf")

        for i in range(n):
            if s[i] == c:
                prev = i
            res[i] = i - prev

        prev = float("inf")

        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            res[i] = min(res[i], prev - i)
        
        return res
```
