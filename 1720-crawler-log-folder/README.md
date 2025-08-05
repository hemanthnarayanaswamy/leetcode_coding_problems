<h2><a href="https://leetcode.com/problems/crawler-log-folder">1720. Crawler Log Folder</a></h2><h3>Easy</h3><hr><p>The Leetcode file system keeps a log each time some user performs a <em>change folder</em> operation.</p>

<p>The operations are described below:</p>

<ul>
	<li><code>&quot;../&quot;</code> : Move to the parent folder of the current folder. (If you are already in the main folder, <strong>remain in the same folder</strong>).</li>
	<li><code>&quot;./&quot;</code> : Remain in the same folder.</li>
	<li><code>&quot;x/&quot;</code> : Move to the child folder named <code>x</code> (This folder is <strong>guaranteed to always exist</strong>).</li>
</ul>

<p>You are given a list of strings <code>logs</code> where <code>logs[i]</code> is the operation performed by the user at the <code>i<sup>th</sup></code> step.</p>

<p>The file system starts in the main folder, then the operations in <code>logs</code> are performed.</p>

<p>Return <em>the minimum number of operations needed to go back to the main folder after the change folder operations.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/sample_11_1957.png" style="width: 775px; height: 151px;" /></p>

<pre>
<strong>Input:</strong> logs = [&quot;d1/&quot;,&quot;d2/&quot;,&quot;../&quot;,&quot;d21/&quot;,&quot;./&quot;]
<strong>Output:</strong> 2
<strong>Explanation: </strong>Use this change folder operation &quot;../&quot; 2 times and go back to the main folder.
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/sample_22_1957.png" style="width: 600px; height: 270px;" /></p>

<pre>
<strong>Input:</strong> logs = [&quot;d1/&quot;,&quot;d2/&quot;,&quot;./&quot;,&quot;d3/&quot;,&quot;../&quot;,&quot;d31/&quot;]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> logs = [&quot;d1/&quot;,&quot;../&quot;,&quot;../&quot;,&quot;../&quot;]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= logs.length &lt;= 10<sup>3</sup></code></li>
	<li><code>2 &lt;= logs[i].length &lt;= 10</code></li>
	<li><code>logs[i]</code> contains lowercase English letters, digits, <code>&#39;.&#39;</code>, and <code>&#39;/&#39;</code>.</li>
	<li><code>logs[i]</code> follows the format described in the statement.</li>
	<li>Folder names consist of lowercase English letters and digits.</li>
</ul>

# Solution 
"""
PROBLEM: Calculate minimum operations to return to main folder
- '../' = go to parent folder (up one level)
- './' = stay in current folder (no change)
- 'folder_name/' = go into folder (down one level)

KEY INSIGHTS:
1. We only need to track DEPTH, not actual folder names
2. Can't go above main folder (depth < 0)
3. This is essentially a parentheses matching problem
4. Stack-like behavior but only need counter

OPERATIONS:
'../' → depth-- (but never below 0)
'./' → no change
'folder/' → depth++

ALGORITHM:
1. Initialize depth = 0 (main folder)
2. For each operation:
   - If '../': decrease depth (min 0)
   - If './': ignore
   - Else: increase depth (enter folder)
3. Return final depth

EDGE CASES:
- Multiple '../' when already at main folder
- Only './' operations
- Empty logs array
"""

```python
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0

        for dir in logs:
            if dir == '../':
                if count == 0:
                    continue
                else:
                    count -= 1
            elif dir == './':
                continue
            else:
                count += 1
        
        return count
```

# Improved Solution

```python
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for dir in logs:
            if dir == '../':
                depth = max(0, depth-1)
            elif dir != './':
                depth += 1

        return depth
```
