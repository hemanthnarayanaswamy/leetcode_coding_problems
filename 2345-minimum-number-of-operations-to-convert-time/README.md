<h2><a href="https://leetcode.com/problems/minimum-number-of-operations-to-convert-time">2345. Minimum Number of Operations to Convert Time</a></h2><h3>Easy</h3><hr><p>You are given two strings <code>current</code> and <code>correct</code> representing two <strong>24-hour times</strong>.</p>

<p>24-hour times are formatted as <code>&quot;HH:MM&quot;</code>, where <code>HH</code> is between <code>00</code> and <code>23</code>, and <code>MM</code> is between <code>00</code> and <code>59</code>. The earliest 24-hour time is <code>00:00</code>, and the latest is <code>23:59</code>.</p>

<p>In one operation you can increase the time <code>current</code> by <code>1</code>, <code>5</code>, <code>15</code>, or <code>60</code> minutes. You can perform this operation <strong>any</strong> number of times.</p>

<p>Return <em>the <strong>minimum number of operations</strong> needed to convert </em><code>current</code><em> to </em><code>correct</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> current = &quot;02:30&quot;, correct = &quot;04:35&quot;
<strong>Output:</strong> 3
<strong>Explanation:
</strong>We can convert current to correct in 3 operations as follows:
- Add 60 minutes to current. current becomes &quot;03:30&quot;.
- Add 60 minutes to current. current becomes &quot;04:30&quot;.
- Add 5 minutes to current. current becomes &quot;04:35&quot;.
It can be proven that it is not possible to convert current to correct in fewer than 3 operations.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> current = &quot;11:00&quot;, correct = &quot;11:01&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> We only have to add one minute to current, so the minimum number of operations needed is 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>current</code> and <code>correct</code> are in the format <code>&quot;HH:MM&quot;</code></li>
	<li><code>current &lt;= correct</code></li>
</ul>

# Solution 
* convert the current and correct time into minutes and calculate the difference between them and compute operations to make that difference zero. 

```python
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_minutes = int(current[:2])*60 + int(current[3:])
        corrent_minutes = int(correct[:2])*60 + int(correct[3:])

        totalDiff = corrent_minutes - current_minutes
        totalOperations = 0

        while totalDiff != 0:
            if totalDiff >= 60:
                totalDiff -= 60
            elif 15 <= totalDiff < 60:
                totalDiff -= 15
            elif 5 <= totalDiff < 15:
                totalDiff -= 5
            else:
                totalDiff -= 1
            
            totalOperations += 1

        return totalOperations
```

# Optimal Solution 
```python
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        # 1) Turn “HH:MM” into total minutes
        h1, m1 = map(int, current.split(':'))
        h2, m2 = map(int, correct.split(':'))
        diff = (h2 * 60 + m2) - (h1 * 60 + m1)

        # 2) Greedily use the largest operations first
        ops = 0
        for step in (60, 15, 5, 1):
            ops += diff // step
            diff %= step
            if diff == 0:
                break

        return ops
```
