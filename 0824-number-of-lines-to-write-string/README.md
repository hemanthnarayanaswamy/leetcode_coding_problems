<h2><a href="https://leetcode.com/problems/number-of-lines-to-write-string">824. Number of Lines To Write String</a></h2><h3>Easy</h3><hr><p>You are given a string <code>s</code> of lowercase English letters and an array <code>widths</code> denoting <strong>how many pixels wide</strong> each lowercase English letter is. Specifically, <code>widths[0]</code> is the width of <code>&#39;a&#39;</code>, <code>widths[1]</code> is the width of <code>&#39;b&#39;</code>, and so on.</p>

<p>You are trying to write <code>s</code> across several lines, where <strong>each line is no longer than </strong><code>100</code><strong> pixels</strong>. Starting at the beginning of <code>s</code>, write as many letters on the first line such that the total width does not exceed <code>100</code> pixels. Then, from where you stopped in <code>s</code>, continue writing as many letters as you can on the second line. Continue this process until you have written all of <code>s</code>.</p>

<p>Return <em>an array </em><code>result</code><em> of length 2 where:</em></p>

<ul>
	<li><code>result[0]</code><em> is the total number of lines.</em></li>
	<li><code>result[1]</code><em> is the width of the last line in pixels.</em></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = &quot;abcdefghijklmnopqrstuvwxyz&quot;
<strong>Output:</strong> [3,60]
<strong>Explanation:</strong> You can write s as follows:
abcdefghij  // 100 pixels wide
klmnopqrst  // 100 pixels wide
uvwxyz      // 60 pixels wide
There are a total of 3 lines, and the last line is 60 pixels wide.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = &quot;bbbcccdddaaa&quot;
<strong>Output:</strong> [2,4]
<strong>Explanation:</strong> You can write s as follows:
bbbcccdddaa  // 98 pixels wide
a            // 4 pixels wide
There are a total of 2 lines, and the last line is 4 pixels wide.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>widths.length == 26</code></li>
	<li><code>2 &lt;= widths[i] &lt;= 10</code></li>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>

# Solution 
* Two variables totalLine to track the number of lines and it starts from line one by default not zero. 
* Now get the width of the character for each iteration and check the size exceeds 100
* If it exceeds 100 move to the next line and add the maxWidth with the current width character. 
```python
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        totalLines, maxWidth = 1, 0

        for i in range(len(s)):
            charWidth = widths[ord(s[i]) - 97]
            if maxWidth + charWidth > 100:
                totalLines += 1
                maxWidth = charWidth
            else:
                maxWidth += charWidth
        
        return [totalLines, maxWidth]
```

# Improved Solution 
```python
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        lines, total = 1, 0
        L = []
        for c in s:
            total += widths[ord(c) - ord('a')]
            
            if total > 100:
                lines += 1
                total = widths[ord(c) - ord('a')]

        L.append(lines)
        L.append(total)

        return L
```
