<h2><a href="https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits">2264. Minimum Sum of Four Digit Number After Splitting Digits</a></h2><h3>Easy</h3><hr><p>You are given a <strong>positive</strong> integer <code>num</code> consisting of exactly four digits. Split <code>num</code> into two new integers <code>new1</code> and <code>new2</code> by using the <strong>digits</strong> found in <code>num</code>. <strong>Leading zeros</strong> are allowed in <code>new1</code> and <code>new2</code>, and <strong>all</strong> the digits found in <code>num</code> must be used.</p>

<ul>
	<li>For example, given <code>num = 2932</code>, you have the following digits: two <code>2</code>&#39;s, one <code>9</code> and one <code>3</code>. Some of the possible pairs <code>[new1, new2]</code> are <code>[22, 93]</code>, <code>[23, 92]</code>, <code>[223, 9]</code> and <code>[2, 329]</code>.</li>
</ul>

<p>Return <em>the <strong>minimum</strong> possible sum of </em><code>new1</code><em> and </em><code>new2</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 2932
<strong>Output:</strong> 52
<strong>Explanation:</strong> Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 4009
<strong>Output:</strong> 13
<strong>Explanation:</strong> Some possible pairs [new1, new2] are [0, 49], [490, 0], etc. 
The minimum sum can be obtained by the pair [4, 9]: 4 + 9 = 13.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1000 &lt;= num &lt;= 9999</code></li>
</ul>

# Solution 
* Convert the num in str and then into a sorted list 
* By the problem we know the num range between 1000 and 9999, Only 4 digits 

```python
class Solution:
    def minimumSum(self, num: int) -> int:
        nums = sorted(str(num))
        return int(nums[0]+nums[3]) + int(nums[1]+nums[2])
```

## Without Sorting 
```python
class Solution:
    def minimumSum(self, num: int) -> int:
        l = []
        l = [int(i) for i in str(num)]
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if l[i] > l[j]:
                    l[i],l[j]=l[j],l[i]
        num1=l[0]*10 + l[2]
        num2=l[1]*10 + l[3]
        return num1+num2
```
