<h2><a href="https://leetcode.com/problems/alternating-groups-ii">3483. Alternating Groups II</a></h2><h3>Medium</h3><hr><p>There is a circle of red and blue tiles. You are given an array of integers <code>colors</code> and an integer <code>k</code>. The color of tile <code>i</code> is represented by <code>colors[i]</code>:</p>

<ul>
	<li><code>colors[i] == 0</code> means that tile <code>i</code> is <strong>red</strong>.</li>
	<li><code>colors[i] == 1</code> means that tile <code>i</code> is <strong>blue</strong>.</li>
</ul>

<p>An <strong>alternating</strong> group is every <code>k</code> contiguous tiles in the circle with <strong>alternating</strong> colors (each tile in the group except the first and last one has a different color from its <strong>left</strong> and <strong>right</strong> tiles).</p>

<p>Return the number of <strong>alternating</strong> groups.</p>

<p><strong>Note</strong> that since <code>colors</code> represents a <strong>circle</strong>, the <strong>first</strong> and the <strong>last</strong> tiles are considered to be next to each other.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">colors = [0,1,0,1,0], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p><strong><img alt="" data-darkreader-inline-bgcolor="" data-darkreader-inline-bgimage="" src="https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-183519.png" style="width: 150px; height: 150px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b;" /></strong></p>

<p>Alternating groups:</p>

<p><img alt="" data-darkreader-inline-bgcolor="" data-darkreader-inline-bgimage="" src="https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-182448.png" style="width: 150px; height: 150px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b;" /><img alt="" data-darkreader-inline-bgcolor="" data-darkreader-inline-bgimage="" src="https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-182844.png" style="width: 150px; height: 150px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b;" /><img alt="" data-darkreader-inline-bgcolor="" data-darkreader-inline-bgimage="" src="https://assets.leetcode.com/uploads/2024/05/28/screenshot-2024-05-28-183057.png" style="width: 150px; height: 150px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b;" /></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">colors = [0,1,0,0,1,0,1], k = 6</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p><strong><img alt="" data-darkreader-inline-bgcolor="" data-darkreader-inline-bgimage="" src="https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-183907.png" style="width: 150px; height: 150px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b;" /></strong></p>

<p>Alternating groups:</p>

<p><img alt="" data-darkreader-inline-bgcolor="" data-darkreader-inline-bgimage="" src="https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184128.png" style="width: 150px; height: 150px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b;" /><img alt="" data-darkreader-inline-bgcolor="" data-darkreader-inline-bgimage="" src="https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184240.png" style="width: 150px; height: 150px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b;" /></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">colors = [1,1,0,1], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" data-darkreader-inline-bgcolor="" data-darkreader-inline-bgimage="" src="https://assets.leetcode.com/uploads/2024/06/19/screenshot-2024-05-28-184516.png" style="width: 150px; height: 150px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b;" /></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= colors.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= colors[i] &lt;= 1</code></li>
	<li><code>3 &lt;= k &lt;= colors.length</code></li>
</ul>

# Solution
**There is a clever trick to avoid circular arrays: instead of implementing wrap-around logic, simply append the entire array to end. But for this question is good appending only the first `k-1` elements is sufficient.**

* A key insight is that once a sequence fails to maintain the alternating pattern at a certain index, any longer sequence containing that point is also invalid. 
* This means we don’t need to check every possible starting position separately - we can slide over the array and discard invalid sequences as soon as we encounter a mismatch.

**This is where the Sliding Window technique comes in. Instead of restarting our search at every index, we maintain a moving window of size k, adjusting it as we go. The moment we detect a mismatch, we move the window forward without unnecessary checks, making the solution much more efficient. Since each tile is processed at most once, the time complexity is reduced to `O(n)`, making this approach suitable for larger inputs.**

1. We use a `start` variable to track the start of the window at idx `0` and other variable `i` to check the alternativity of the array at `1`
2. We use the while loop to iteration `i < len(colors)`
3. In each iteration we check the alternativity using this condition `if colors[i] != colors[i-1]`, If the condition is `true` we can keep expanding the window.
4. We check the length of subarray `>=k` we don't need to shrink the window size because if its greater then `k` its still satifies the condition we only need to do the count.
5. If the alternativity breaks then we reset the window `start` to i and continue to loop 

```python
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k-1])
        start = 0
        i = 1
        res = 0

        while i < len(colors):
            if colors[i] != colors[i-1]:
                if i - start + 1 >= k:
                    res += 1
            else:
                start = i
            i += 1
        
        return res
```

---

```python
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors +=colors[:k-1]
        n=len(colors)
        subLen=1
        ans=0

        for i in range(1,n):
            if colors[i] != colors[i-1]:
                subLen += 1
            else:
                subLen = 1

            if subLen >= k:
                ans+=1
                
        return ans
```

