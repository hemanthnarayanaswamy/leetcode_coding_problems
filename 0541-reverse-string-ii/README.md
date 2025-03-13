<h2><a href="https://leetcode.com/problems/reverse-string-ii">541. Reverse String II</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code> and an integer <code>k</code>, reverse the first <code>k</code> characters for every <code>2k</code> characters counting from the start of the string.</p>

<p>If there are fewer than <code>k</code> characters left, reverse all of them. If there are less than <code>2k</code> but greater than or equal to <code>k</code> characters, then reverse the first <code>k</code> characters and leave the other as original.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abcdefg", k = 2
<strong>Output:</strong> "bacdfeg"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abcd", k = 2
<strong>Output:</strong> "bacd"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>

## Question 
`For every group of 2k characters, reverse the first k characters.`

* Example:
"onetwoten", k = 3

1. we take the first group of 2k, or 6 chars: "onetwo"
2. reverse the first k = 3 chars, ignore the next k = 3 chars from this group: "eno" + "two"
3. take the next group of 2k = 6 chars: "ten" (we only have 3 chars left, so take those), reverse the first k = 3 chars of the group: so "ten" becomes "net"
4. result: "eno" + "two" + "net"
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
* Case−I : for every 2 * k characters of that string s reverse the first k characters then go for another 2k chars and reverse the first k chars and go on..
* Case−II : while doing case-i if few chars are left and that chars are not eqaul 2k then if they lie in the range of k to 2k (k included) then reverse the first k chars and dont do anything on other chars.
* Case−III : If there are fewer than k characters left, reverse all of them.

-----------
## Solution Approach 
✅ Process in chunks of `2k`
✅ Use slicing` ([::-1])` for reversing
✅ Modify the string as a list for efficiency
✅ Use `''.join()` to convert the list back to a string

```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = [chr for chr in s]   # s = list(s)                           ## Convert string in List as string is immutable
        for i in range(0, len(s), 2*k):                  ## Iterating with a step count or batch of 2*K
            end_index = min(i+k, len(s))            ## We need to find the end index usually it is i+k if not enough character its len(s)
            s[i:end_index] = s[i:end_index][::-1]  ## Reversing the elements 

        return "".join(s) ## List into String
```      
## Improved Version
```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        for i in range(0,len(s_list),2*k):
            s_list[i:i+k] = reversed(s_list[i:i+k])
        
        return "".join(s_list)
```
## Using Two-Pointer Approach
```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)         # Convert string to list to allow modifications
        n = len(s)

        # Process the string in chunks of 2k
        for i in range(0, n, 2 * k):
            left, right = i, min(i + k - 1, n - 1)  # Two pointers for reversing

            # Reverse first k characters using two-pointer swapping
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)  # Convert list back to string
```
