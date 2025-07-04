<h2><a href="https://leetcode.com/problems/find-indices-of-stable-mountains">3582. Find Indices of Stable Mountains</a></h2><h3>Easy</h3><hr><p>There are <code>n</code> mountains in a row, and each mountain has a height. You are given an integer array <code>height</code> where <code>height[i]</code> represents the height of mountain <code>i</code>, and an integer <code>threshold</code>.</p>

<p>A mountain is called <strong>stable</strong> if the mountain just before it (<strong>if it exists</strong>) has a height <strong>strictly greater</strong> than <code>threshold</code>. <strong>Note</strong> that mountain 0 is <strong>not</strong> stable.</p>

<p>Return an array containing the indices of <em>all</em> <strong>stable</strong> mountains in <strong>any</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">height = [1,2,3,4,5], threshold = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,4]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Mountain 3 is stable because <code>height[2] == 3</code> is greater than <code>threshold == 2</code>.</li>
	<li>Mountain 4 is stable because <code>height[3] == 4</code> is greater than <code>threshold == 2</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">height = [10,1,10,1,10], threshold = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,3]</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">height = [10,1,10,1,10], threshold = 10</span></p>

<p><strong>Output:</strong> <span class="example-io">[]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n == height.length &lt;= 100</code></li>
	<li><code>1 &lt;= height[i] &lt;= 100</code></li>
	<li><code>1 &lt;= threshold &lt;= 100</code></li>
</ul>

# Solution 
* We iterate through each mountain starting from index 1 (since the 0th mountain has no previous mountain).
* For each mountain i, we check if the height of the previous mountain i-1 is strictly greater than the threshold.
* If this condition is met, we consider it stable and add its index to the result array.

```python 
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        res = []

        for i in range(1, len(height)):
            if height[i-1] > threshold:
                res.append(i)
        
        return res
```
