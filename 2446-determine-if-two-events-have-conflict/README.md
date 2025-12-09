<h2><a href="https://leetcode.com/problems/determine-if-two-events-have-conflict">2536. Determine if Two Events Have Conflict</a></h2><h3>Easy</h3><hr><p>You are given two arrays of strings that represent two inclusive events that happened <strong>on the same day</strong>, <code>event1</code> and <code>event2</code>, where:</p>

<ul>
	<li><code>event1 = [startTime<sub>1</sub>, endTime<sub>1</sub>]</code> and</li>
	<li><code>event2 = [startTime<sub>2</sub>, endTime<sub>2</sub>]</code>.</li>
</ul>

<p>Event times are valid 24 hours format in the form of <code>HH:MM</code>.</p>

<p>A <strong>conflict</strong> happens when two events have some non-empty intersection (i.e., some moment is common to both events).</p>

<p>Return <code>true</code><em> if there is a conflict between two events. Otherwise, return </em><code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> event1 = [&quot;01:15&quot;,&quot;02:00&quot;], event2 = [&quot;02:00&quot;,&quot;03:00&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong> The two events intersect at time 2:00.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> event1 = [&quot;01:00&quot;,&quot;02:00&quot;], event2 = [&quot;01:20&quot;,&quot;03:00&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong> The two events intersect starting from 01:20 to 02:00.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> event1 = [&quot;10:00&quot;,&quot;11:00&quot;], event2 = [&quot;14:00&quot;,&quot;15:00&quot;]
<strong>Output:</strong> false
<strong>Explanation:</strong> The two events do not intersect.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>event1.length == event2.length == 2</code></li>
	<li><code>event1[i].length == event2[i].length == 5</code></li>
	<li><code>startTime<sub>1</sub> &lt;= endTime<sub>1</sub></code></li>
	<li><code>startTime<sub>2</sub> &lt;= endTime<sub>2</sub></code></li>
	<li>All the event times follow the <code>HH:MM</code> format.</li>
</ul>

# Solution 
* We can do the comparison with the strings itself no need to change them to intergers. 
* Everytime we assume `EVENT1` starts before `EVENT2` and make required changes when working on it. 

```python
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1, end1 = event1
        start2, end2 = event2

        if start1 > start2:  # if event2 starts before event1 we swap the variables
            start1, start2 = start2, start1
            end1, end2 = end2, end1
				# This way we are sure to assure that event1 should be over before event2
        
        if end1 >= start2: # checking the conflict
            return True        # End time of earlier event should not conflict with the start of the next event
        else:
            return False
```
---
```python
class Solution:
    def haveConflict(self, a: list[str], b: list[str]) -> bool:
        a_start, a_end = a
        b_start, b_end = b

        # First event starts before second ends or ends after second starts
        if b_start <= a_start <= b_end or b_start <= a_end <= b_end:
            return True

        # Second event starts before first ends or ends after first starts
        if a_start <= b_start <= a_end or a_start <= b_end <= a_end:
            return True

        return False
```
