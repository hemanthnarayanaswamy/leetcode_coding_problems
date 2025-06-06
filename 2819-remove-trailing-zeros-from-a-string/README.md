<h2><a href="https://leetcode.com/problems/remove-trailing-zeros-from-a-string">2819. Remove Trailing Zeros From a String</a></h2><h3>Easy</h3><hr><p>Given a <strong>positive</strong> integer <code>num</code> represented as a string, return <em>the integer </em><code>num</code><em> without trailing zeros as a string</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;51230100&quot;
<strong>Output:</strong> &quot;512301&quot;
<strong>Explanation:</strong> Integer &quot;51230100&quot; has 2 trailing zeros, we remove them and return integer &quot;512301&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;123&quot;
<strong>Output:</strong> &quot;123&quot;
<strong>Explanation:</strong> Integer &quot;123&quot; has no trailing zeros, we return integer &quot;123&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 1000</code></li>
	<li><code>num</code> consists&nbsp;of only digits.</li>
	<li><code>num</code> doesn&#39;t&nbsp;have any leading zeros.</li>
</ul>


# Solution 
* Its tricky solution if you want to convert it to int and play with it here is the solution

```python
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        numAns = str(int(num[::-1]))

        return numAns[::-1]
```
# Improved Solution
```python
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        if num[-1] == '0':
            return str(int(num[::-1]))[::-1]
        else:
            return num
```

# Optimal Solution
```python
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        idx = len(num)
        for i in range(len(num) - 1, -1 , -1):
            if num[i] == '0':
                continue
            else:
                idx = i + 1
                break
        return num[:idx]
```
