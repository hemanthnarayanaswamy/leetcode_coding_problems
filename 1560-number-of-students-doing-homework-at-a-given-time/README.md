<h2><a href="https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time">1560. Number of Students Doing Homework at a Given Time</a></h2><h3>Easy</h3><hr><p>Given two integer arrays <code>startTime</code> and <code>endTime</code> and given an integer <code>queryTime</code>.</p>

<p>The <code>ith</code> student started doing their homework at the time <code>startTime[i]</code> and finished it at time <code>endTime[i]</code>.</p>

<p>Return <em>the number of students</em> doing their homework at time <code>queryTime</code>. More formally, return the number of students where <code>queryTime</code> lays in the interval <code>[startTime[i], endTime[i]]</code> inclusive.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
<strong>Output:</strong> 1
<strong>Explanation:</strong> We have 3 students where:
The first student started doing homework at time 1 and finished at time 3 and wasn&#39;t doing anything at time 4.
The second student started doing homework at time 2 and finished at time 2 and also wasn&#39;t doing anything at time 4.
The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> startTime = [4], endTime = [4], queryTime = 4
<strong>Output:</strong> 1
<strong>Explanation:</strong> The only student was doing their homework at the queryTime.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>startTime.length == endTime.length</code></li>
	<li><code>1 &lt;= startTime.length &lt;= 100</code></li>
	<li><code>1 &lt;= startTime[i] &lt;= endTime[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= queryTime &lt;= 1000</code></li>
</ul>

# Solution 
* Imagine that startTime[i] and endTime[i] form an interval `(i.e. [startTime[i], endTime[i]]).`
* The answer is how many times the queryTime laid in those mentioned intervals.

1. For each student time check if the query lies in the range of the start and end time. 

```python
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        result = 0

        for t1,t2 in zip(startTime, endTime):
            if queryTime in range(t1, t2+1):
                result += 1
        
        return result
```

```python
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        for i in range(len(startTime)):
            if  queryTime >= startTime[i] and queryTime<=endTime[i]:
                count+=1
        return count        
```

# Optimal Solution 
* You’re already at the optimal O(n) time (you have to look at each student at least once) and O(1) extra space. You can, however, shave off a bit of Python overhead and make it more idiomatic by:
1. Avoiding the creation of a new range object on every iteration
2. Pushing the loop into a C‐level construct with sum

```python
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        # sum up 1 for each (s,e) where s <= queryTime <= e
        return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))
```
