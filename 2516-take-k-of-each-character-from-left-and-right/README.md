<h2><a href="https://leetcode.com/problems/take-k-of-each-character-from-left-and-right">2599. Take K of Each Character From Left and Right</a></h2><h3>Medium</h3><hr><p>You are given a string <code>s</code> consisting of the characters <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code> and a non-negative integer <code>k</code>. Each minute, you may take either the <strong>leftmost</strong> character of <code>s</code>, or the <strong>rightmost</strong> character of <code>s</code>.</p>

<p>Return<em> the <strong>minimum</strong> number of minutes needed for you to take <strong>at least</strong> </em><code>k</code><em> of each character, or return </em><code>-1</code><em> if it is not possible to take </em><code>k</code><em> of each character.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aabaaaacaabc&quot;, k = 2
<strong>Output:</strong> 8
<strong>Explanation:</strong> 
Take three characters from the left of s. You now have two &#39;a&#39; characters, and one &#39;b&#39; character.
Take five characters from the right of s. You now have four &#39;a&#39; characters, two &#39;b&#39; characters, and two &#39;c&#39; characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;, k = 1
<strong>Output:</strong> -1
<strong>Explanation:</strong> It is not possible to take one &#39;b&#39; or &#39;c&#39; so return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only the letters <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code>.</li>
	<li><code>0 &lt;= k &lt;= s.length</code></li>
</ul>

# Solution
**'what is the biggest contiguous subsequence I can remove while the remaining is still valid?'**

* Instead of choosing what to take, we choose the largest window to skip.

* Everything outside that window is taken from the ends.

* We maintain counts of characters outside the window.

* The window is valid if outside counts still have at least `k` of each.

* We minimize the number of characters taken.

1. We do a early termination if the remaining characters in the the string are less then `k`
```python
   if remaining['a'] < k or remaining['b'] < k or remaining['c'] < k:
            return -1
```
2. Sliding window, Iteration we start to expand the window to the right by trying to leave out the elements.

```python
for right in range(n):
            remaining[s[right]] -= 1
```
3. But at any stage if the removal violates the valid logic. `The sliding window s[left : right+1] is the middle segment you REMOVE.`
```python
while remaining['a'] < k or remaining['b'] < k or remaining['c'] < k:
			remaining[s[left]] += 1
			left += 1
```
4. The Number for elements to take are. 
```
# Remove the middle 
remove = right - left + 1
valid take part = n - (remove) = n - (right - left + 1)
```

5. Lets assume the worst case the total is `len(s)`
```python
# Valid window → compute characters taken from ends
take_count = left + (n - 1 - right)
answer = min(answer, take_count)
```
---
## Sample Flow

```ini
s = "abacbc", n = 6
k = 1

remaining = {a:2, b:2, c:2}

left = 0, right = 0
remaining = {a:2, b:2, c:2}

1. right = 0 s[right]= 'a'
remaining = {a:1, b:2, c:2}  --> valid 
take = 0 + (6 - 0 - 1) = 5

2. right = 1 s[right]='b'
remaining = {a:1, b:1, c:2} --> valid
take = 0 + (6 - 1 - 1) = 4

3. right=2, s[right] = 'a'
remaining = {a:0, b:1, c:2} --> Invalid
        Shrink window: Left = 0 → character 'a'
				{a:1, b:1, c:2}, 
left = 1
take = 1 + (6 - 2 - 1) = 4

4. right = 3 and s[right] = 'c'
remaining = {a:1, b:1, c:1} --> valid
take = 1 + (6 - 3 - 1) = 3
..
```

```python
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        remaining = Counter(s)

        # If we can't get k of each, impossible
        if remaining['a'] < k or remaining['b'] < k or remaining['c'] < k:
            return -1
        
        left = 0
        answer = n  # worst case: take everything

        for right in range(n):
            remaining[s[right]] -= 1

            # Shrink window while invalid
            while remaining['a'] < k or remaining['b'] < k or remaining['c'] < k:
                remaining[s[left]] += 1
                left += 1

            # Valid window → compute characters taken from ends
            remove = right - left + 1
            take_count = n - remove
            answer = min(answer, take_count)

        return answer
```
