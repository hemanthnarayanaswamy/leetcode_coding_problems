<h2><a href="https://leetcode.com/problems/buddy-strings">889. Buddy Strings</a></h2><h3>Easy</h3><hr><p>Given two strings <code>s</code> and <code>goal</code>, return <code>true</code><em> if you can swap two letters in </em><code>s</code><em> so the result is equal to </em><code>goal</code><em>, otherwise, return </em><code>false</code><em>.</em></p>

<p>Swapping letters is defined as taking two indices <code>i</code> and <code>j</code> (0-indexed) such that <code>i != j</code> and swapping the characters at <code>s[i]</code> and <code>s[j]</code>.</p>

<ul>
	<li>For example, swapping at indices <code>0</code> and <code>2</code> in <code>&quot;abcd&quot;</code> results in <code>&quot;cbad&quot;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ab&quot;, goal = &quot;ba&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> You can swap s[0] = &#39;a&#39; and s[1] = &#39;b&#39; to get &quot;ba&quot;, which is equal to goal.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ab&quot;, goal = &quot;ab&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> The only letters you can swap are s[0] = &#39;a&#39; and s[1] = &#39;b&#39;, which results in &quot;ba&quot; != goal.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aa&quot;, goal = &quot;aa&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> You can swap s[0] = &#39;a&#39; and s[1] = &#39;a&#39; to get &quot;aa&quot;, which is equal to goal.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, goal.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>goal</code> consist of lowercase letters.</li>
</ul>

# Solution 
* **If length of `s` and length of `goal` aren't equal, return `false`.**
* **If `s == goal` but none of the characters in `S` occur more than once, return `False`, else return `True`.
* **if `s[i] != goals[i]` at more than `2` different places, return `False`.**

1. If length or frequey of chars vary between the 2 strings we terminate the program. 
2. But if two strings are equal, then we check if any characters has a frequency more then `2`, This way we can swap the similar characters and maintain the equality. **It is mandatory to swap the characters**
3. If two strings are different, We check the inequity between two strings can only be at two places which can be fixed by a swap to make them equal. 
```python
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        sn = len(s)
        gn = len(goal)
        sfreq = Counter(s)
        gfreq = Counter(goal)

        if (sn != gn) or (sfreq != gfreq):
            return False
        
        if s == goal:
            for v in sfreq.values():
                if v >= 2:
                    return True
            return False
        
        misMatch = 0
        for c1, c2 in zip(s, goal):
            if c1 != c2:
                misMatch += 1
            
            if misMatch > 2:
                return False
        
        return True
```
---
# Optimal Solution 
```python
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            # need at least one duplicate to allow a no-op swap
            return any(c >= 2 for c in Counter(s).values())

        # collect mismatched positions
        diffs = [(a, b) for a, b in zip(s, goal) if a != b]
        if len(diffs) != 2:
            return False

        (a1, b1), (a2, b2) = diffs
        
        return a1 == b2 and a2 == b1
```
