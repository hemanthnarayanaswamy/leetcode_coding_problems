<h2><a href="https://leetcode.com/problems/largest-triangle-area">830. Largest Triangle Area</a></h2><h3>Easy</h3><hr><p>Given an array of points on the <strong>X-Y</strong> plane <code>points</code> where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>, return <em>the area of the largest triangle that can be formed by any three different points</em>. Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png" style="height: 369px; width: 450px;" />
<pre>
<strong>Input:</strong> points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
<strong>Output:</strong> 2.00000
<strong>Explanation:</strong> The five points are shown in the above figure. The red triangle is the largest.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> points = [[1,0],[0,0],[0,1]]
<strong>Output:</strong> 0.50000
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= points.length &lt;= 50</code></li>
	<li><code>-50 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 50</code></li>
	<li>All the given points are <strong>unique</strong>.</li>
</ul>

# Solution
```python
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxArea = 0
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j]
                for k in range(n):
                    if k == j or k == i:
                        continue 
                    x3, y3 = points[k]
                    
                    area = 0.5 * abs((x1 * (y2 - y3))+(x2 * (y3 - y1))+(x3 * (y1 - y2)))
                    if area > maxArea:
                        maxArea = area
        
        return maxArea
```
---
```python
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxArea = 0
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                for k in range(j+1, n):
                    x3, y3 = points[k]
                    area = abs((x1 * (y2 - y3))+(x2 * (y3 - y1))+(x3 * (y1 - y2)))
                    if area > maxArea:
                        maxArea = area
        
        return maxArea * 0.5
```
---
```python
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        
        maxArea = 0.0
        n = len(points)

        
        for i in range(n-2):
            for j in range(i + 1, n-1): 
                for k in range(j + 1, n):
                    current_area = area(points[i], points[j], points[k])
                    if current_area > maxArea:
                        maxArea = current_area
    
        return maxArea
```
