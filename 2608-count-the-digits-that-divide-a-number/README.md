<h2><a href="https://leetcode.com/problems/count-the-digits-that-divide-a-number">2608. Count the Digits That Divide a Number</a></h2><h3>Easy</h3><hr><p>Given an integer <code>num</code>, return <em>the number of digits in <code>num</code> that divide </em><code>num</code>.</p>

<p>An integer <code>val</code> divides <code>nums</code> if <code>nums % val == 0</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 7
<strong>Output:</strong> 1
<strong>Explanation:</strong> 7 divides itself, hence the answer is 1.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 121
<strong>Output:</strong> 2
<strong>Explanation:</strong> 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = 1248
<strong>Output:</strong> 4
<strong>Explanation:</strong> 1248 is divisible by all of its digits, hence the answer is 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10<sup>9</sup></code></li>
	<li><code>num</code> does not contain <code>0</code> as one of its digits.</li>
</ul>

** Read Question properly before answering 

# Solution 
* split and save the numbers in the list while converting them to int. 
* a formal for loop to check the divide condition one by one. 

```python
class Solution:
    def countDigits(self, num: int) -> int:
        numList = [int(n) for n in str(num)]
        count = 0

        for n in numList:
            if num % n == 0:
                count += 1
        
        return count
```
# Optimal Solution 
```python
class Solution:
    def countDigits(self, num: int) -> int:
        temp=num
        count=0
        while(num>0):
            rem=num%10
            if(temp%rem==0):
                count+=1
            num//=10
        return count
        
```
