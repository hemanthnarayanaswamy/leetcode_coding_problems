<h2><a href="https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end">3493. Maximum Number of Operations to Move Ones to the End</a></h2><h3>Medium</h3><hr><p>You are given a <span data-keyword="binary-string">binary string</span> <code>s</code>.</p>

<p>You can perform the following operation on the string <strong>any</strong> number of times:</p>

<ul>
	<li>Choose <strong>any</strong> index <code>i</code> from the string where <code>i + 1 &lt; s.length</code> such that <code>s[i] == &#39;1&#39;</code> and <code>s[i + 1] == &#39;0&#39;</code>.</li>
	<li>Move the character <code>s[i]</code> to the <strong>right</strong> until it reaches the end of the string or another <code>&#39;1&#39;</code>. For example, for <code>s = &quot;010010&quot;</code>, if we choose <code>i = 1</code>, the resulting string will be <code>s = &quot;0<strong><u>001</u></strong>10&quot;</code>.</li>
</ul>

<p>Return the <strong>maximum</strong> number of operations that you can perform.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;1001101&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>We can perform the following operations:</p>

<ul>
	<li>Choose index <code>i = 0</code>. The resulting string is <code>s = &quot;<u><strong>001</strong></u>1101&quot;</code>.</li>
	<li>Choose index <code>i = 4</code>. The resulting string is <code>s = &quot;0011<u><strong>01</strong></u>1&quot;</code>.</li>
	<li>Choose index <code>i = 3</code>. The resulting string is <code>s = &quot;001<strong><u>01</u></strong>11&quot;</code>.</li>
	<li>Choose index <code>i = 2</code>. The resulting string is <code>s = &quot;00<strong><u>01</u></strong>111&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;00111&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>

# Solution 
* We need to keep track of number of ones we encounter on the way while iterating.
* When we encounter zero, we check if the next number `s[i+1] == 1` or if we are at the end of iteration `i = n -1`, if yes then we add the operation to number of ones, **As we are moving all the encounter `1's` to this position which is number of operations**. 
* Scan the string. As we scan, count how many 1s we've seen so far (counted_ones). Every time we start a new zero block (0 after 1), all previous 1s will cross it eventually -> so add counted_ones to the answer.

```python
class Solution:
    def maxOperations(self, s: str) -> int:
        operations = 0
        onesCounter = 0
        n = len(s)

        for i in range(n):
            if s[i] == '1':
                onesCounter += 1
            else:
                if i == n - 1 or s[i+1] == '1':
                    operations += onesCounter 

        return operations
```
---
```python
class Solution:
    def maxOperations(self, s: str) -> int:
        count_one = 0
        ans = 0
        i = 0
        while i < len(s):
            if s[i] == "0":
                while i + 1 < len(s) and s[i + 1] == "0":
                    i += 1
                ans += count_one
            else:
                count_one += 1
            i += 1
        return ans
```
---
# Optimal Solution 
```python
# Solution 
* We need to keep track of number of ones we encounter on the way while iterating.
* When we encounter zero, we check if the next number `s[i+1] == 1` or if we are at the end of iteration `i = n -1`, if yes then we add the operation to number of ones, **As we are moving all the encounter `1's` to this position which is number of operations**. 
* Scan the string. As we scan, count how many 1s we've seen so far (counted_ones). Every time we start a new zero block (0 after 1), all previous 1s will cross it eventually -> so add counted_ones to the answer.

```python
class Solution:
    def maxOperations(self, s: str) -> int:
        operations = 0
        onesCounter = 0
        n = len(s)

        for i in range(n):
            if s[i] == '1':
                onesCounter += 1
            else:
                if i == n - 1 or s[i+1] == '1':
                    operations += onesCounter 

        return operations
```
---
```python
class Solution:
    def maxOperations(self, s: str) -> int:
        count_one = 0
        ans = 0
        i = 0
        while i < len(s):
            if s[i] == "0":
                while i + 1 < len(s) and s[i + 1] == "0":
                    i += 1
                ans += count_one
            else:
                count_one += 1
            i += 1
        return ans
```
---
# Optimal Solution 
```python
class Solution:
    def maxOperations(self, s: str) -> int:
        ones = [len(i) for i in s.split('0') if i]
        
        if not ones:
            return 0
        tot = 0
        ans = 0
        # print(ones[:-1])
        for f in ones[:-1]: # Ignore the last 1
            tot += f
            ans += tot
        if s[-1] == '1':
            return ans
        else:
            tot += ones[-1]
            ans += tot

        return ans
```
* We count the number of ones divided by intermediate zeros.
* We we'll remove the last element of ones.

* We count all the ones, In the iteration and If the last element was `1`, we return the result.
* But If the last element was not `1`, then we need to consider the last batch of `1's` we ignored, add that to
