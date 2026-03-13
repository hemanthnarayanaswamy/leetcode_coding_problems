<h2><a href="https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen">3566. Find the Sequence of Strings Appeared on the Screen</a></h2><h3>Medium</h3><hr><p>You are given a string <code>target</code>.</p>

<p>Alice is going to type <code>target</code> on her computer using a special keyboard that has <strong>only two</strong> keys:</p>

<ul>
	<li>Key 1 appends the character <code>&quot;a&quot;</code> to the string on the screen.</li>
	<li>Key 2 changes the <strong>last</strong> character of the string on the screen to its <strong>next</strong> character in the English alphabet. For example, <code>&quot;c&quot;</code> changes to <code>&quot;d&quot;</code> and <code>&quot;z&quot;</code> changes to <code>&quot;a&quot;</code>.</li>
</ul>

<p><strong>Note</strong> that initially there is an <em>empty</em> string <code>&quot;&quot;</code> on the screen, so she can <strong>only</strong> press key 1.</p>

<p>Return a list of <em>all</em> strings that appear on the screen as Alice types <code>target</code>, in the order they appear, using the <strong>minimum</strong> key presses.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">target = &quot;abc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;a&quot;,&quot;aa&quot;,&quot;ab&quot;,&quot;aba&quot;,&quot;abb&quot;,&quot;abc&quot;]</span></p>

<p><strong>Explanation:</strong></p>

<p>The sequence of key presses done by Alice are:</p>

<ul>
	<li>Press key 1, and the string on the screen becomes <code>&quot;a&quot;</code>.</li>
	<li>Press key 1, and the string on the screen becomes <code>&quot;aa&quot;</code>.</li>
	<li>Press key 2, and the string on the screen becomes <code>&quot;ab&quot;</code>.</li>
	<li>Press key 1, and the string on the screen becomes <code>&quot;aba&quot;</code>.</li>
	<li>Press key 2, and the string on the screen becomes <code>&quot;abb&quot;</code>.</li>
	<li>Press key 2, and the string on the screen becomes <code>&quot;abc&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">target = &quot;he&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;d&quot;,&quot;e&quot;,&quot;f&quot;,&quot;g&quot;,&quot;h&quot;,&quot;ha&quot;,&quot;hb&quot;,&quot;hc&quot;,&quot;hd&quot;,&quot;he&quot;]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= target.length &lt;= 400</code></li>
	<li><code>target</code> consists only of lowercase English letters.</li>
</ul>

# Solution
```python
class Solution:
    def stringSequence(self, target: str) -> List[str]:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        res = []
        prev = ''
        
        def subSequence(prev, letter):
            tmp = []
            for i in alphabets:
                tmp.append(prev+i)
                if i == letter:
                    break
            return tmp
        
        for letter in target:
            subArr = subSequence(prev, letter)
            prev += letter
            res.extend(subArr)
        
        return res
```
* You don't need to rebuild `prev` from scratch, it's just the last built string and each new string its just `prev + new_letter`
* Right now, each iteration builds a list of intermediate strings. You only need to output the sequence in order. You don’t need to store intermediate lists.

```python
class Solution:
    def stringSequence(self, target: str) -> List[str]:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        res = []
        prev = ''
        
        for letter in target:
            for i in alphabets:
                res.append(prev+i)
                if i == letter:
                    break
            prev += letter
            
        return res
```
* Instead of `alphabets` string pre defined. You don’t need to loop through the entire alphabet each time. You already know the target letter.You know the alphabet is ordered. You know exactly how many steps you need to take.

```python
class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = []
        prev = ''
        
        for letter in target:
            start = ord('a')
            end = ord(letter)+1
            for i in range(start, end):
                res.append(prev+chr(i))
            prev += letter
            
        return res
```
