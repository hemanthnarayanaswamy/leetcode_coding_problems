<h2><a href="https://leetcode.com/problems/merge-intervals">56. Merge Intervals</a></h2><h3>Medium</h3><hr><p>Given an array&nbsp;of <code>intervals</code>&nbsp;where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, merge all overlapping intervals, and return <em>an array of the non-overlapping intervals that cover all the intervals in the input</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,3],[2,6],[8,10],[15,18]]
<strong>Output:</strong> [[1,6],[8,10],[15,18]]
<strong>Explanation:</strong> Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,4],[4,5]]
<strong>Output:</strong> [[1,5]]
<strong>Explanation:</strong> Intervals [1,4] and [4,5] are considered overlapping.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>

## Solution Approach 
![approach](https://assets.leetcode.com/users/criskgl/image_1574967731.png)

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]  ## Initiating result with first element of intervals for references 
        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1],intervals[i][1])
            else:
                result.append(intervals[i])
        return result
```

## Improved Solution
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]  ## Initiating result with first element of intervals for references 
        for i in range(1, len(intervals)):
            current_element = result[-1][1]
            if current_element >= intervals[i][0]:
                result[-1][1] = max(current_element,intervals[i][1])
            else:
                result.append(intervals[i])
                
        return result
```

## Optimal Solution
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort()
        #sort the intervals by the first values
        intervals.sort(key = lambda i: i[0])
        result = [intervals[0]]  ## Initiating result with first element of intervals for references 
        for i in range(1, len(intervals)):
            current_element = result[-1]
            next_element = intervals[i]
            if current_element[1] >= next_element[0]:
                current_element[1] = max(current_element[1],next_element[1])
            else:
                result.append(next_element)

        return result
```
