<h2><a href="https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/">2005. Check if All the Integers in a Range Are Covered</a></h2><h3>Easy</h3><hr><p>You are given a 2D integer array <code>ranges</code> and two integers <code>left</code> and <code>right</code>. Each <code>ranges[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> represents an <strong>inclusive</strong> interval between <code>start<sub>i</sub></code> and <code>end<sub>i</sub></code>.</p>

<p>Return <code>true</code> <em>if each integer in the inclusive range</em> <code>[left, right]</code> <em>is covered by <strong>at least one</strong> interval in</em> <code>ranges</code>. Return <code>false</code> <em>otherwise</em>.</p>

<p>An integer <code>x</code> is covered by an interval <code>ranges[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> if <code>start<sub>i</sub> &lt;= x &lt;= end<sub>i</sub></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> ranges = [[1,10],[10,20]], left = 21, right = 21
<strong>Output:</strong> false
<strong>Explanation:</strong> 21 is not covered by any range.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= ranges.length &lt;= 50</code></li>
	<li><code>1 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 50</code></li>
	<li><code>1 &lt;= left &lt;= right &lt;= 50</code></li>
</ul>

# Brute Force Solution 
```python
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums_in_ranges = set()

        for l, r in ranges:
            for num in range(l, r+1):
                nums_in_ranges.add(num)
        
        for num in range(left, right+1):
            if num not in nums_in_ranges:
                return False
        
        return True
```
---
```python
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered=[0]*51
        for start,end in ranges:
            for i in range(start,end+1):
                covered[i]=True
        for i in range(left,right+1):
            if not covered[i]:
                return False
        return True
```
# Difference Array Approach
[Diff Array Algo Apporach](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/solutions/7109522/beats-100-o51-prefix-sum-sweep-diff-arra-zcz5/)

```python
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52                         # 1..50 domain
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1
        cover = 0
        for x in range(1, 51):
            cover += diff[x]
            if left <= x <= right and cover == 0:
                return False
            if x == right:
                return True
        return True
```
