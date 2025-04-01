<h2><a href="https://leetcode.com/problems/sort-vowels-in-a-string">2887. Sort Vowels in a String</a></h2><h3>Medium</h3><hr><p>Given a <strong>0-indexed</strong> string <code>s</code>, <strong>permute</strong> <code>s</code> to get a new string <code>t</code> such that:</p>

<ul>
	<li>All consonants remain in their original places. More formally, if there is an index <code>i</code> with <code>0 &lt;= i &lt; s.length</code> such that <code>s[i]</code> is a consonant, then <code>t[i] = s[i]</code>.</li>
	<li>The vowels must be sorted in the <strong>nondecreasing</strong> order of their <strong>ASCII</strong> values. More formally, for pairs of indices <code>i</code>, <code>j</code> with <code>0 &lt;= i &lt; j &lt; s.length</code> such that <code>s[i]</code> and <code>s[j]</code> are vowels, then <code>t[i]</code> must not have a higher ASCII value than <code>t[j]</code>.</li>
</ul>

<p>Return <em>the resulting string</em>.</p>

<p>The vowels are <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, and <code>&#39;u&#39;</code>, and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;lEetcOde&quot;
<strong>Output:</strong> &quot;lEOtcede&quot;
<strong>Explanation:</strong> &#39;E&#39;, &#39;O&#39;, and &#39;e&#39; are the vowels in s; &#39;l&#39;, &#39;t&#39;, &#39;c&#39;, and &#39;d&#39; are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;lYmpH&quot;
<strong>Output:</strong> &quot;lYmpH&quot;
<strong>Explanation:</strong> There are no vowels in s (all characters in s are consonants), so we return &quot;lYmpH&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

# Solution Approach 
* Convert the string into List 
* Iterate through the list and store all the vowels in a temp list and mark the vowel places in the s_list
* Sort the Temp List of vowels and 
* Once Again iterate through the List of String List 
* If you detected a marked character then Pop from the temp list of vowels and add to str 
* Returns the joined version of string list 

```python
class Solution:
    def sortVowels(self, s: str) -> str:
        s_vowel = {'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        temp = []
        for i in range(len(s)):
            if s[i].lower() in s_vowel:
                temp.append(s[i])
                s[i] = '*'
        temp.sort()

        for i in range(len(s)-1, -1, -1):
            if s[i] == '*':
                s[i] = temp.pop()
        
        return ''.join(s)
```

## Improved Version
```python
class Solution:
    def sortVowels(self, s: str) -> str:
        s_vowel = {'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        temp = []
        for i in range(len(s)):
            if s[i].lower() in s_vowel:
                temp.append(s[i])
                s[i] = '*'
        temp.sort(reverse=True)

        for i in range(len(s)):
            if s[i] == '*':
                s[i] = temp.pop()
        
        return ''.join(s)
```
```python
class Solution:
    def sortVowels(self, s: str) -> str:
        s_vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        temp = []
        for i in range(len(s)):
            if s[i] in s_vowel:
                temp.append(s[i])
                s[i] = '_'
        temp.sort(reverse=True)

        for i in range(len(s)):
            if s[i] == '_':
                s[i] = temp.pop()
        
        return ''.join(s)
```

## Optimal Solution 
```python
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        count_char = Counter(s)
        s_vowels = []
        for char in count_char.keys():
            if char in vowels:
                s_vowels.append(char)                
                s = s.replace(char, '_')                              
        s_vowels.sort()
        for char in s_vowels:
            s = s.replace('_', char, count_char[char])
        return s
```

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of letters of the&nbsp;English alphabet&nbsp;in <strong>uppercase and lowercase</strong>.</li>
</ul>
