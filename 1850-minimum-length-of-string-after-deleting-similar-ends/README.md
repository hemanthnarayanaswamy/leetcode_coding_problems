<h2><a href="https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends">1850. Minimum Length of String After Deleting Similar Ends</a></h2><h3>Medium</h3><hr><p>Given a string <code>s</code> consisting only of characters <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code>. You are asked to apply the following algorithm on the string any number of times:</p>

<ol>
	<li>Pick a <strong>non-empty</strong> prefix from the string <code>s</code> where all the characters in the prefix are equal.</li>
	<li>Pick a <strong>non-empty</strong> suffix from the string <code>s</code> where all the characters in this suffix are equal.</li>
	<li>The prefix and the suffix should not intersect at any index.</li>
	<li>The characters from the prefix and suffix must be the same.</li>
	<li>Delete both the prefix and the suffix.</li>
</ol>

<p>Return <em>the <strong>minimum length</strong> of </em><code>s</code> <em>after performing the above operation any number of times (possibly zero times)</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ca&quot;
<strong>Output:</strong> 2
<strong>Explanation: </strong>You can&#39;t remove any characters, so the string stays as is.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cabaabac&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> An optimal sequence of operations is:
- Take prefix = &quot;c&quot; and suffix = &quot;c&quot; and remove them, s = &quot;abaaba&quot;.
- Take prefix = &quot;a&quot; and suffix = &quot;a&quot; and remove them, s = &quot;baab&quot;.
- Take prefix = &quot;b&quot; and suffix = &quot;b&quot; and remove them, s = &quot;aa&quot;.
- Take prefix = &quot;a&quot; and suffix = &quot;a&quot; and remove them, s = &quot;&quot;.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aabccabba&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> An optimal sequence of operations is:
- Take prefix = &quot;aa&quot; and suffix = &quot;a&quot; and remove them, s = &quot;bccabb&quot;.
- Take prefix = &quot;b&quot; and suffix = &quot;bb&quot; and remove them, s = &quot;cca&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> only consists of characters <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code>.</li>
</ul>


## Solution Approach 
* I have used two-pointer to track the prefix and suffix strings 
```python
def minimumlenght(s):
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:                        ## If not equal return
            return len(s[l:r+1])          ## This thing can be changed
        else:
            while s[l+1] == s[l] and l < r:  ## If they are equal then group the similar prefix
                l += 1
            while s[r-1] == s[r] and r > l:   #3 If they are equal group the similar suffix 
                r -= 1
            l += 1            # If no groups are found increment and decrement the pointers 
            r -= 1

    return len(s[l:r+1])      ## Only return r instead of calculating the length
```

## Improved Solution
```python 
def minimumlenght(s):
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            return r-l+1    ## Calculate the lenght manually using the pointer values 
        else:
            while s[l+1] == s[l] and l < r:  ## Something it throws a out of index error
                l += 1
            while s[r-1] == s[r] and r > l:  ## So check the r > l condition first before the equallity
                r -= 1
            l += 1
            r -= 1

    return r-l+1         ## Calculate the lenght manually using the pointer values 
```

## Optimized Solution
```python
class Solution:
    def minimumLength(self, s: str) -> int:
         l, r = 0, len(s)-1
        while l < r and s[l] == s[r]:  # Check both conditions
            currChar = s[l]    ## Storing the present char
            while l <= r and s[l] == currChar:   ## Computing the prefix lenght
                    l += 1

            while l <= r and s[r] == currChar:    ## Computing the Suffix length
                    r -= 1
        return r - l + 1 ## Return length
```

