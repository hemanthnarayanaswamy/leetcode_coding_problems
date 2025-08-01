<h2><a href="https://leetcode.com/problems/odd-string-difference/?envType=problem-list-v2&envId=n9iuhemc">2547. Odd String Difference</a></h2><h3>Easy</h3><hr><p>You are given an array of equal-length strings <code>words</code>. Assume that the length of each string is <code>n</code>.</p>

<p>Each string <code>words[i]</code> can be converted into a <strong>difference integer array</strong> <code>difference[i]</code> of length <code>n - 1</code> where <code>difference[i][j] = words[i][j+1] - words[i][j]</code> where <code>0 &lt;= j &lt;= n - 2</code>. Note that the difference between two letters is the difference between their <strong>positions</strong> in the alphabet i.e.&nbsp;the position of <code>&#39;a&#39;</code> is <code>0</code>, <code>&#39;b&#39;</code> is <code>1</code>, and <code>&#39;z&#39;</code> is <code>25</code>.</p>

<ul>
	<li>For example, for the string <code>&quot;acb&quot;</code>, the difference integer array is <code>[2 - 0, 1 - 2] = [2, -1]</code>.</li>
</ul>

<p>All the strings in words have the same difference integer array, <strong>except one</strong>. You should find that string.</p>

<p>Return<em> the string in </em><code>words</code><em> that has different <strong>difference integer array</strong>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;adc&quot;,&quot;wzy&quot;,&quot;abc&quot;]
<strong>Output:</strong> &quot;abc&quot;
<strong>Explanation:</strong> 
- The difference integer array of &quot;adc&quot; is [3 - 0, 2 - 3] = [3, -1].
- The difference integer array of &quot;wzy&quot; is [25 - 22, 24 - 25]= [3, -1].
- The difference integer array of &quot;abc&quot; is [1 - 0, 2 - 1] = [1, 1]. 
The odd array out is [1, 1], so we return the corresponding string, &quot;abc&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;aaa&quot;,&quot;bob&quot;,&quot;ccc&quot;,&quot;ddd&quot;]
<strong>Output:</strong> &quot;bob&quot;
<strong>Explanation:</strong> All the integer arrays are [0, 0] except for &quot;bob&quot;, which corresponds to [13, -13].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= words.length &lt;= 100</code></li>
	<li><code>n == words[i].length</code></li>
	<li><code>2 &lt;= n &lt;= 20</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>

# Solution 
* In Python, tuples can be used as keys in dictionaries, while lists cannot, due to a fundamental difference in their mutability and hashability.
```python
# Valid: Tuple as a dictionary key
my_dict = {(1, 2): 'value1', ('a', 'b'): 'value2'}
print(my_dict[(1, 2)])

# Invalid: List as a dictionary key (will raise a TypeError)
# my_dict_invalid = {[1, 2]: 'value'}
```
```python
class Solution:
    def oddString(self, words: List[str]) -> str:
        def get_difference_array(word):
            return tuple(ord(word[i]) - ord(word[i-1]) for i in range(1, len(word)))
        
        diff_map = {}
        
        for word in words:
            diff = get_difference_array(word)
            if diff in diff_map:
                diff_map[diff].append(word)
            else:
                diff_map[diff] = [word]
        
        for words_list in diff_map.values():
            if len(words_list) == 1:
                return words_list[0]
```

# Improved Solution 
```python
class Solution:
    def oddString(self, words: List[str]) -> str:
        def get_difference_array(word):
            return tuple(ord(word[i]) - ord(word[i-1]) for i in range(1, len(word)))
        
        diff_map = {}
        
        for word in words:
            diff = get_difference_array(word)
            if diff in diff_map:
                diff_map[diff].append(word)
            else:
                diff_map[diff] = [word]
        
        for words_list in diff_map.values():
            if len(words_list) == 1:
                return words_list[0]
```

# Optimal Solution 
```python
from collections import defaultdict

class Solution:
    def oddString(self, words: List[str]) -> str:
        diff_count = defaultdict(list)
        
        for word in words:
            diff = tuple(ord(word[i]) - ord(word[i-1]) for i in range(1, len(word)))
            diff_count[diff].append(word)
        
        return next(words[0] for words in diff_count.values() if len(words) == 1)
```

"""
PROBLEM: Find the string with unique difference array among given words

DIFFERENCE ARRAY:
For word "abc": [ord('b')-ord('a'), ord('c')-ord('b')] = [1, 1]
For word "bcd": [ord('c')-ord('b'), ord('d')-ord('c')] = [1, 1]
For word "xyz": [ord('y')-ord('x'), ord('z')-ord('y')] = [1, 1]

KEY INSIGHTS:
1. Calculate difference array for each word: diff[i] = word[i+1] - word[i]
2. Most words will have same difference pattern
3. Exactly one word will have different pattern
4. Use ord() to get ASCII values instead of hardcoded mapping

ALGORITHM APPROACHES:

APPROACH 1 - Hash Map (Your approach):
1. Store difference arrays as keys, words as values
2. Find the key with only one word
TIME: O(n*m) where n=words, m=word_length

APPROACH 2 - Early Exit (Optimal):
1. Check first 3 words to determine common pattern
2. If diffs[0] == diffs[1]: pattern = diffs[0], check if word[2] is odd
3. If diffs[0] == diffs[2]: pattern = diffs[0], return word[1]
4. Else: return word[0]
5. Check remaining words against pattern
TIME: O(m) best case, O(n*m) worst case

EDGE CASES:
- All words same length (guaranteed by problem)
- Exactly one word has different pattern (guaranteed)
"""
