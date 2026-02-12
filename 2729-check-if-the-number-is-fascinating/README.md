<h2><a href="https://leetcode.com/problems/check-if-the-number-is-fascinating">2824. Check if The Number is Fascinating</a></h2><h3>Easy</h3><hr><p>You are given an integer <code>n</code> that consists of exactly <code>3</code> digits.</p>

<p>We call the number <code>n</code> <strong>fascinating</strong> if, after the following modification, the resulting number contains all the digits from <code>1</code> to <code>9</code> <strong>exactly</strong> once and does not contain any <code>0</code>&#39;s:</p>

<ul>
	<li><strong>Concatenate</strong> <code>n</code> with the numbers <code>2 * n</code> and <code>3 * n</code>.</li>
</ul>

<p>Return <code>true</code><em> if </em><code>n</code><em> is fascinating, or </em><code>false</code><em> otherwise</em>.</p>

<p><strong>Concatenating</strong> two numbers means joining them together. For example, the concatenation of <code>121</code> and <code>371</code> is <code>121371</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 192
<strong>Output:</strong> true
<strong>Explanation:</strong> We concatenate the numbers n = 192 and 2 * n = 384 and 3 * n = 576. The resulting number is 192384576. This number contains all the digits from 1 to 9 exactly once.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 100
<strong>Output:</strong> false
<strong>Explanation:</strong> We concatenate the numbers n = 100 and 2 * n = 200 and 3 * n = 300. The resulting number is 100200300. This number does not satisfy any of the conditions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>100 &lt;= n &lt;= 999</code></li>
</ul>

# Solution
```python
class Solution:
    def isFascinating(self, n: int) -> bool:
        n2 = n * 2
        n3 = n * 3
    
        conStr = Counter(str(n) + str(n2) + str(n3))
        print(conStr)
        
        if '0' in conStr or len(conStr) != 9:
            return False
        
        for _, val in conStr.items():
            if val > 1:
                return False
        
        return True
```
---
* The concentrated string will always contain `9 or more` numbers. 
* and In the condition we need to only check, if the number is 0 and any number is repeacted thats it, no need to check is the lenght is `9` because, initally after concentating `n1,n2,n3` we'll have 9 digits, if there is no repeat or no `0`, all 9 nums are unique thats the assumption we are operating under.

```python
class Solution:
    def isFascinating(self, n: int) -> bool:
        n2 = n * 2
        n3 = n * 3
        numsFreq = set()
    
        nums = (str(n) + str(n2) + str(n3))

        for num in nums:
            if num in numsFreq or num == '0':
                return False
            else:
                numsFreq.add(num)
        
        return True
```        
        
        
