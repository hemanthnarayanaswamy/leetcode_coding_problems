<h2><a href="https://leetcode.com/problems/path-crossing">1619. Path Crossing</a></h2><h3>Easy</h3><hr><p>Given a string <code>path</code>, where <code>path[i] = &#39;N&#39;</code>, <code>&#39;S&#39;</code>, <code>&#39;E&#39;</code> or <code>&#39;W&#39;</code>, each representing moving one unit north, south, east, or west, respectively. You start at the origin <code>(0, 0)</code> on a 2D plane and walk on the path specified by <code>path</code>.</p>

<p>Return <code>true</code> <em>if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited</em>. Return <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/10/screen-shot-2020-06-10-at-123929-pm.png" style="width: 400px; height: 358px;" />
<pre>
<strong>Input:</strong> path = &quot;NES&quot;
<strong>Output:</strong> false 
<strong>Explanation:</strong> Notice that the path doesn&#39;t cross any point more than once.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/06/10/screen-shot-2020-06-10-at-123843-pm.png" style="width: 400px; height: 339px;" />
<pre>
<strong>Input:</strong> path = &quot;NESWW&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> Notice that the path visits the origin twice.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= path.length &lt;= 10<sup>4</sup></code></li>
	<li><code>path[i]</code> is either <code>&#39;N&#39;</code>, <code>&#39;S&#39;</code>, <code>&#39;E&#39;</code>, or <code>&#39;W&#39;</code>.</li>
</ul>

## SOLUTION 
1.  This is my first solution, The only problem here is this code is right is the path comes back to the origin but we want to check if the paths are crossing any point again
2. The solution should track previously visited tracks like history tracking 
```python
def iscrossing(path):
    directions = {'N':(0,1), "E":(1, 0), "S":(0,-1), "W":(-1, 0)}
    x, y = 0 ,0
    for direction in path:
        x += directions[direction][0]
        y += directions[direction][1]
        if x == y == 0:
            return True
    return False
```
3. Final optimal solution 	
```python 
    directions = {'N':(0,1), "E":(1, 0), "S":(0,-1), "W":(-1, 0)} ## Coordinates to follow 
    history = {(0,0),} ## History of coordinates visted 
    x, y = 0 ,0 initial cooridnates 
    for direction in path:
        x += directions[direction][0]
        y += directions[direction][1]
        if (x,y) in history: # checking is the current cooridnate was visted or not 
            return True
        history.add((x,y))
    return False
```
