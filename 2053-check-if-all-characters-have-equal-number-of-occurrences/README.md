<h2><a href="https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences">2053. Check if All Characters Have Equal Number of Occurrences</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code>, return <code>true</code><em> if </em><code>s</code><em> is a <strong>good</strong> string, or </em><code>false</code><em> otherwise</em>.</p>

<p>A string <code>s</code> is <strong>good</strong> if <strong>all</strong> the characters that appear in <code>s</code> have the <strong>same</strong> number of occurrences (i.e., the same frequency).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abacbc&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The characters that appear in s are &#39;a&#39;, &#39;b&#39;, and &#39;c&#39;. All characters occur 2 times in s.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaabb&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> The characters that appear in s are &#39;a&#39; and &#39;b&#39;.
&#39;a&#39; occurs 3 times while &#39;b&#39; occurs 2 times, which is not the same number of times.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

## Solution Approach 
* Simple Problem not too complicazted but stuck at apoint not knowing how to compare values among themselves in the dictionary. 

```python 
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # if len(s) % 2 != 0: ## Not required as 
        #     return False   ## Fail for s = "vvvvvvvvvvvvvvvvvvv"
    
        char_freq = Counter(s)  ## using counter to compute the frequency 
        result = set() 

        for char in char_freq:
            result.add(char_freq[char]) ## adding all freq to set to see if they are equal 

        return True if len(result) == 1 else False
```

## Improved my Solution 
* used a variable to store result instead of set
```python
char_freq = Counter(s) ## To get the frequenccy of elements 
        result = 0 ## To store individual occurances

        for char in char_freq:
            if result == 0:
                result = char_freq[char] ## Assign the result with the first occurrence value
            else:
                if result != char_freq[char]: # Retur false if the count is off
                    return False

        return True
```

<B>Optimized Solution </B>

```python
def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for i in s: 
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        all_vals = d.values()
        return len(set(all_vals)) == 1
```
