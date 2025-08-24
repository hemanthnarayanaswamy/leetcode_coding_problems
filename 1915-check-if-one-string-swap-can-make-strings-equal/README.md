<h2><a href="https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal">1915. Check if One String Swap Can Make Strings Equal</a></h2><h3>Easy</h3><hr><p>You are given two strings <code>s1</code> and <code>s2</code> of equal length. A <strong>string swap</strong> is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.</p>

<p>Return <code>true</code> <em>if it is possible to make both strings equal by performing <strong>at most one string swap </strong>on <strong>exactly one</strong> of the strings. </em>Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;bank&quot;, s2 = &quot;kanb&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> For example, swap the first character with the last character of s2 to make &quot;bank&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;attack&quot;, s2 = &quot;defend&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to make them equal with one string swap.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;kelb&quot;, s2 = &quot;kelb&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> The two strings are already equal, so no string swap operation is required.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length &lt;= 100</code></li>
	<li><code>s1.length == s2.length</code></li>
	<li><code>s1</code> and <code>s2</code> consist of only lowercase English letters.</li>
</ul>

# Solution 
* If one swap if allowed that means the two strings can have 2 characters mismatched, but the frequency of all the elements between 2 strings should be the same and also the lenght of two strings should also be the same. 

```python
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2): # If the frequency of the elments are different return False
            return False

        swapCorrections = 2 # If frequency if same we compare the strings by allowing 2 mismatch of characters for the strings. 
        for c1,c2 in zip(s1, s2):
            if c1 != c2:
                swapCorrections -= 1
        
        return False if swapCorrections < 0 else True 
				# Return False if there are more mismatches else True
```
---
# Optimal Solution 

### Algorithm

1. Initialize `firstIndexDiff`, `secondIndexDiff`, and `numDiffs` all to 0.
2. Iterate through the characters of s1 and s2:
 - Let `s1Char` and `s2Char` be the current characters of `s1` and `s2` at index `i`, respectively.
- If `s1Char != s2Char`:
* Increment `numDiffs`.
* If numDiffs is now greater than 2, then we know one string swap will not make the strings equal, so return false.
* If numDiffs is now equal to 1, then we have found our first difference: assign `firstIndexDiff = i`.
* Otherwise, numDiffs is 2 so we have found our second difference: assign `secondIndexDiff = i`.
3. Return `s1[firstIndexDiff] == s2[secondIndexDiff] && s1[secondIndexDiff] == s2[firstIndexDiff]`


```python
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first_index_diff = 0
        second_index_diff = 0
        num_diffs = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                num_diffs += 1
                # num_diffs is more than 2, one string swap will not make two strings equal
                if num_diffs > 2:
                    return False
                elif num_diffs == 1:
                    # store the index of first difference
                    first_index_diff = i
                else:
                    # store the index of second difference
                    second_index_diff = i
        # check if swap is possible
        return (
            s1[first_index_diff] == s2[second_index_diff]
            and s1[second_index_diff] == s2[first_index_diff]
        )
```
