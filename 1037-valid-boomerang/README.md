<h2><a href="https://leetcode.com/problems/valid-boomerang/">1115. Valid Boomerang</a></h2><h3>Easy</h3><hr><p>Given an array <code>points</code> where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a point on the <strong>X-Y</strong> plane, return <code>true</code> <em>if these points are a <strong>boomerang</strong></em>.</p>

<p>A <strong>boomerang</strong> is a set of three points that are <strong>all distinct</strong> and <strong>not in a straight line</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> points = [[1,1],[2,3],[3,2]]
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> points = [[1,1],[2,2],[3,3]]
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>points.length == 3</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 100</code></li>
</ul>

# Solution
What question is asking to return if all three points can be joined by a single straight line ( i.e we have to return if the given three points are non-collinear)

**3 points form a boomerang if and only if the triangle formed from them has non-zero area.**

So if three points are non collinear then they form triangle. So all we need to check if the area of the triangle formed is non-zero. If the area is zero it means all three points are collinear.

Suppose the three points are `(x1,y1), (x2,y2), (x3,y3)`.
So area of triangle is given by : `0.5 * [x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)]`

Thus we just need to check the condition if `[x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)] !=0`

`(x2−x1)(y3−y2) != (y2−y1)(x3−x2)`

---

```python
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0][0], points[0][1]
        x2, y2 = points[1][0], points[1][1]
        x3, y3 = points[2][0], points[2][1]

        return (x2 - x1)*(y3 - y2) != (y2 - y1)*(x3 - x2)
```
