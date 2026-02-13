<h2><a href="https://leetcode.com/problems/check-if-it-is-a-straight-line">1349. Check If It Is a Straight Line</a></h2><h3>Easy</h3><hr><p>You are given an integer array&nbsp;<code>coordinates</code>, <code>coordinates[i] = [x, y]</code>, where <code>[x, y]</code> represents the coordinate of a point. Check if these points&nbsp;make a straight line in the XY plane.</p>

<p>&nbsp;</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/10/15/untitled-diagram-2.jpg" style="width: 336px; height: 336px;" /></p>

<pre>
<strong>Input:</strong> coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/10/09/untitled-diagram-1.jpg" style="width: 348px; height: 336px;" /></strong></p>

<pre>
<strong>Input:</strong> coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;=&nbsp;coordinates.length &lt;= 1000</code></li>
	<li><code>coordinates[i].length == 2</code></li>
	<li><code>-10^4 &lt;=&nbsp;coordinates[i][0],&nbsp;coordinates[i][1] &lt;= 10^4</code></li>
	<li><code>coordinates</code>&nbsp;contains no duplicate point.</li>
</ul>

# Solution 
* Slope Formula `(y2-y1)(x1-x0)==(y1-y0)(x2-x1)`, for any three points. 

```python
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, len(coordinates)):
            x2, y2 = coordinates[i]

            if (y2-y1) * (x1-x0) != (y1-y0) * (x2-x1):
                return False
        
        return True
```

- The slope for a line through any 2 points `(x0, y0)` and `(x1, y1)` is `(y1 - y0) / (x1 - x0)`; 
- Therefore, for any given 3 points (denote the 3rd point as (x, y)), if they are in a straight line, **the slopes of the lines from the 3rd point to the 2nd point and the 2nd point to the 1st point must be equal**

`(y - y1) / (x - x1) = (y1 - y0) / (x1 - x0)`

**In order to avoid being divided by 0, `use multiplication form`**

```ini
(x1 - x0) * (y2 - y1) = (x2 - x1) * (y1 - y0)   =>  (y2 - y1) / (x2 - x1) = (y1 - y0) / (x1 - x0)
```
```python
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[: 2]
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False
        return True
```
