<h2><a href="https://leetcode.com/problems/reverse-vowels-of-a-string">345. Reverse Vowels of a String</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code>, reverse only all the vowels in the string and return it.</p>

<p>The vowels are <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, and <code>&#39;u&#39;</code>, and they can appear in both lower and upper cases, more than once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;IceCreAm&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;AceCreIm&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>The vowels in <code>s</code> are <code>[&#39;I&#39;, &#39;e&#39;, &#39;e&#39;, &#39;A&#39;]</code>. On reversing the vowels, s becomes <code>&quot;AceCreIm&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;leetcode&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;leotcede&quot;</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> consist of <strong>printable ASCII</strong> characters.</li>
</ul>


## Solution Approach 
* Two pointer approach swapping if a vowel is detected 
```
def longestpalindrome(s):
    s= list(s)
    vowels = {'a','e','i','o','u'}
    left, right = 0, len(s)-1
    while left < right:
        left_char = s[left]
        right_char = s[right]
        print(left_char, right_char)
        if right_char.lower() in vowels and left_char.lower() in vowels:
            s[left], s[right] = right_char, left_char
            left += 1
            right -= 1
            print(s)
        elif right_char.lower() in vowels and left_char.lower() not in vowels:
            left += 1
        else:
            right -= 1

    return ''.join(s)
```
* Solution can be optimized more to suite the needs 

## Improved Solution
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        s= list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}  # Include uppercase vowels
        left, right = 0, len(s) - 1  # Two pointers

        while left < right:
            while left < right and s[left] not in vowels:  # Move left pointer to next vowel
                left += 1
            while left < right and s[right] not in vowels:  # Move right pointer to previous vowel
                right -= 1

            # Swap vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)  # Convert list back to string
```

## Optimal Solution
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=[i for i in s if i in "aeiouAEIOU"]
        result=[i if i not in "aeiouAEIOU" else vowels.pop() for i in s]
        return "".join(result)
```
