<h2><a href="https://leetcode.com/problems/count-square-sum-triples/description/?envType=daily-question&envId=2025-12-08">2037. Count Square Sum Triples</a></h2><h3>Easy</h3><hr><p>A <strong>square triple</strong> <code>(a,b,c)</code> is a triple where <code>a</code>, <code>b</code>, and <code>c</code> are <strong>integers</strong> and <code>a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup></code>.</p>

<p>Given an integer <code>n</code>, return <em>the number of <strong>square triples</strong> such that </em><code>1 &lt;= a, b, c &lt;= n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 2
<strong>Explanation</strong>: The square triples are (3,4,5) and (4,3,5).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 4
<strong>Explanation</strong>: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 250</code></li>
</ul>

# Python 
* Instread of running three loops, use only 2 loops

```python
class Solution:
    def countTriples(self, n: int) -> int:
        triplesCount = 0

        for a in range(1, n+1):
            for b in range(1, n+1):
                c = int(sqrt(a**2 + b**2))
                if c <= n and c**2 == a**2 + b**2:
                    triplesCount += 1
        
        return triplesCount
```
---
```python
class Solution:
    def countTriples(self, n: int) -> int:
        total = 0
        squares = set([i**2 for i in range(1, n+1)])


        for x in range(1, n+1):
            for y in range(x+1, n+1):
                if x**2 + y**2 in squares: 
                    total += 2 # Here count is 2 because the x and y can be swapped to get other pair (x,y,z), (y,x,z)
        
        return total
```
