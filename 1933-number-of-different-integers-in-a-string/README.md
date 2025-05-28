<h2><a href="https://leetcode.com/problems/number-of-different-integers-in-a-string">1933. Number of Different Integers in a String</a></h2><h3>Easy</h3><hr><p>You are given a string <code>word</code> that consists of digits and lowercase English letters.</p>

<p>You will replace every non-digit character with a space. For example, <code>&quot;a123bc34d8ef34&quot;</code> will become <code>&quot; 123&nbsp; 34 8&nbsp; 34&quot;</code>. Notice that you are left with some integers that are separated by at least one space: <code>&quot;123&quot;</code>, <code>&quot;34&quot;</code>, <code>&quot;8&quot;</code>, and <code>&quot;34&quot;</code>.</p>

<p>Return <em>the number of <strong>different</strong> integers after performing the replacement operations on </em><code>word</code>.</p>

<p>Two integers are considered different if their decimal representations <strong>without any leading zeros</strong> are different.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;a<u>123</u>bc<u>34</u>d<u>8</u>ef<u>34</u>&quot;
<strong>Output:</strong> 3
<strong>Explanation: </strong>The three different integers are &quot;123&quot;, &quot;34&quot;, and &quot;8&quot;. Notice that &quot;34&quot; is only counted once.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;leet<u>1234</u>code<u>234</u>&quot;
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;a<u>1</u>b<u>01</u>c<u>001</u>&quot;
<strong>Output:</strong> 1
<strong>Explanation: </strong>The three integers &quot;1&quot;, &quot;01&quot;, and &quot;001&quot; all represent the same integer because
the leading zeros are ignored when comparing their decimal values.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 1000</code></li>
	<li><code>word</code> consists of digits and lowercase English letters.</li>
</ul>

# Solution 
* First we need to have a flag that check for a continuous numbers. 

1. When the char is num we register the index and turn the flag on. 
2. When the flag is on and the char is not a num, we append the sliced version of the string from the registered index to the current index, and turn the flag off.
3. and when we are at the last index and the flag is turned on we appened that sliced string also 
4. Return the length of the string 

```python
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        digit_index = 0
        digit_found = False
        number_list = set()
        
        for i in range(len(word)):
            if word[i].isdigit() and not digit_found: 
                digit_index = i 
                digit_found = True

            if not word[i].isdigit() and digit_found: 
                number_list.add(int(word[digit_index:i]))
                digit_found = False

            if i == len(word) -1 and digit_found: 
                number_list.add(int(word[digit_index:i+1])) 

        return len(number_list) 
```

# OPtimal Solution 
```python
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        start_idx = 0
        in_digit_sequence = False
        numbers = set()

        for i, char in enumerate(word):
            if char.isdigit():
                if not in_digit_sequence:
                    start_idx = i
                    in_digit_sequence = True
                if i == len(word) - 1:
                    numbers.add(int(word[start_idx:i + 1]))
            else:
                if in_digit_sequence:
                    numbers.add(int(word[start_idx:i]))
                    in_digit_sequence = False

        return len(numbers)
```
