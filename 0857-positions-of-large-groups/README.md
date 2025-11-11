<h2><a href="https://leetcode.com/problems/positions-of-large-groups">857. Positions of Large Groups</a></h2><h3>Easy</h3><hr><p>In a string <code><font face="monospace">s</font></code>&nbsp;of lowercase letters, these letters form consecutive groups of the same character.</p>

<p>For example, a string like <code>s = &quot;abbxxxxzyy&quot;</code> has the groups <code>&quot;a&quot;</code>, <code>&quot;bb&quot;</code>, <code>&quot;xxxx&quot;</code>, <code>&quot;z&quot;</code>, and&nbsp;<code>&quot;yy&quot;</code>.</p>

<p>A group is identified by an interval&nbsp;<code>[start, end]</code>, where&nbsp;<code>start</code>&nbsp;and&nbsp;<code>end</code>&nbsp;denote the start and end&nbsp;indices (inclusive) of the group. In the above example,&nbsp;<code>&quot;xxxx&quot;</code>&nbsp;has the interval&nbsp;<code>[3,6]</code>.</p>

<p>A group is considered&nbsp;<strong>large</strong>&nbsp;if it has 3 or more characters.</p>

<p>Return&nbsp;<em>the intervals of every <strong>large</strong> group sorted in&nbsp;<strong>increasing order by start index</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abbxxxxzzy&quot;
<strong>Output:</strong> [[3,6]]
<strong>Explanation:</strong> <code>&quot;xxxx&quot; is the only </code>large group with start index 3 and end index 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abc&quot;
<strong>Output:</strong> []
<strong>Explanation:</strong> We have groups &quot;a&quot;, &quot;b&quot;, and &quot;c&quot;, none of which are large groups.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcdddeeeeaabbbcd&quot;
<strong>Output:</strong> [[3,5],[6,9],[12,14]]
<strong>Explanation:</strong> The large groups are &quot;ddd&quot;, &quot;eeee&quot;, and &quot;bbb&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> contains lowercase English letters only.</li>
</ul>

# Solution 
* Track the start and prev element and then if the strek is broken then check if the length is `>= 3`, then appened the start and end & reset `start` and `prev`. 
* If the length `n` is less then 3, terminate early. 
* And If all the elements in the array are same then the condition won't be satified, then we need to check if `start and len(s)`, is `>= 3`
```python
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        n = len(s)
        start = 0
        prev = s[0]

        if n < 3:
            return res

        for i in range(1, n):
            if s[i] != prev:
                if (i - start) >= 3:
                    res.append([start, i-1])
                start = i
                prev = s[i]
        
        if (n - start) >= 3:
            res.append([start, n-1])

        return res
```
---
# Optimal Solution 
* Maintain pointers `i, j with i <= j`. The `i` pointer will represent the start of the current group, and we will increment `j` forward until it reaches the end of the group.
* We know that we have reached the end of the group **when j is at the end of the string**, or `S[j] != S[j+1]`. 
* At this point, we have some group `[i, j]`; and after, we will update `i = j+1`, the start of the next group.
```python
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        n = len(s)
        start = 0
        largeGroup = []

        for i in range(1, n + 1):
            if i == n or s[i] != s[i - 1]:
                if i - start >= 3:
                    largeGroup.append([start, i - 1])
                start = i

        return largeGroup
```
