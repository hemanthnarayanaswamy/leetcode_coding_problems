<h2><a href="https://leetcode.com/problems/calculate-money-in-leetcode-bank">1817. Calculate Money in Leetcode Bank</a></h2><h3>Easy</h3><hr><p>Hercy wants to save money for his first car. He puts money in the Leetcode&nbsp;bank <strong>every day</strong>.</p>

<p>He starts by putting in <code>$1</code> on Monday, the first day. Every day from Tuesday to Sunday, he will put in <code>$1</code> more than the day before. On every subsequent Monday, he will put in <code>$1</code> more than the <strong>previous Monday</strong>.<span style="display: none;"> </span></p>

<p>Given <code>n</code>, return <em>the total amount of money he will have in the Leetcode bank at the end of the </em><code>n<sup>th</sup></code><em> day.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 10
<strong>Explanation:</strong>&nbsp;After the 4<sup>th</sup> day, the total is 1 + 2 + 3 + 4 = 10.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 37
<strong>Explanation:</strong>&nbsp;After the 10<sup>th</sup> day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2<sup>nd</sup> Monday, Hercy only puts in $2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 20
<strong>Output:</strong> 96
<strong>Explanation:</strong>&nbsp;After the 20<sup>th</sup> day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>

# Solution 
* Simulation Processes 

```python
class Solution:
    def totalMoney(self, n: int) -> int:
        startMoney = 1
        money = 1
        dayOfWeek = 0
        totalMoney = 0
        totalDays = 0

        while totalDays < n:
            totalMoney += money
            dayOfWeek += 1
            totalDays += 1
            money += 1

            if dayOfWeek == 7:
                dayOfWeek = 0
                startMoney += 1
                money = startMoney
        
        return totalMoney
```
---
# Optimal Solution
* Week `i` (0-indexed) deposits: `(1+i),(2+i),…,(7+i)`.
* After `w`full weeks and `r` leftover days: `n = 7w + r, 0 ≤ r < 7`.

* Week `i` `total = (1+…+7) + 7i = 28 + 7i` because 1+…+7 = 28.
* Weekly totals form an `AP: 28, 35, 42, …` with difference 7.

```ini
Sum over i = 0…w−1:

AP formula: w * (first + last) / 2 = w * (28 + (28+7(w−1))) / 2.

Simplify to 28w + 7 * w(w−1)/2.

Equivalent closed form often used: 7 * w(w+1)/2 + 21w. Same value.
```

```ini
Leftover r days:

First leftover deposit = 1 + w (next Monday).

r terms increasing by 1: (1+w),(2+w),…,(w+r).

Sum = r * (first + last) / 2 = r * ((1+w) + (w+r)) / 2 = r * (2w + r + 1) / 2.
```

```ini
Total:

total = [full weeks sum] + [leftover sum]

= [28w + 7*w(w−1)/2] + [r * (2w + r + 1) / 2]

Same as 7 * w(w+1)/2 + 21w + r * (2w + r + 1) / 2.
```

```ini
n=10 → w=1, r=3.

Full weeks: 28.

Leftover: 3 * (2*1 + 3 + 1) / 2 = 3 * 6 / 2 = 9.

Total = 37
```

```python
class Solution:
    def totalMoney(self, n: int) -> int:
        fullWeeks = n // 7
        leftDays = n % 7
        totalMoney = 0

        for i in range(fullWeeks): # Using AP to calculate the amount for the fullweeks
            totalMoney += 7 * (1 + i) + 21
        
        # calculate amount for remaining weeks
        f = 1+fullWeeks
        l = f+leftDays-1 

        totalMoney += leftDays * (f + l)//2
        
        return totalMoney
```
