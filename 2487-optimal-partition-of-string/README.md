<h2><a href="https://leetcode.com/problems/optimal-partition-of-string">2487. Optimal Partition of String</a></h2><h3>Medium</h3><hr><p>Given a string <code>s</code>, partition the string into one or more <strong>substrings</strong> such that the characters in each substring are <strong>unique</strong>. That is, no letter appears in a single substring more than <strong>once</strong>.</p>

<p>Return <em>the <strong>minimum</strong> number of substrings in such a partition.</em></p>

<p>Note that each character should belong to exactly one substring in a partition.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abacaba&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong>
Two possible partitions are (&quot;a&quot;,&quot;ba&quot;,&quot;cab&quot;,&quot;a&quot;) and (&quot;ab&quot;,&quot;a&quot;,&quot;ca&quot;,&quot;ba&quot;).
It can be shown that 4 is the minimum number of substrings needed.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ssssss&quot;
<strong>Output:</strong> 6
<strong>Explanation:
</strong>The only valid partition is (&quot;s&quot;,&quot;s&quot;,&quot;s&quot;,&quot;s&quot;,&quot;s&quot;,&quot;s&quot;).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only English lowercase letters.</li>
</ul>

# Solution 
* To construct minimum number of substrings in such a partition, we can greedily make each substring as long as possible until we encounter a character that already existed in current substring.

1. Maintain a temp string to hold unique characters and if a repeating character comes up increment the count and reset the temp. 
2. return the total count 

```python
class Solution:
    def partitionString(self, s: str) -> int:
        res = []
        temp = ''

        for c in s:
            if c in temp:
                res.append(temp)
                temp = c
            else:
                temp += c
        
        res.append(temp)
        
        return len(res)
```

# Improved 
* No Need to hold the substrings we only need the count 
* Temp lookup is O(n) use set for O(1) lookup 

```python
class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        temp = set()

        for c in s:
            if c in temp:
                count += 1
                temp.clear()
                temp.add(c)
            else:
                temp.add(c)
        count += 1
        
        return count
```
