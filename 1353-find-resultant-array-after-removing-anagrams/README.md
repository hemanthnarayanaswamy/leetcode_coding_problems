<h2><a href="https://leetcode.com/problems/find-resultant-array-after-removing-anagrams">1353. Find Resultant Array After Removing Anagrams</a></h2><h3>Easy</h3><hr><p>You are given a <strong>0-indexed</strong> string array <code>words</code>, where <code>words[i]</code> consists of lowercase English letters.</p>

<p>In one operation, select any index <code>i</code> such that <code>0 &lt; i &lt; words.length</code> and <code>words[i - 1]</code> and <code>words[i]</code> are <strong>anagrams</strong>, and <strong>delete</strong> <code>words[i]</code> from <code>words</code>. Keep performing this operation as long as you can select an index that satisfies the conditions.</p>

<p>Return <code>words</code> <em>after performing all operations</em>. It can be shown that selecting the indices for each operation in <strong>any</strong> arbitrary order will lead to the same result.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, <code>&quot;dacb&quot;</code> is an anagram of <code>&quot;abdc&quot;</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;abba&quot;,&quot;baba&quot;,&quot;bbaa&quot;,&quot;cd&quot;,&quot;cd&quot;]
<strong>Output:</strong> [&quot;abba&quot;,&quot;cd&quot;]
<strong>Explanation:</strong>
One of the ways we can obtain the resultant array is by using the following operations:
- Since words[2] = &quot;bbaa&quot; and words[1] = &quot;baba&quot; are anagrams, we choose index 2 and delete words[2].
  Now words = [&quot;abba&quot;,&quot;baba&quot;,&quot;cd&quot;,&quot;cd&quot;].
- Since words[1] = &quot;baba&quot; and words[0] = &quot;abba&quot; are anagrams, we choose index 1 and delete words[1].
  Now words = [&quot;abba&quot;,&quot;cd&quot;,&quot;cd&quot;].
- Since words[2] = &quot;cd&quot; and words[1] = &quot;cd&quot; are anagrams, we choose index 2 and delete words[2].
  Now words = [&quot;abba&quot;,&quot;cd&quot;].
We can no longer perform any operations, so [&quot;abba&quot;,&quot;cd&quot;] is the final answer.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;d&quot;,&quot;e&quot;]
<strong>Output:</strong> [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;d&quot;,&quot;e&quot;]
<strong>Explanation:</strong>
No two adjacent strings in words are anagrams of each other, so no operations are performed.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>

# Solution 
* **Use STACK**

```python
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def isAnagram(s1, s2):
            if Counter(s1) == Counter(s2):
                return True
            return False
        
        stack = []
        
        for i in range(len(words)):
            if stack:
                if not isAnagram(stack[-1], words[i]):
                    stack.append(words[i])
            else:
                stack.append(words[i])
        
        return stack
```
---
* No need to compute Counter for `stack[-1]` everytime, we can reuse it. 
* Main issue is cost from Counter allocation and dict equality each step. 
* Avoid using Counter and look for alternative solution. 
```python
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        prev_sig = None
        
        for word in words:
            sig = Counter(word)
            if stack and prev_sig == sig:
                    continue
           
            stack.append(word)
            prev_sig = sig
        
        return stack

```
---
* We sort the characters and then check for the anagram condition, Instead of using the hashMap everything. 
* Complexity: `O(nk log k)` with sorting. We are sorting all words with length `n`. 
```python
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        prev_sig = None
        
        for word in words:
            sig = ''.join(sorted(word))
            if stack and prev_sig == sig:
                    continue
           
            stack.append(word)
            prev_sig = sig
        
        return stack
```
