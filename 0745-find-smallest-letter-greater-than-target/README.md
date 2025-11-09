<h2><a href="https://leetcode.com/problems/find-smallest-letter-greater-than-target">745. Find Smallest Letter Greater Than Target</a></h2><h3>Easy</h3><hr><p>You are given an array of characters <code>letters</code> that is sorted in <strong>non-decreasing order</strong>, and a character <code>target</code>. There are <strong>at least two different</strong> characters in <code>letters</code>.</p>

<p>Return <em>the smallest character in </em><code>letters</code><em> that is lexicographically greater than </em><code>target</code>. If such a character does not exist, return the first character in <code>letters</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> letters = [&quot;c&quot;,&quot;f&quot;,&quot;j&quot;], target = &quot;a&quot;
<strong>Output:</strong> &quot;c&quot;
<strong>Explanation:</strong> The smallest character that is lexicographically greater than &#39;a&#39; in letters is &#39;c&#39;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> letters = [&quot;c&quot;,&quot;f&quot;,&quot;j&quot;], target = &quot;c&quot;
<strong>Output:</strong> &quot;f&quot;
<strong>Explanation:</strong> The smallest character that is lexicographically greater than &#39;c&#39; in letters is &#39;f&#39;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> letters = [&quot;x&quot;,&quot;x&quot;,&quot;y&quot;,&quot;y&quot;], target = &quot;z&quot;
<strong>Output:</strong> &quot;x&quot;
<strong>Explanation:</strong> There are no characters in letters that is lexicographically greater than &#39;z&#39; so we return letters[0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= letters.length &lt;= 10<sup>4</sup></code></li>
	<li><code>letters[i]</code> is a lowercase English letter.</li>
	<li><code>letters</code> is sorted in <strong>non-decreasing</strong> order.</li>
	<li><code>letters</code> contains at least two different characters.</li>
	<li><code>target</code> is a lowercase English letter.</li>
</ul>

# Brute Force Solution 
```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        targetNum = ord(target)

        for c in letters:
            if ord(c) > targetNum:
                return c
        
        return letters[0]
```

# Binary Seach 
* Since the given array if sorted, we can use `binary seach`

**Binary search is a fast search algorithm that works by repeatedly dividing in half the portion of the array that could contain the target. The binary search has two pointers, `l (left)` and `r (right)`, to point to the start and end of the segment of letters we are searching.**

Complexity
Time complexity: O(log(n)) - each time we divide the search space in half. An array of length n can be divided in half at most log(n) times.

Space complexity: O(1)
```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        targetNum = ord(target)
        n = len(letters)
        l, r = 0, n

        while l < r:
            m = (l + r) // 2
            if ord(letters[m]) > targetNum:
                r = m
            else: 
                l = m + 1
        
        return letters[l] if l < n else letters[0]
```
* if the `m` is greater than the target Num, we need to look to the left to see if there is any other possiblity of other things being greater, So we move the `r` pointer to `m`.
* If `m` is less, then that means the character we are looking for is to the right side to `m`, excluding `m`. so `l = m +1`.
* If the result is found, the pointer would have stopped at the exact character which is **Smallest Letter Greater than the Target**, We return the target. 
* But if the target was not found, then the pointer would be out of array lenthg range. 

* Return char is the pointer is range or return the first character. 


