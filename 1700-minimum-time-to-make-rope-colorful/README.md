<h2><a href="https://leetcode.com/problems/minimum-time-to-make-rope-colorful">1700. Minimum Time to Make Rope Colorful</a></h2><h3>Medium</h3><hr><p>Alice has <code>n</code> balloons arranged on a rope. You are given a <strong>0-indexed</strong> string <code>colors</code> where <code>colors[i]</code> is the color of the <code>i<sup>th</sup></code> balloon.</p>

<p>Alice wants the rope to be <strong>colorful</strong>. She does not want <strong>two consecutive balloons</strong> to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it <strong>colorful</strong>. You are given a <strong>0-indexed</strong> integer array <code>neededTime</code> where <code>neededTime[i]</code> is the time (in seconds) that Bob needs to remove the <code>i<sup>th</sup></code> balloon from the rope.</p>

<p>Return <em>the <strong>minimum time</strong> Bob needs to make the rope <strong>colorful</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/ballon1.jpg" style="width: 404px; height: 243px;" />
<pre>
<strong>Input:</strong> colors = &quot;abaac&quot;, neededTime = [1,2,3,4,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> In the above image, &#39;a&#39; is blue, &#39;b&#39; is red, and &#39;c&#39; is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/balloon2.jpg" style="width: 244px; height: 243px;" />
<pre>
<strong>Input:</strong> colors = &quot;abc&quot;, neededTime = [1,2,3]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The rope is already colorful. Bob does not need to remove any balloons from the rope.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/balloon3.jpg" style="width: 404px; height: 243px;" />
<pre>
<strong>Input:</strong> colors = &quot;aabaa&quot;, neededTime = [1,2,3,4,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == colors.length == neededTime.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= neededTime[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>colors</code> contains only lowercase English letters.</li>
</ul>

# Solution
* Scan left→right keeping: `curr_color`, `run_sum` of needed times in this run
* `run_max` largest time in this run. If next `color == curr_color`: update `run_sum += t`, `run_max = max(run_max, t)`.
**If color changes or at the end: add run_sum - run_max to answer, then reset run_sum = t, run_max = t, curr_color = new color.**
* Final answer is the sum over all runs.

```python
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l, r = 0, 1
        time = 0
        n = len(colors)

        while r < n:
            if colors[l] == colors[r]:
                if neededTime[l] > neededTime[r]:
                    time += neededTime[r]
                    r += 1
                else:
                    time += neededTime[l]
                    l = r
                    r += 1
            else:
                l = r
                r += 1

        return time
```
---
```python
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        prev_color = ''
        prev_max = 0
        
        for c, t in zip(colors, neededTime):
            if c == prev_color:
                total += min(prev_max, t)
                prev_max = max(prev_max, t)
            else:
                prev_color = c
                prev_max = t
        return total
```
---
```python
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        lc = colors[0]
        lm = neededTime[0]
        tt = 0
        for i in range(1, n):
            if lc == colors[i]:
                if lm > neededTime[i]:
                    tt += neededTime[i]
                else:
                    tt += lm
                    lm = neededTime[i]
            else:
                lc = colors[i]
                lm = neededTime[i]
        return tt
```
