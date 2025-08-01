<h2><a href="https://leetcode.com/problems/goat-latin/?envType=problem-list-v2&envId=n9iuhemc">851. Goat Latin</a></h2><h3>Easy</h3><hr><p>You are given a string <code>sentence</code> that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.</p>

<p>We would like to convert the sentence to &quot;Goat Latin&quot; (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:</p>

<ul>
	<li>If a word begins with a vowel (<code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, or <code>&#39;u&#39;</code>), append <code>&quot;ma&quot;</code> to the end of the word.

	<ul>
		<li>For example, the word <code>&quot;apple&quot;</code> becomes <code>&quot;applema&quot;</code>.</li>
	</ul>
	</li>
	<li>If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add <code>&quot;ma&quot;</code>.
	<ul>
		<li>For example, the word <code>&quot;goat&quot;</code> becomes <code>&quot;oatgma&quot;</code>.</li>
	</ul>
	</li>
	<li>Add one letter <code>&#39;a&#39;</code> to the end of each word per its word index in the sentence, starting with <code>1</code>.
	<ul>
		<li>For example, the first word gets <code>&quot;a&quot;</code> added to the end, the second word gets <code>&quot;aa&quot;</code> added to the end, and so on.</li>
	</ul>
	</li>
</ul>

<p>Return<em> the final sentence representing the conversion from sentence to Goat Latin</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> sentence = "I speak Goat Latin"
<strong>Output:</strong> "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> sentence = "The quick brown fox jumped over the lazy dog"
<strong>Output:</strong> "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= sentence.length &lt;= 150</code></li>
	<li><code>sentence</code> consists of English letters and spaces.</li>
	<li><code>sentence</code> has no leading or trailing spaces.</li>
	<li>All the words in <code>sentence</code> are separated by a single space.</li>
</ul>

# Solution 
* Similar to the simulation case read the simulation properly and manipulate the string in that way .

```python
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        goatLst = sentence.split()

        for i in range(len(goatLst)):
            if goatLst[i][0] in 'aeiouAEIOU':
                goatLst[i] = goatLst[i] + 'ma' + (i+1) * 'a'
            else:
                goatLst[i] = goatLst[i][1::] + goatLst[i][0] + 'ma' + (i+1) * 'a'

        
        return ' '.join(goatLst)
```

# Optimal Solution
```python
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        if not sentence:
            return ""
        
        res = []
        
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        
        for i, word in enumerate(sentence.split()):
            if word[0] in vowels:
                res.append(word + 'ma' + (i+1) * 'a')
            else:
                res.append(word[1::] + word[0] + 'ma' + (i+1) * 'a')
        
        return " ".join(res)
```
