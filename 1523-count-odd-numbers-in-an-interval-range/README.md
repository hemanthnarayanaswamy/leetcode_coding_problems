<h2><a href="https://leetcode.com/problems/count-odd-numbers-in-an-interval-range">1630. Count Odd Numbers in an Interval Range</a></h2><h3>Easy</h3><hr><p>Given two non-negative integers <code>low</code> and <code><font face="monospace">high</font></code>. Return the <em>count of odd numbers between </em><code>low</code><em> and </em><code><font face="monospace">high</font></code><em>&nbsp;(inclusive)</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> low = 3, high = 7
<strong>Output:</strong> 3
<b>Explanation: </b>The odd numbers between 3 and 7 are [3,5,7].</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> low = 8, high = 10
<strong>Output:</strong> 1
<b>Explanation: </b>The odd numbers between 8 and 10 are [9].</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= low &lt;= high&nbsp;&lt;= 10^9</code></li>

</ul>

# Brute Force Solution 
```python
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        
        for num in range(low, high+1):
            if num % 2:
                count += 1
        
        return count
```
* `Key Insight:` Instead of checking each number individually, we can use a simple mathematical formula to get the answer directly in constant time.
---
* If both ends are even then the number of odd numbers between them is the formula.
```python
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        lm = low % 2
        hm = high % 2
        count = (high - low) // 2

        if lm == 0 and hm == 0:
            return count
        else:
            return count + 1
```        
```ini
return (high + 1) / 2 - (low / 2);
```
* `(high + 1) / 2` → Counts how many odd numbers are in the range `[0, high]`
* `low / 2` → Counts how many odd numbers are in the range `[0, low-1]`
* Subtract them → Gets the count in `[low, high]`

---
```python
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - (low // 2)
```
