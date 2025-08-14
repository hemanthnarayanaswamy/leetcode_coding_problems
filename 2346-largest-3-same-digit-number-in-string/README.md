<h2><a href="https://leetcode.com/problems/largest-3-same-digit-number-in-string">2346. Largest 3-Same-Digit Number in String</a></h2><h3>Easy</h3><hr><p>You are given a string <code>num</code> representing a large integer. An integer is <strong>good</strong> if it meets the following conditions:</p>

<ul>
	<li>It is a <strong>substring</strong> of <code>num</code> with length <code>3</code>.</li>
	<li>It consists of only one unique digit.</li>
</ul>

<p>Return <em>the <strong>maximum good </strong>integer as a <strong>string</strong> or an empty string </em><code>&quot;&quot;</code><em> if no such integer exists</em>.</p>

<p>Note:</p>

<ul>
	<li>A <strong>substring</strong> is a contiguous sequence of characters within a string.</li>
	<li>There may be <strong>leading zeroes</strong> in <code>num</code> or a good integer.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;6<strong><u>777</u></strong>133339&quot;
<strong>Output:</strong> &quot;777&quot;
<strong>Explanation:</strong> There are two distinct good integers: &quot;777&quot; and &quot;333&quot;.
&quot;777&quot; is the largest, so we return &quot;777&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;23<strong><u>000</u></strong>19&quot;
<strong>Output:</strong> &quot;000&quot;
<strong>Explanation:</strong> &quot;000&quot; is the only good integer.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;42352338&quot;
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= num.length &lt;= 1000</code></li>
	<li><code>num</code> only consists of digits.</li>
</ul>

# Optimal Solution 
* Once the match is found we can increment i to end of the match index, 
* Store the result parallely while check for maximum number result. 

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        maxNum = -1
        res = ''

        while i < len(num)-2:
            if num[i] == num[i + 1] == num[i + 2]:
                x = int(num[i])
                if x > maxNum:
                    maxNum = x
                    res = num[i:i+3]
                i += 2
            i += 1
                
        return res
```

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        c = 0
        cur = None
        max_good = -1
        for char in num:
            if char == cur:
                c += 1
                if c == 3 and int(cur) > max_good:
                    max_good = int(cur)
            else:
                cur = char
                c = 1
        if max_good < 0:
            return ""
        return str(max_good) * 3
```

1. Simple Solution but the problem is it returns the first found good integer which might not be the highest good interget
```python 
def largestGoodInteger(self, num: str) -> str:
        for i in range(len(num)):
            if i + 2 < len(num) and num[i] == num[i + 1] == num[i + 2]:
                return num[i]*3

        return ""
```

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_triple = ""
        
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                current_triple = num[i:i + 3]
                if current_triple > max_triple:
                    max_triple = current_triple
        
        return max_triple
```
