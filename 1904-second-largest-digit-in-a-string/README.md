<h2><a href="https://leetcode.com/problems/second-largest-digit-in-a-string">1904. Second Largest Digit in a String</a></h2><h3>Easy</h3><hr><p>Given an alphanumeric string <code>s</code>, return <em>the <strong>second largest</strong> numerical digit that appears in </em><code>s</code><em>, or </em><code>-1</code><em> if it does not exist</em>.</p>

<p>An <strong>alphanumeric</strong><strong> </strong>string is a string consisting of lowercase English letters and digits.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;dfa12321afd&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abc1111&quot;
<strong>Output:</strong> -1
<strong>Explanation:</strong> The digits that appear in s are [1]. There is no second largest digit. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> consists of only lowercase English letters and digits.</li>
</ul>


# Solution
* create a alphabet string that has all the characters.
* Now create a set of unique intergers from the s
* sort that set into a list, then if the len of the list is more then 1 return the second element else -1.

```python
class Solution:
    def secondHighest(self, s: str) -> int:
        alphabates = 'abcdefghijklmnopqrstuvwxyz'

        nums = set(int(char) for char in s if char not in alphabates)
        nums = sorted(nums, reverse=True)

        if len(nums) > 1:
            return nums[1]
        else:
            return -1
```

# Improved Solution
```python
class Solution:
    def secondHighest(self, s: str) -> int:
        digits = {int(c) for c in s if c.isdigit()}

        if len(digits) < 2:
            return -1
						
        return sorted(digits, reverse=True)[1]
```

## Without Sorting 
```python
class Solution:
    def secondHighest(self, s: str) -> int:
        first = second = -1

        for c in s:
            if c.isdigit():
                d = int(c)
                if d > first:
                    second = first
                    first = d
                elif first > d > second:
                    second = d

        return second
```
