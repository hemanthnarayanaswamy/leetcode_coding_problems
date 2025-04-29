<h2><a href="https://leetcode.com/problems/keyboard-row/?envType=problem-list-v2&envId=array">500. Keyboard Row</a></h2><h3>Easy</h3><hr><p>Given an array of strings <code>words</code>, return <em>the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below</em>.</p>

<p><strong>Note</strong> that the strings are <strong>case-insensitive</strong>, both lowercased and uppercased of the same letter are treated as if they are at the same row.</p>

<p>In the <strong>American keyboard</strong>:</p>

<ul>
	<li>the first row consists of the characters <code>&quot;qwertyuiop&quot;</code>,</li>
	<li>the second row consists of the characters <code>&quot;asdfghjkl&quot;</code>, and</li>
	<li>the third row consists of the characters <code>&quot;zxcvbnm&quot;</code>.</li>
</ul>
<img alt="" src="https://assets.leetcode.com/uploads/2018/10/12/keyboard.png" style="width: 800px; max-width: 600px; height: 267px;" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">words = [&quot;Hello&quot;,&quot;Alaska&quot;,&quot;Dad&quot;,&quot;Peace&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;Alaska&quot;,&quot;Dad&quot;]</span></p>

<p><strong>Explanation:</strong></p>

<p>Both <code>&quot;a&quot;</code> and <code>&quot;A&quot;</code> are in the 2nd row of the American keyboard due to case insensitivity.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">words = [&quot;omk&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[]</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">words = [&quot;adsdf&quot;,&quot;sfd&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;adsdf&quot;,&quot;sfd&quot;]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 20</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> consists of English letters (both lowercase and uppercase).&nbsp;</li>
</ul>

# Solution
* I try to do it, but when I try to remove the word the index will shift and there is a possibility of an element being skipped without undergoing the condition.

```python
###### Wrong Solution ######
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

        for word in words:
            if word[0].lower() in keyboard[0]:
                for i in range(1, len(word)):
                    if word[i] not in keyboard[0]:
                        print(word[i])
                        words.remove(word)
                        break 
            elif word[0].lower() in keyboard[1]:
                for i in range(1, len(word)):
                    if word[i] not in keyboard[1]:
                        print(word[i])
                        words.remove(word)
                        break 
            else:
                for i in range(1, len(word)):
                    if word[i] not in keyboard[2]:
                        print(word[i])
                        words.remove(word)
                        break 
        
        return words
```
*** Correct Solution for the above approach
```python
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiopQWERTYUIOP"
        row2 = "asdfghjklASDFGHJKL"
        row3 = "zxcvbnmZXCVBNM" 
        c = []
        
        for i in words:
            if i[0] in row1:
                for j in range(1, len(i)):
                    if i[j] not in row1:
                        break
                else: 
                    c.append(i)
            elif i[0] in row2:
                for j in range(1, len(i)):
                    if i[j] not in row2:
                        break
                else: 
                    c.append(i)
            elif i[0] in row3:
                for j in range(1, len(i)):
                    if i[j] not in row3:
                        break
                else: 
                    c.append(i)
        
        return c
```

## Optimal Solution
```python
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        res = []
        for word in words:
            lower_word = word.lower()
            if all(char in keyboard[0] for char in lower_word):
                res.append(word)
            elif all(char in keyboard[1] for char in lower_word):
                res.append(word)
            elif all(char in keyboard[2] for char in lower_word):
                res.append(word)
        return res
```
