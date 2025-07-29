<h2><a href="https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii">2293. Minimum Number of Steps to Make Two Strings Anagram II</a></h2><h3>Medium</h3><hr><p>You are given two strings <code>s</code> and <code>t</code>. In one step, you can append <strong>any character</strong> to either <code>s</code> or <code>t</code>.</p>

<p>Return <em>the minimum number of steps to make </em><code>s</code><em> and </em><code>t</code><em> <strong>anagrams</strong> of each other.</em></p>

<p>An <strong>anagram</strong> of a string is a string that contains the same characters with a different (or the same) ordering.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;<strong><u>lee</u></strong>tco<u><strong>de</strong></u>&quot;, t = &quot;co<u><strong>a</strong></u>t<u><strong>s</strong></u>&quot;
<strong>Output:</strong> 7
<strong>Explanation:</strong> 
- In 2 steps, we can append the letters in &quot;as&quot; onto s = &quot;leetcode&quot;, forming s = &quot;leetcode<strong><u>as</u></strong>&quot;.
- In 5 steps, we can append the letters in &quot;leede&quot; onto t = &quot;coats&quot;, forming t = &quot;coats<u><strong>leede</strong></u>&quot;.
&quot;leetcodeas&quot; and &quot;coatsleede&quot; are now anagrams of each other.
We used a total of 2 + 5 = 7 steps.
It can be shown that there is no way to make them anagrams of each other with less than 7 steps.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;night&quot;, t = &quot;thing&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> The given strings are already anagrams of each other. Thus, we do not need any further steps.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>

# Solution 
* Use HashMap for both the strings.
* In the first iterattion use the sMap characters to see how many operations are need to make s same as t. 
```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        operations = 0
        sFreq = Counter(s)
        tFreq = Counter(t)

        for c in sFreq:
            if sFreq[c] < tFreq.get(c, 0):
                operations += tFreq.get(c, 0) - sFreq[c]
            elif c not in tFreq:
                operations += sFreq[c]
        
        for c in tFreq:
            if tFreq[c] < sFreq.get(c, 0):
                operations += sFreq.get(c, 0) - tFreq[c]
            elif c not in sFreq:
                operations += tFreq[c]

        return operations
```

# Optimal Solution 
```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        operations = 0
        sFreq = Counter(s)
        tFreq = Counter(t)

        for i in range(97, 123):
            c = chr(i)
            operations += abs(sFreq.get(c, 0) - tFreq.get(c, 0))
        
        return operations
```

```python
def minsteps(s, t):
    operations = 0
    sFreq = Counter(s)
    tFreq = Counter(t)

    for i in range(97, 123):
        c = chr(i)
        print(c)
        if c in sFreq and c not in tFreq:
            operations += sFreq[c]
        elif c in tFreq and c not in sFreq:
            operations += tFreq[c]
        else:
            operations += abs(sFreq.get(c, 0) - tFreq.get(c, 0))
    
    return operations
```

## Approach
* The goal is to determine the minimum number of steps required to make two strings s and t anagrams of each other. An anagram means both strings have the same characters with the same frequencies.

1. Count the frequency of each character in both strings s and t using Counter.
2. Find the intersection of these two counters, which gives the common characters with their minimum frequencies in both strings.
3. Calculate the sum of the values in the intersection counter, which represents the number of characters that are already correctly aligned to form an anagram.
4. The minimum number of steps required is calculated as the total length of both strings minus twice the sum of the values in the intersection counter. This effectively gives the number of characters that need to be removed or replaced to make the two strings anagrams.
