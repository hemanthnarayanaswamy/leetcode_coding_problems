<h2><a href="https://leetcode.com/problems/find-the-maximum-achievable-number">2812. Find the Maximum Achievable Number</a></h2><h3>Easy</h3><hr><p>Given two integers, <code>num</code> and <code>t</code>. A <strong>number </strong><code>x</code><strong> </strong>is<strong> achievable</strong> if it can become equal to <code>num</code> after applying the following operation <strong>at most</strong> <code>t</code> times:</p>

<ul>
	<li>Increase or decrease <code>x</code> by <code>1</code>, and <em>simultaneously</em> increase or decrease <code>num</code> by <code>1</code>.</li>
</ul>

<p>Return the <strong>maximum </strong>possible value of <code>x</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = 4, t = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>Apply the following operation once to make the maximum achievable number equal to <code>num</code>:</p>

<ul>
	<li>Decrease the maximum achievable number by 1, and increase <code>num</code> by 1.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">num = 3, t = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<p>Apply the following operation twice to make the maximum achievable number equal to <code>num</code>:</p>

<ul>
	<li>Decrease the maximum achievable number by 1, and increase <code>num</code> by 1.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num, t&nbsp;&lt;= 50</code></li>
</ul>

# Solution 
* The logic is a bit messed up, what you need to done is find the maximum possible initial x value ( what x actually started with )
* But we know that after the k operations the need achievable number `x` which is equal to num after t operations 

```
n = 4, t = 1
If I increase n then n = 5
If I decrease n then n = 3

x - t
x + t 

If I want both x and n to be equal, need to increase n and decrease x so that x can start with maximum value 

if after increment operations n=5 then x=5 because achievable number when n is increased x is decreased so x started at x = 6

n=3, t=2
If I inc rease n in two operations n=5 x is also x=5 but x is decreasced by t so x=7
```

**Formula**
```
x - t = n + t
x = n + 2t
```

```python
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2*t
```
