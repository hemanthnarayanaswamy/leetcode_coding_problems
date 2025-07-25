<h2><a href="https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points">1742. Widest Vertical Area Between Two Points Containing No Points</a></h2><h3>Easy</h3><hr><p>Given <code>n</code> <code>points</code> on a 2D plane where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>, Return<em>&nbsp;the <strong>widest vertical area</strong> between two points such that no points are inside the area.</em></p>

<p>A <strong>vertical area</strong> is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The <strong>widest vertical area</strong> is the one with the maximum width.</p>

<p>Note that points <strong>on the edge</strong> of a vertical area <strong>are not</strong> considered included in the area.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/19/points3.png" style="width: 276px; height: 371px;" />​
<pre>
<strong>Input:</strong> points = [[8,7],[9,9],[7,4],[9,7]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Both the red and the blue area are optimal.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == points.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub>&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>

# Approach 
* We have N points on a 2D plane. The problem is to find the widest vertical area between any two points without having any other point in between. Vertical area implies that the area can have an infinite length over the y-axis. This means that the y-coordinate doesn't affect the result and we shall focus on the distance along the x-axis.
* Therefore, we only need to find the width between every two adjacent points based on x-coordinates and the maximum width among these would be the answer. Note that there can be multiple points with the same x-coordinate but that won't affect the answer as the points on the edges can be included in the area.
* Since the points do not have a specific order, we will need to sort the points in ascending order of x-coordinates first. Then we need to find the difference in x-coordinates between every two neighboring points, and their maximum value is the result we want, as shown in the picture below.

# Solution
```python
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xpoints = sorted(x for x,y in points)
        maxWidth = 0

        for i in range(len(xpoints)-1):
            tempDiff = xpoints[i+1] - xpoints[i]
            if tempDiff > maxWidth:
                maxWidth = tempDiff
        
        return maxWidth
```

# Optimal Solution
```python
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        xs = [p[0] for p in points]

        xs.sort()

        max_width = 0
        for i in range(1, len(xs)):
            width = xs[i] - xs[i - 1]
            if width > max_width:
                max_width = width

        return max_width
```
