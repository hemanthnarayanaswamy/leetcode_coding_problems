<h2><a href="https://leetcode.com/problems/count-integers-with-even-digit-sum">2298. Count Integers With Even Digit Sum</a></h2><h3>Easy</h3><hr><p>Given a positive integer <code>num</code>, return <em>the number of positive integers <strong>less than or equal to</strong></em> <code>num</code> <em>whose digit sums are <strong>even</strong></em>.</p>

<p>The <strong>digit sum</strong> of a positive integer is the sum of all its digits.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong>
The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 30
<strong>Output:</strong> 14
<strong>Explanation:</strong>
The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 1000</code></li>
</ul>

# Solution 
```python
class Solution:
    def countEven(self, num: int) -> int:
        count = 0

        for i in range(2, num+1):
            tempSum = 0
            x = i
            if x < 9:
                tempSum += i 
            else:
                while x > 0:
                    tempSum += x % 10
                    x //= 10
            
            if tempSum % 2 == 0:
                count += 1
        
        return count
```

* Learn the seperation of digits from the number algorithm without using the string. 
