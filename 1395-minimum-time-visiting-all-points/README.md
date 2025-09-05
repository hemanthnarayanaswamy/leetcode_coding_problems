<h2><a href="https://leetcode.com/problems/minimum-time-visiting-all-points">1395. Minimum Time Visiting All Points</a></h2><h3>Easy</h3><hr><p>On a 2D plane, there are <code>n</code> points with integer coordinates <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>. Return <em>the <strong>minimum time</strong> in seconds to visit all the points in the order given by </em><code>points</code>.</p>

<p>You can move according to these rules:</p>

<ul>
	<li>In <code>1</code> second, you can either:

	<ul>
		<li>move vertically by one&nbsp;unit,</li>
		<li>move horizontally by one unit, or</li>
		<li>move diagonally <code>sqrt(2)</code> units (in other words, move one unit vertically then one unit horizontally in <code>1</code> second).</li>
	</ul>
	</li>
	<li>You have to visit the points in the same order as they appear in the array.</li>
	<li>You are allowed to pass through points that appear later in the order, but these do not count as visits.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/11/14/1626_example_1.PNG" style="width: 500px; height: 428px;" />
<pre>
<strong>Input:</strong> points = [[1,1],[3,4],[-1,0]]
<strong>Output:</strong> 7
<strong>Explanation: </strong>One optimal path is <strong>[1,1]</strong> -&gt; [2,2] -&gt; [3,3] -&gt; <strong>[3,4] </strong>-&gt; [2,3] -&gt; [1,2] -&gt; [0,1] -&gt; <strong>[-1,0]</strong>   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> points = [[3,2],[-2,2]]
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>points.length == n</code></li>
	<li><code>1 &lt;= n&nbsp;&lt;= 100</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-1000&nbsp;&lt;= points[i][0], points[i][1]&nbsp;&lt;= 1000</code></li>
</ul>

# Solution 
```python
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points)-1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            
            time += max(abs(x2 - x1), abs(y2 - y1))

        return time
```
---
```python
def minTimeToVisitAllPoints(points):
    time = 0
    x, y = points[0]
    for i in range(1, len(points)):
        x1, y1 = points[i]
        
        time += max(abs(x1 - x), abs(y1 - y))
        x, y = x1, y1

    return time
```

### Key Insight: Chebyshev Distance
The minimum time between two points is the **Chebyshev distance** (L∞ metric).

### Mathematical Foundation
For points (x₁, y₁) and (x₂, y₂):
- **Manhattan distance**: `|x₂-x₁| + |y₂-y₁|` (only horizontal/vertical moves)
- **Euclidean distance**: `√[(x₂-x₁)² + (y₂-y₁)²]` (direct line)
- **Chebyshev distance**: `max(|x₂-x₁|, |y₂-y₁|)` (8-directional movement)

### Why Chebyshev Distance Works
```
Example: From (0,0) to (3,2)
- Optimal path: diagonal moves + remaining straight moves
- Move diagonally 2 times: (0,0)→(1,1)→(2,2) 
- Move horizontally 1 time: (2,2)→(3,2)
- Total time: max(3,2) = 3 seconds
```
---
```python
def minTimeToVisitAllPoints(points):
    return sum(max(abs(p2[0] - p1[0]), abs(p2[1] - p1[1])) 
               for p1, p2 in zip(points, points[1:]))
```

```ini
1. **Move diagonally** while possible (reduces both x and y distances)
2. **Move straight** for remaining distance in one direction
3. **Total time = max(horizontal_distance, vertical_distance)**
```
