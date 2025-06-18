<h2><a href="https://leetcode.com/problems/circular-sentence/">2580. Circular Sentence</a></h2><h3>Easy</h3><hr><p>A <strong>sentence</strong> is a list of words that are separated by a<strong> single</strong> space with no leading or trailing spaces.</p>

<ul>
	<li>For example, <code>&quot;Hello World&quot;</code>, <code>&quot;HELLO&quot;</code>, <code>&quot;hello world hello world&quot;</code> are all sentences.</li>
</ul>

<p>Words consist of <strong>only</strong> uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.</p>

<p>A sentence is <strong>circular </strong>if:</p>

<ul>
	<li>The last character of each word in the sentence is equal to the first character of its next word.</li>
	<li>The last character of the last word is equal to the first character of the first word.</li>
</ul>

<p>For example, <code>&quot;leetcode exercises sound delightful&quot;</code>, <code>&quot;eetcode&quot;</code>, <code>&quot;leetcode eats soul&quot; </code>are all circular sentences. However, <code>&quot;Leetcode is cool&quot;</code>, <code>&quot;happy Leetcode&quot;</code>, <code>&quot;Leetcode&quot;</code> and <code>&quot;I like Leetcode&quot;</code> are <strong>not</strong> circular sentences.</p>

<p>Given a string <code>sentence</code>, return <code>true</code><em> if it is circular</em>. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> sentence = &quot;leetcode exercises sound delightful&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The words in sentence are [&quot;leetcode&quot;, &quot;exercises&quot;, &quot;sound&quot;, &quot;delightful&quot;].
- leetcod<u>e</u>&#39;s&nbsp;last character is equal to <u>e</u>xercises&#39;s first character.
- exercise<u>s</u>&#39;s&nbsp;last character is equal to <u>s</u>ound&#39;s first character.
- soun<u>d</u>&#39;s&nbsp;last character is equal to <u>d</u>elightful&#39;s first character.
- delightfu<u>l</u>&#39;s&nbsp;last character is equal to <u>l</u>eetcode&#39;s first character.
The sentence is circular.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> sentence = &quot;eetcode&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The words in sentence are [&quot;eetcode&quot;].
- eetcod<u>e</u>&#39;s&nbsp;last character is equal to <u>e</u>etcode&#39;s first character.
The sentence is circular.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> sentence = &quot;Leetcode is cool&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> The words in sentence are [&quot;Leetcode&quot;, &quot;is&quot;, &quot;cool&quot;].
- Leetcod<u>e</u>&#39;s&nbsp;last character is <strong>not</strong> equal to <u>i</u>s&#39;s first character.
The sentence is <strong>not</strong> circular.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= sentence.length &lt;= 500</code></li>
	<li><code>sentence</code> consist of only lowercase and uppercase English letters and spaces.</li>
	<li>The words in <code>sentence</code> are separated by a single space.</li>
	<li>There are no leading or trailing spaces.</li>
</ul>

# Solution 
```python
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        n = len(sentence)

        if n == 1: # Edge case to check if the one len string is circular 
            return sentence[0][0] == sentence[0][-1]
        
        for i in range(n-1): # Here we are not check circularity between the last char and first char
                if sentence[i][-1] != sentence[i+1][0]: 
                    return False
        
        return sentence[n-1][-1] == sentence[0][0] # Final check between last and first char circularity 
```
* Here is the solution where we can use the string version directly without splitting into the list. 

```python
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # first and last character must match
        if sentence[0] != sentence[-1]:
            return False

        # for every space in the sentence, the char before it must equal the char after it
        for i, ch in enumerate(sentence):
            if ch == ' ': # We only proceed when we detect the space seperation between two words 
                if sentence[i-1] != sentence[i+1]: # Then check chars before and after space
                    return False

        return True
```
