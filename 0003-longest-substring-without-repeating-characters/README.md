<h2><a href="https://leetcode.com/problems/longest-substring-without-repeating-characters">3. Longest Substring Without Repeating Characters</a></h2><h3>Medium</h3><hr><p>Given a string <code>s</code>, find the length of the <strong>longest</strong> <span data-keyword="substring-nonempty"><strong>substring</strong></span> without duplicate characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcbb&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;abc&quot;, with the length of 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbbbb&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is &quot;b&quot;, with the length of 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;pwwkew&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is &quot;wke&quot;, with the length of 3.
Notice that the answer must be a substring, &quot;pwke&quot; is a subsequence and not a substring.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>

## Solution Approach 
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_set = set() ## Used a string to store the character 
        count = 0 ## Temp Count 
        max_count = 0
        for char in s:
            if char not in str_set:
                str_set.add(char)
                count += 1
            else:
                str_set.clear()
                str_set.add(char)
                count = 1 
            max_count = max(max_count, count)
        return max_count
```
* Solution Seems to work but the issue is `"dvdf"` answer is 3 but my code is giving 2 as you can simulate. 

* This is the working Solution that uses both the set() and two-pointer technique 
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_set = set() ## To store the unique characters
        count = 0
        max_count = 0
        l, r = 0,0             ## Initialize the pointers 
        while l < len(s) and r < len(s):
            if s[r] not in str_set:   # If character not in set we add and increment the right pointer
                str_set.add(s[r])
                r += 1
                count += 1 # Increase Count 
            else:
                str_set.clear() #3 If the char in the set we clear the set 
                l += 1  ## We Increment the left pointer 
                r = l  ## Bring the Right pointer to the left 
								# To start the Iteration Again 
                count = 0 ## Reset the count
            max_count = max(max_count, count) ## to track the max sub lenght 
        
        return max_count Return that
```
## Improved Solution - Sliding Window
* Our Previous Solution takes a lot of time and there is alot of unwanted steps and storage 
*  If a duplicate is found, `str_set.clear()` is called, and both l and r are reset to the same index., `Better approach`: <b>Instead of clearing everything, we should remove only the leftmost character (l) until the duplicate is removed.</b>
*  The algorithm resets r back to l, which leads to unnecessary re-processing of characters.

```python 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_length = 0
        l = 0

        for r in range(len(s)):           # Expand right pointer
            while s[r] in char_set:      # If duplicate found, shrink from left
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])  # Add new character
            max_length = max(max_length, r - l + 1)  # Update max length
        
        return max_length
```

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_length = 0
        l = 0

        for r in range(len(s)):  # Expand right pointer
            while s[r] in char_set:  # If duplicate found, shrink from left
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])  # Add new character
            sublen =  r - l + 1
            if max_length < sublen:
                max_length = sublen  # Update max length
        
        return max_length
```

